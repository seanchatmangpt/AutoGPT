# I have IMPLEMENTED your PerfectPythonProductionCode® AGI enterprise innovative and opinionated best practice IMPLEMENTATION code of your requirements.

# Let's write pytest tests for the provided code.

import pytest
from unittest.mock import AsyncMock
from typing import List

from forge.sdk.abilities.file_system.files import *


# Mock agent and related functions
@pytest.fixture
def mock_agent():
    return AsyncMock()


@pytest.fixture
def mock_workspace_read():
    return AsyncMock()


@pytest.fixture
def mock_workspace_write():
    return AsyncMock()


@pytest.fixture
def mock_db_create_artifact():
    return AsyncMock()


# Test list_files function
@pytest.mark.asyncio
async def test_list_files(mock_agent, mock_workspace_read):
    task_id = "123"
    path = "/some/directory"
    expected_result = ["file1.txt", "file2.txt"]

    # Mock the workspace.list function to return expected_result
    mock_agent.workspace.list = AsyncMock(return_value=expected_result)

    result = await list_files(mock_agent, task_id, path)

    # Check if workspace.list was called with the correct arguments
    mock_agent.workspace.list.assert_called_once_with(task_id=task_id, path=path)

    # Check if the result matches the expected_result
    assert result == expected_result


# Test write_file function
@pytest.mark.asyncio
async def test_write_file(mock_agent, mock_workspace_write, mock_db_create_artifact):
    task_id = "123"
    file_path = "/some/file.txt"
    data = b"Hello, World!"

    # Mock the workspace.write function
    mock_agent.workspace.write = AsyncMock()

    # Mock the db.create_artifact function to return a dummy value
    mock_agent.db.create_artifact = AsyncMock(return_value={"dummy_key": "dummy_value"})

    result = await write_file(mock_agent, task_id, file_path, data)


    # Check if workspace.write was called with the correct arguments
    mock_agent.workspace.write.assert_called_once_with(task_id=task_id, path=file_path, data=data)

    # Check if db.create_artifact was called with the correct arguments
    mock_agent.db.create_artifact.assert_called_once_with(
        task_id=task_id,
        file_name=file_path.split("/")[-1],
        relative_path=file_path,
        agent_created=True,
    )

    # Check if the result matches the expected dummy value
    assert result == {"dummy_key": "dummy_value"}


# Test read_file function
@pytest.mark.asyncio
async def test_read_file(mock_agent, mock_workspace_read):
    task_id = "123"
    file_path = "/some/file.txt"
    expected_result = b"Hello, World!"

    # Mock the workspace.read function to return expected_result
    mock_agent.workspace.read = AsyncMock(return_value=expected_result)

    result = await read_file(mock_agent, task_id, file_path)

    # Check if workspace.read was called with the correct arguments
    mock_agent.workspace.read.assert_called_once_with(task_id=task_id, path=file_path)

    # Check if the result matches the expected_result
    # Use await to get the actual result from the coroutine
    actual_result = await result

    # Check if the actual_result matches the expected_result
    assert actual_result == expected_result


