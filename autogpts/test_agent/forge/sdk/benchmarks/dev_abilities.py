from forge.sdk.abilities.registry import *


@ability(
    name="list_files",
    description="List files in a directory",
    parameters=[
        AbilityParameter(
            name="path",
            description="Path to the directory",
            type="string",
            required=True,
        )
    ],
    output_type="list[str]",
)
async def list_files(agent, task_id: str, path: str) -> List[str]:
    """
    List files in a directory
    """
    try:
        files = os.listdir(path)
        return [file for file in files if os.path.isfile(os.path.join(path, file))]
    except Exception as e:
        raise Exception(f"Error listing files: {str(e)}")


@ability(
    name="write_file",
    description="Write data to a file",
    parameters=[
        AbilityParameter(
            name="file_path",
            description="Path to the file",
            type="string",
            required=True,
        ),
        AbilityParameter(
            name="data",
            description="Data to write to the file",
            type="bytes",
            required=True,
        ),
    ],
    output_type="None",
)
async def write_file(agent, task_id: str, file_path: str, data: bytes):
    """
    Write data to a file
    """
    try:
        with open(file_path, "wb") as file:
            file.write(data)
    except Exception as e:
        raise Exception(f"Error writing to file: {str(e)}")


@ability(
    name="read_file",
    description="Read data from a file",
    parameters=[
        AbilityParameter(
            name="file_path",
            description="Path to the file",
            type="string",
            required=True,
        ),
    ],
    output_type="bytes",
)
async def read_file(agent, task_id: str, file_path: str) -> bytes:
    """
    Read data from a file
    """
    try:
        with open(file_path, "rb") as file:
            data = file.read()
            return data
    except Exception as e:
        raise Exception(f"Error reading from file: {str(e)}")
