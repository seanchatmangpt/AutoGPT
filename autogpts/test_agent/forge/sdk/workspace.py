import abc
import os
import typing
from pathlib import Path
from loguru import logger


class Workspace(abc.ABC):
    @abc.abstractclassmethod
    def __init__(self, base_path: str) -> None:
        self.base_path = base_path

    @abc.abstractclassmethod
    def read(self, task_id: str, path: str) -> bytes:
        pass

    @abc.abstractclassmethod
    def write(self, task_id: str, path: str, data: bytes) -> None:
        pass

    @abc.abstractclassmethod
    def delete(
        self, task_id: str, path: str, directory: bool = False, recursive: bool = False
    ) -> None:
        pass

    @abc.abstractclassmethod
    def exists(self, task_id: str, path: str) -> bool:
        pass

    @abc.abstractclassmethod
    def list(self, task_id: str, path: str) -> typing.List[str]:
        pass

class LocalWorkspace(Workspace):
    def __init__(self, base_path: str):
        self.base_path = Path(base_path).resolve()

    def _resolve_path(self, task_id: str, path: str) -> Path:
        path = str(path)
        path = path if not path.startswith("/") else path[1:]
        abs_path = (self.base_path / task_id / path).resolve()
        if not str(abs_path).startswith(str(self.base_path)):
            logger.error("Directory traversal is not allowed! - {abs_path}")
            raise ValueError(f"Directory traversal is not allowed! - {abs_path}")
        try:
            abs_path.parent.mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            pass
        return abs_path

    def read(self, task_id: str, path: str) -> bytes:
        logger.info(f"Reading file: {path}")
        with open(self._resolve_path(task_id, path), "rb") as f:
            data = f.read()
        logger.info(f"Read {len(data)} bytes from file: {path}")
        return data

    def write(self, task_id: str, path: str, data: bytes) -> None:
        file_path = self._resolve_path(task_id, path)
        logger.info(f"Writing {len(data)} bytes to file: {path}")
        with open(file_path, "wb") as f:
            f.write(data)
        logger.info(f"Data written to file: {path}")

    def delete(
        self, task_id: str, path: str, directory: bool = False, recursive: bool = False
    ) -> None:
        path = self.base_path / task_id / path
        resolved_path = self._resolve_path(task_id, path)
        if directory:
            if recursive:
                logger.info(f"Deleting directory recursively: {path}")
                os.rmdir(resolved_path)
            else:
                logger.info(f"Deleting directory: {path}")
                os.removedirs(resolved_path)
        else:
            logger.info(f"Deleting file: {path}")
            os.remove(resolved_path)

    def exists(self, task_id: str, path: str) -> bool:
        path = self.base_path / task_id / path
        exists = self._resolve_path(task_id, path).exists()
        logger.info(f"Checking existence of {path}: {exists}")
        return exists

    def list(self, task_id: str, path: str) -> typing.List[str]:
        path = self.base_path / task_id / path
        base = self._resolve_path(task_id, path)
        if not base.exists() or not base.is_dir():
            return []
        files = [str(p.relative_to(self.base_path / task_id)) for p in base.iterdir()]
        logger.info(f"Listed files in directory {path}: {files}")
        return files
