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
from agent.openapi_client.models.artifact import Artifact
from agent.openapi_client.models.pagination import Pagination


class TaskArtifactsListResponse(BaseModel):
    """
    TaskArtifactsListResponse
    """

    artifacts: conlist(Artifact) = Field(...)
    pagination: Pagination = Field(...)
    __properties = ["artifacts", "pagination"]

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
    def from_json(cls, json_str: str) -> TaskArtifactsListResponse:
        """Create an instance of TaskArtifactsListResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict["pagination"] = self.pagination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaskArtifactsListResponse:
        """Create an instance of TaskArtifactsListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaskArtifactsListResponse.parse_obj(obj)

        _obj = TaskArtifactsListResponse.parse_obj(
            {
                "artifacts": [
                    Artifact.from_dict(_item) for _item in obj.get("artifacts")
                ]
                if obj.get("artifacts") is not None
                else None,
                "pagination": Pagination.from_dict(obj.get("pagination"))
                if obj.get("pagination") is not None
                else None,
            }
        )
        return _obj
