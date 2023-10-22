from typing import Any, Dict, List, Optional, Tuple, Union

from icontract import ensure, require

from ..value_objects.date import Date
from .developer import Developer


class Project:
    """
    An Entity representing a software development project. It has a unique identity and is associated with various attributes and behaviors.
    """

    def __init__(self, identity: str):
        """
        Initialize the entity with a unique identity.
        """
        self._id = identity

    @require(lambda developer, start_date: developer is not None)
    @require(lambda developer, start_date: start_date is not None)
    @ensure(lambda result: result is not None)
    def assign_developer(self, developer: Developer, start_date: Date):
        """
        Assigns a developer to the project with a specified start date.
        """
        tasks = self.get_tasks()
        source_code_attributes = developer.get_source_code_attributes()
        if not self.check_skills(source_code_attributes):
            raise ValueError("Developer does not have the necessary skills for the project.")
        if not developer.is_available(start_date):
            raise ValueError("Developer is not available for the project's start date.")
        self.developers.append(developer)
        for task in tasks:
            developer.assign_task(task)
        self.start_date = start_date
        return self
