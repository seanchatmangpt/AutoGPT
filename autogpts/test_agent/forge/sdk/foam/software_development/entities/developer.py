from typing import Any, Dict, List, Optional, Tuple, Union

from icontract import ensure, require

from ..value_objects.source_code_attributes import SourceCodeAttributes
from ..value_objects.task import Task
from .source_code import SourceCode


class Developer:
    """
    An Entity representing a developer involved in a software project. It has a unique identity and associated properties.
    """

    def __init__(self, identity: str):
        """
        Initialize the entity with a unique identity.
        """
        self._id = identity

    @require(lambda task: task is not None)
    @ensure(lambda result: result is not None)
    def complete_task(self, task: Task):
        """
        Marks a task as completed by the developer.
        """
        task.completed = True
        return task

    @require(lambda task: task is not None)
    @ensure(lambda result: result is not None)
    def analyze_code(self, task: Task):
        """
        Analyzes the source code within the context of a specific task.
        """
        source_code_attributes = self._extract_source_code_attributes(task)
        code_analysis_result = self._perform_code_analysis(source_code_attributes)
        return code_analysis_result

    @require(lambda task: task is not None)
    @ensure(lambda result: result is not None)
    def fix_code(self, task: Task):
        """
        Fixes the source code within the context of a specific task.
        """
        source_code_attributes = self.get_source_code_attributes(task)
        if not self.is_valid_source_code(source_code_attributes):
            raise ValueError("Source code is not valid.")
        fixed_source_code = self.fix_source_code(source_code_attributes)
        task = self.update_task(task, fixed_source_code)
        return task

    @require(lambda source_code: source_code is not None)
    @ensure(lambda result: result is not None)
    def is_valid_source_code(self, source_code: SourceCode):
        """
        Checks if the given source code is valid.
        """
        if not source_code:
            return False
        if not source_code.filepath:
            return False
        if not source_code.classes:
            return False
        if not source_code.functions:
            return False
        if not source_code.imports:
            return False
        return True

    @require(lambda source_code: source_code is not None)
    @ensure(lambda result: result is not None)
    def add_necessary_imports(self, source_code: SourceCode):
        """
        Adds necessary imports to the given source code.
        """
        imports = source_code.imports
        if "datetime" not in imports:
            imports.append("datetime")
        if "typing" not in imports:
            imports.append("typing")
        source_code.imports = imports
        return source_code

    @require(lambda source_code: source_code is not None)
    @ensure(lambda result: result is not None)
    def get_necessary_imports(self, source_code: SourceCode):
        """
        Gets the list of necessary imports for the given source code.
        """
        necessary_imports = []
        classes = source_code.classes
        functions = source_code.functions
        if classes or functions:
            necessary_imports.append("from typing import List")
        if classes:
            necessary_imports.append("from dataclasses import dataclass, field")
        if functions:
            necessary_imports.append("from typing import List")
        if source_code.imports:
            necessary_imports.append("from typing import List")
        return necessary_imports

    def _extract_source_code_attributes(self, task: Task) -> SourceCodeAttributes:
        """
        Extracts source code attributes from the given task.
        """
        filepath = task.description
        classes = self._extract_classes(filepath)
        functions = self._extract_functions(filepath)
        imports = self._extract_imports(filepath)
        return SourceCodeAttributes(
            filepath=filepath, classes=classes, functions=functions, imports=imports
        )

    def _extract_classes(self, filepath: str) -> List[str]:
        """
        Extracts classes from the given filepath.
        """
        with open(filepath, "r") as file:
            file_contents = file.read()
            classes = re.findall("class\\s+(\\w+)", file_contents)
            return classes

    def _extract_functions(self, filepath: str) -> List[str]:
        """
        Extracts functions from the given filepath.
        """
        with open(filepath, "r") as file:
            file_contents = file.read()
            functions = re.findall("def\\s+(\\w+)", file_contents)
            return functions

    def _extract_imports(self, filepath: str) -> List[str]:
        """
        Extracts imports from the given filepath.
        """
        with open(filepath, "r") as file:
            file_contents = file.read()
            imports = re.findall("import\\s+(\\w+)", file_contents)
            return imports

    def _perform_code_analysis(
        self, source_code_attributes: SourceCodeAttributes
    ) -> CodeAnalysisResult:
        """
        Performs code analysis on the given source code attributes.
        """
        filepath = source_code_attributes.filepath
        classes = source_code_attributes.classes
        functions = source_code_attributes.functions
        imports = source_code_attributes.imports
        return CodeAnalysisResult(
            filepath=filepath, classes=classes, functions=functions, imports=imports
        )

    def get_source_code_attributes(self, task: Task) -> SourceCodeAttributes:
        """
        Gets the source code attributes from the given task.
        """
        filepath = task.description
        classes = self.get_source_code_classes(filepath)
        functions = self.get_source_code_functions(filepath)
        imports = self.get_source_code_imports(filepath)
        source_code_attributes = SourceCodeAttributes(
            filepath=filepath, classes=classes, functions=functions, imports=imports
        )
        return source_code_attributes

    def fix_source_code(self, source_code_attributes: SourceCodeAttributes) -> str:
        """
        Fixes the given source code.
        """
        fixed_filepath = self.fix_source_code_filepath(source_code_attributes.filepath)
        fixed_classes = self.fix_source_code_classes(source_code_attributes.classes)
        fixed_functions = self.fix_source_code_functions(source_code_attributes.functions)
        fixed_imports = self.fix_source_code_imports(source_code_attributes.imports)
        fixed_source_code = self.create_fixed_source_code(
            fixed_filepath, fixed_classes, fixed_functions, fixed_imports
        )
        return fixed_source_code

    def update_task(self, task: Task, fixed_source_code: str) -> Task:
        """
        Updates the given task with the fixed source code.
        """
        task.description = fixed_source_code
        return task

    def get_source_code_classes(self, filepath: str) -> List[str]:
        """
        Gets the classes from the given source code filepath.
        """
        source_code = self.get_source_code(filepath)
        classes = self.parse_source_code_classes(source_code)
        return classes

    def get_source_code_functions(self, filepath: str) -> List[str]:
        """
        Gets the functions from the given source code filepath.
        """
        source_code = self.get_source_code(filepath)
        functions = self.parse_source_code_functions(source_code)
        return functions

    def get_source_code_imports(self, filepath: str) -> List[str]:
        """
        Gets the imports from the given source code filepath.
        """
        source_code = self.get_source_code(filepath)
        imports = self.parse_source_code_imports(source_code)
        return imports

    def is_valid_source_code_filepath(self, filepath: str) -> bool:
        """
        Checks if the given source code filepath is valid.
        """
        if not filepath:
            return False
        if not self.is_valid_filepath(filepath):
            return False
        if not self.has_valid_file_extension(filepath):
            return False
        return True

    def is_valid_source_code_classes(self, classes: List[str]) -> bool:
        """
        Checks if the given source code classes are valid.
        """
        if not classes:
            return False
        for class_name in classes:
            if not self.is_valid_class_name(class_name):
                return False
        return True

    def is_valid_source_code_functions(self, functions: List[str]) -> bool:
        """
        Checks if the given source code functions are valid.
        """
        if not functions:
            return False
        for function_name in functions:
            if not self.is_valid_function_name(function_name):
                return False
        return True

    def is_valid_source_code_imports(self, imports: List[str]) -> bool:
        """
        Checks if the given source code imports are valid.
        """
        if not imports:
            return False
        for import_name in imports:
            if not self.is_valid_import_name(import_name):
                return False
        return True

    def fix_source_code_filepath(self, filepath: str) -> str:
        """
        Fixes the given source code filepath.
        """
        fixed_filepath = self.fix_filepath(filepath)
        return fixed_filepath

    def fix_source_code_classes(self, classes: List[str]) -> List[str]:
        """
        Fixes the given source code classes.
        """
        fixed_classes = [self.fix_class_name(class_name) for class_name in classes]
        return fixed_classes

    def fix_source_code_functions(self, functions: List[str]) -> List[str]:
        """
        Fixes the given source code functions.
        """
        fixed_functions = [self.fix_function_name(function_name) for function_name in functions]
        return fixed_functions

    def fix_source_code_imports(self, imports: List[str]) -> List[str]:
        """
        Fixes the given source code imports.
        """
        fixed_imports = [self.fix_import_name(import_name) for import_name in imports]
        return fixed_imports

    def create_fixed_source_code(
        self, filepath: str, classes: List[str], functions: List[str], imports: List[str]
    ) -> str:
        """
        Creates the fixed source code from the given filepath, classes, functions, and imports.
        """
        fixed_source_code = self.create_source_code(filepath, classes, functions, imports)
        return fixed_source_code

    def get_source_code(self, filepath: str) -> str:
        """
        Gets the source code from the given filepath.
        """
        source_code = self.read_source_code(filepath)
        return source_code

    def parse_source_code_classes(self, source_code: str) -> List[str]:
        """
        Parses the classes from the given source code.
        """
        classes = self.parse_classes(source_code)
        return classes

    def parse_source_code_functions(self, source_code: str) -> List[str]:
        """
        Parses the functions from the given source code.
        """
        functions = self.parse_functions(source_code)
        return functions

    def parse_source_code_imports(self, source_code: str) -> List[str]:
        """
        Parses the imports from the given source code.
        """
        imports = self.parse_imports(source_code)
        return imports

    def is_valid_filepath(self, filepath: str) -> bool:
        """
        Checks if the given filepath is valid.
        """
        if not filepath:
            return False
        if not isinstance(filepath, str):
            return False
        return True

    def has_valid_file_extension(self, filepath: str) -> bool:
        """
        Checks if the given filepath has a valid file extension.
        """
        file_extension = self.get_file_extension(filepath)
        if not self.is_valid_file_extension(file_extension):
            return False
        return True

    def is_valid_class_name(self, class_name: str) -> bool:
        """
        Checks if the given class name is valid.
        """
        if not class_name:
            return False
        if not isinstance(class_name, str):
            return False
        return True

    def is_valid_function_name(self, function_name: str) -> bool:
        """
        Checks if the given function name is valid.
        """
