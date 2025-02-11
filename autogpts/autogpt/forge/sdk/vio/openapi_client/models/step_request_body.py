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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class StepRequestBody(BaseModel):
    """
    Body of the task request.  # noqa: E501
    """
    input: Optional[StrictStr] = Field(None, description="Input prompt for the step.")
    additional_input: Optional[Dict[str, Any]] = Field(None, description="Input parameters for the task step. Any value is allowed.")
    __properties = ["input", "additional_input"]

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
    def from_json(cls, json_str: str) -> StepRequestBody:
        """Create an instance of StepRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if input (nullable) is None
        # and __fields_set__ contains the field
        if self.input is None and "input" in self.__fields_set__:
            _dict['input'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StepRequestBody:
        """Create an instance of StepRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StepRequestBody.parse_obj(obj)

        _obj = StepRequestBody.parse_obj({
            "input": obj.get("input"),
            "additional_input": obj.get("additional_input")
        })
        return _obj


