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


from typing import List
from pydantic import BaseModel, Field, conlist
from agent.openapi_client.models.pagination import Pagination
from agent.openapi_client.models.task import Task

class TaskListResponse(BaseModel):
    """
    TaskListResponse
    """
    tasks: conlist(Task) = Field(...)
    pagination: Pagination = Field(...)
    __properties = ["tasks", "pagination"]

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
    def from_json(cls, json_str: str) -> TaskListResponse:
        """Create an instance of TaskListResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in tasks (list)
        _items = []
        if self.tasks:
            for _item in self.tasks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tasks'] = _items
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskListResponse:
        """Create an instance of TaskListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskListResponse.parse_obj(obj)

        _obj = TaskListResponse.parse_obj({
            "tasks": [Task.from_dict(_item) for _item in obj.get("tasks")] if obj.get("tasks") is not None else None,
            "pagination": Pagination.from_dict(obj.get("pagination")) if obj.get("pagination") is not None else None
        })
        return _obj


