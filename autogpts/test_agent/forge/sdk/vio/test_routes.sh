#!/bin/bash

# Base API URL
BASE_URL="http://127.0.0.1:8000/ap/v1/agent"

# POST: Create a new task
echo "Creating a new task..."
TASK_ID=$(curl -s -X POST "${BASE_URL}/tasks" -H "accept: application/json" -H "Content-Type: application/json" -d '{"input": "do something", "additional_input": {"key": "value"}}' | jq -r '.task_id')
echo "Created task with ID: $TASK_ID"

# GET: List tasks
echo "Listing tasks..."
curl -s -X GET "${BASE_URL}/tasks" -H "accept: application/json"

# GET: Retrieve a task by its ID
echo "Retrieving task by ID..."
curl -s -X GET "${BASE_URL}/tasks/$TASK_ID" -H "accept: application/json"

# POST: Execute a step in a task
echo "Executing a step in the task..."
STEP_ID=$(curl -s -X POST "${BASE_URL}/tasks/$TASK_ID/steps" -H "accept: application/json" -H "Content-Type: application/json" -d '{"action": "run", "parameters": {"param1": "value1"}}' | jq -r '.step_id')
echo "Executed step with ID: $STEP_ID"

# GET: List all steps for a task
echo "Listing all steps for the task..."
curl -s -X GET "${BASE_URL}/tasks/$TASK_ID/steps" -H "accept: application/json"

# GET: Retrieve a specific step by its ID
echo "Retrieving specific step by its ID..."
curl -s -X GET "${BASE_URL}/tasks/$TASK_ID/steps/$STEP_ID" -H "accept: application/json"

# POST: Upload an artifact for a task (assuming a file named 'example.txt' exists)
echo "Uploading an artifact for the task..."
ARTIFACT_ID=$(curl -s -X POST "${BASE_URL}/tasks/$TASK_ID/artifacts" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "file=@example.txt" | jq -r '.artifact_id')
echo "Uploaded artifact with ID: $ARTIFACT_ID"

# GET: List all artifacts for a task
echo "Listing all artifacts for the task..."
curl -s -X GET "${BASE_URL}/tasks/$TASK_ID/artifacts" -H "accept: application/json"

# GET: Download a specific artifact by its ID
echo "Downloading a specific artifact by its ID..."
curl -s -X GET "${BASE_URL}/tasks/$TASK_ID/artifacts/$ARTIFACT_ID" -H "accept: application/json"

echo "Finished testing all routes."
