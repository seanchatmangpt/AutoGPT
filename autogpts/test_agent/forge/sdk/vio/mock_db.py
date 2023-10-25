# Generate a mock database that matches the OpenAPI schema
def generate_compliant_mock_db():
    """
    Generate a mock database that is compliant with the OpenAPI schema for the AutoGPT Arena Hacks hackathon.

    Returns:
        dict: A mock database containing tasks, steps, and artifacts mapped to various hackathon prize categories.
    """
    # Initialize a dictionary to hold the tasks, steps, and artifacts for each prize category.
    mock_db = {
        "General Challenge": {
            "tasks": [],
            "pagination": {
                "total_items": 0,
                "total_pages": 0,
                "current_page": 1,
                "page_size": 25,
            },
        },
        "Scrape and Synthesize": {
            "tasks": [],
            "pagination": {
                "total_items": 0,
                "total_pages": 0,
                "current_page": 1,
                "page_size": 25,
            },
        },
        # ... Add other categories here
    }

    # Populate the 'General Challenge' category as an example.
    mock_db["General Challenge"]["tasks"].append(
        {
            "task_id": "1",
            "input": "Write an algorithm to solve Sudoku puzzles",
            "additional_input": {"debug": False, "mode": "benchmark"},
            "artifacts": [
                {
                    "artifact_id": "artifact_1",
                    "agent_created": True,
                    "file_name": "sudoku_solver.py",
                    "relative_path": "python/code/",
                }
            ],
            "steps": [
                {
                    "step_id": "1a",
                    "task_id": "1",
                    "input": "Initialize a 9x9 Sudoku board",
                    "additional_input": {"file_to_refactor": "sudoku_solver.py"},
                    "status": "completed",
                    "is_last": False,
                    "artifacts": [],
                    "additional_output": {"tokens": 7894, "estimated_cost": "0.24$"},
                },
                {
                    "step_id": "1b",
                    "task_id": "1",
                    "input": "Implement backtracking algorithm",
                    "additional_input": {"file_to_refactor": "sudoku_solver.py"},
                    "status": "completed",
                    "is_last": True,
                    "artifacts": [],
                    "additional_output": {"tokens": 1520, "estimated_cost": "0.05$"},
                },
            ],
        }
    )

    # Update pagination details for 'General Challenge'
    mock_db["General Challenge"]["pagination"]["total_items"] = len(
        mock_db["General Challenge"]["tasks"]
    )
    mock_db["General Challenge"]["pagination"]["total_pages"] = 1  # As an example

    return mock_db


# Generate the mock data
mock_db = generate_compliant_mock_db()
