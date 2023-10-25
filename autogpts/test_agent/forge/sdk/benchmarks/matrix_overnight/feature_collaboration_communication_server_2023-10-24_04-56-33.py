# Feature: Collaboration and communication.
# Scenario: The system should provide communication and collaboration tools for team members to discuss and work on code

# import necessary libraries
import asyncio
import websockets


# create a server to handle incoming websocket connections
async def server(websocket, path):
    # receive messages from the client
    async for message in websocket:
        # print the message received
        print(message)


# start the server on a specific port
start_server = websockets.serve(server, "localhost", 8765)

# start the event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


# Feature: Task assignment and tracking.
# Scenario: The system should allow managers to assign tasks to team members and track their progress.

# import necessary libraries
import uuid
from datetime import datetime


# function to assign a unique task id
def assign_id():
    return str(uuid.uuid4())


# function to create a new task
def create_task(name, description, assignee):
    # assign a unique id to the task
    task_id = assign_id()
    # get the current date and time
    created_at = datetime.now()
    # initialize the task status as 'incomplete'
    status = "incomplete"
    # create a dictionary to store the task details
    task = {
        "id": task_id,
        "name": name,
        "description": description,
        "assignee": assignee,
        "created_at": created_at,
        "status": status,
    }
    return task


# function to update the status of a task
def update_task_status(task, status):
    # check if the task exists
    if task:
        # update the task status
        task["status"] = status
        return task
    else:
        return None


# Feature: User-friendly interface.
# Scenario: The system should have a user-friendly interface that is easy to navigate and understand.

# import necessary libraries
import PySimpleGUI as sg

# define the layout of the GUI
layout = [
    [sg.Text("Welcome to the Task Manager!")],
    [sg.Text("Task Name:"), sg.InputText()],
    [sg.Text("Task Description:"), sg.InputText()],
    [sg.Text("Assignee:"), sg.InputText()],
    [
        sg.Button("Create Task"),
        sg.Button("Assign Task"),
        sg.Button("Update Task Status"),
    ],
]

# create the window
window = sg.Window("Task Manager", layout)

# event loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.Read()
    # check if the user clicked the 'Create Task' button
    if event == "Create Task":
        # create a new task
        task = create_task(values[0], values[1], values[2])
        # print the task details
        print(task)
    # check if the user clicked the 'Assign Task' button
    elif event == "Assign Task":
        # create a new task
        task = create_task(values[0], values[1], values[2])
        # update the task status to 'assigned'
        task = update_task_status(task, "assigned")
        # print the updated task details
        print(task)
    # check if the user clicked the 'Update Task Status' button
    elif event == "Update Task Status":
        # update the task status to 'completed'
        task = update_task_status(task, "completed")
        # print the updated task details
        print(task)
