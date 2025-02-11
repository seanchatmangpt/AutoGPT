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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class Artifact(BaseModel):
    """
    An Artifact either created by or submitted to the agent.  # noqa: E501
    """
    artifact_id: StrictStr = Field(..., description="ID of the artifact.")
    agent_created: StrictBool = Field(..., description="Whether the artifact has been created by the agent.")
    file_name: StrictStr = Field(..., description="Filename of the artifact.")
    relative_path: Optional[StrictStr] = Field(None, description="Relative path of the artifact in the agent's workspace.")
    __properties = ["artifact_id", "agent_created", "file_name", "relative_path"]

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
    def from_json(cls, json_str: str) -> Artifact:
        """Create an instance of Artifact from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if relative_path (nullable) is None
        # and __fields_set__ contains the field
        if self.relative_path is None and "relative_path" in self.__fields_set__:
            _dict['relative_path'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Artifact:
        """Create an instance of Artifact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Artifact.parse_obj(obj)

        _obj = Artifact.parse_obj({
            "artifact_id": obj.get("artifact_id"),
            "agent_created": obj.get("agent_created"),
            "file_name": obj.get("file_name"),
            "relative_path": obj.get("relative_path")
        })
        return _obj


