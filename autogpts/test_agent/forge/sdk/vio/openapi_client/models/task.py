# coding: utf-8

"""
    Agent Protocol

    Specification of the API protocol for communication with an agent.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from agent.openapi_client.models.artifact import Artifact


class Task(BaseModel):
    """
    Task
    """

    input: Optional[StrictStr] = Field(None, description="Input prompt for the task.")
    additional_input: Optional[Dict[str, Any]] = Field(
        None, description="Input parameters for the task. Any value is allowed."
    )
    task_id: StrictStr = Field(..., description="The ID of the task.")
    artifacts: conlist(Artifact) = Field(
        ..., description="A list of artifacts that the task has produced."
    )
    __properties = ["input", "additional_input", "task_id", "artifacts"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Task:
        """Create an instance of Task from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in artifacts (list)
        _items = []
        if self.artifacts:
            for _item in self.artifacts:
                if _item:
                    _items.append(_item.to_dict())
            _dict["artifacts"] = _items
        # set to None if input (nullable) is None
        # and __fields_set__ contains the field
        if self.input is None and "input" in self.__fields_set__:
            _dict["input"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Task:
        """Create an instance of Task from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Task.parse_obj(obj)

        _obj = Task.parse_obj(
            {
                "input": obj.get("input"),
                "additional_input": obj.get("additional_input"),
                "task_id": obj.get("task_id"),
                "artifacts": [
                    Artifact.from_dict(_item) for _item in obj.get("artifacts")
                ]
                if obj.get("artifacts") is not None
                else None,
            }
        )
        return _obj
