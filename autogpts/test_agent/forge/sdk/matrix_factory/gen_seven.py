import asyncio

import asyncio
from random import random

import yaml

from fgn.completion.complete import acreate
from matrix_factory.afile import write, read
from matrix_factory.chat_helpers import best_models


async def generate_plan(given_input, steps):
    print("Generating plan...")
    plan_prompt = f"""
        Objective:
        Given the input, transform it into a structured YAML plan with {steps} main steps. Each main step should have a verbose instructive description.
        Sample Plan:
        
        The project blueprint details a systematic development of a full-stack CRUD application utilizing Flask and React. Initial steps encompass setting up distinct directories for frontend and backend, with the backend focusing on database models, API endpoints, and crucial security measures like JWT authentication. The frontend, initialized using 'npx create-react-app', emphasizes user interface components, seamless navigation with 'React-Router', and effective state management. Aesthetic refinement is achieved through chosen styling frameworks, ensuring a captivating user experience. Comprehensive documentation accompanies the application, promoting clarity and ease of future development.

        Sample Output:
        ```yaml
steps:
  - name: "Create project directory using mkdir"
    description: "Start by initializing a new project directory to house both the frontend and backend components. This structure ensures a clear separation of concerns and eases navigation. Utilize the 'mkdir' command to create the root directory, followed by subdirectories 'frontend' and 'backend'."

  - name: "Set up virtual environment and Flask app in backend folder"
    description: "Navigate to the 'backend' subdirectory and initiate a virtual environment to manage dependencies for the Flask application. Using `cookiecutter`, scaffold the Flask application, emphasizing the folder structure, app configurations, and database settings. This lays the foundation for the subsequent steps."

  - name: "Implement SQLAlchemy models and API endpoints in Flask"
    description: "With Flask initialized, proceed to define the 'Users' database model using SQLAlchemy, integrating attributes like 'id', 'name', 'email', and 'password'. Subsequently, develop the necessary API endpoints to handle CRUD operations for users. These endpoints will connect the frontend to the backend database."

  - name: "Incorporate JWT Authentication and Error Handling in Flask"
    description: "To ensure the security of the application, integrate JWT authentication. This facilitates user registration, login, and protection of certain routes. Additionally, implement error handlers to respond to specific HTTP status codes, such as 400, 404, and 500, providing users with informative feedback."

  - name: "Create React app using npx create-react-app in frontend folder"
    description: "Switching focus to the frontend, navigate to the 'frontend' subdirectory and bootstrap a new React application using 'npx create-react-app'. This command initializes a new React project with a standard folder structure, which provides a solid starting point for frontend development."

  - name: "Design User Interface and Implement Routing in React"
    description: "Begin frontend development by designing the user interface components based on the provided specifications. This includes views for listing users, displaying user details, and forms for creating or editing users. Integrate 'React-Router' for seamless navigation between these views. Furthermore, decide on the state management solution, either React Context or Redux, and set it up accordingly."

  - name: "Style the application and write comprehensive documentation"
    description: "To enhance user experience, implement styling using either 'styled-components' or a CSS framework like Bootstrap. Make sure the design is responsive and adheres to best practices. Parallelly, write detailed documentation for each feature, function, and component, ensuring future developers or team members can quickly grasp the application's structure and functionalities."

        ```

        Given Plan:
        {given_input}
        
        Given Output:
    ```yaml\n
        """

    return await acreate(
        prompt=plan_prompt, model=best_models[0], stop=["```"], max_tokens=500
    )


async def generate_meta_workflow(generated_plan, steps):
    print("Generating meta-workflow...")
    meta_workflow_prompt = f"""
    Objective: Generate a YAML meta-workflow that loads {steps} other workflow files.
    Sample Output:
    ```yaml
    workflow:
      - name: "create_project_directory"
        description: 
        params:
          path: "workflows/sub_workflow_1.yaml"
    ```
    Generated Plan:
    {generated_plan}
    
    Using the provided guidelines, transform the given input into the desired YAML format.
    ```yaml\n
    """
    print(meta_workflow_prompt)
    return await acreate(
        prompt=meta_workflow_prompt, model=best_models[0], stop=["```"], max_tokens=2500
    )


async def generate_sub_workflow(step, sub_steps):
    print(f"Generating sub-workflow {step['name']}...")
    sub_workflow_prompt = f"""
    Objective: Generate a YAML workflow that has {sub_steps} steps.
    Sample Output:
    ```yaml
    workflow:
      - name: "installation"
        description: "To install the project, follow these steps:"
        params:
          clone_command: "git clone https://link-to-project"
          navigate_command: "cd project-directory"
      - name: "fetch_items"
        description: "Endpoint to fetch all items."
        params:
          method: "GET"
          endpoint: "/api/items"
    ```
    Generated Plan:
    {step['description']}

    Using the provided guidelines, transform the given input into the desired YAML format.
    ```yaml\n
    """
    print(sub_workflow_prompt)
    return await acreate(
        prompt=sub_workflow_prompt, model=best_models[0], stop=["```"], max_tokens=2500
    )


async def write_to_file(content, path):
    await write(content, path)


async def generate_workflow_structure(given_input, steps=7, sub_steps=7):
    # Generate Plan
    generated_plan = await generate_plan(given_input, steps)

    # Generate Meta-Workflow
    # meta_workflow_result = await generate_meta_workflow(generated_plan, steps)
    # await write_to_file(meta_workflow_result, "workflows/meta_workflow.yaml")

    meta = yaml.load(await read("workflows/meta_workflow.yaml"), Loader=yaml.FullLoader)

    # Generate Sub-Workflows
    for step in meta.get("workflow"):
        sub_workflow_result = await generate_sub_workflow(step, sub_steps)
        await write_to_file(sub_workflow_result, step["params"]["path"])

    print("Workflows generation complete.")


async def main():
    steps = 7
    sub_steps = 1
    given_input = """
    Objective:
    Develop a full-stack CRUD application integrating Flask and React.

    Specifications:

    Backend (Flask):
    - **Database Models**: Implement models for 'Users' with attributes 'id', 'name', 'email', and 'password'. Utilize SQLAlchemy as the ORM.
    - **API Endpoints**:
      - GET /users: Fetch all users.
      - POST /users: Create a new user.
      - GET /users/<id>: Fetch details of a specific user.
      - PUT /users/<id>: Update a specific user.
      - DELETE /users/<id>: Delete a specific user.
    - **Authentication**: Implement JWT authentication.
    - **Error Handling**: Incorporate error handlers for 400, 404, and 500 status codes.

    Frontend (React):
    - **User List View**: Display a list of all users with options to 'Edit' or 'Delete' each user and a button to 'Add' a new user.
    - **User Detail View**: On selecting a user, show detailed information.
    - **User Creation Form**: A form to add a new user.
    - **User Edit Form**: A form to edit existing user details.
    - **Routing**: Implement routing with React-Router. Include routes for the list view, detail view, creation, and editing.
    - **State Management**: Utilize React Context or Redux for managing the application state.
    - **Styling**: Implement styling using a library like 'styled-components' or CSS frameworks like Bootstrap.

    Click Tests:
    - **Navigation Test**: Ensure that the user can navigate between different views using both buttons and the URL.
    - **Creation Test**: Confirm that a user can be added using the form.
    - **Editing Test**: Verify that user details can be modified using the edit form.
    - **Deletion Test**: Confirm that a user can be deleted.
    - **Error Handling Test**: Check how the application handles errors, e.g., trying to access a non-existent user.

    It's essential that the application is built following best practices, is maintainable, and considers both security and performance. Include comprehensive documentation for each feature and function.
    """
    await generate_workflow_structure(given_input, steps, sub_steps)


if __name__ == "__main__":
    asyncio.run(main())
