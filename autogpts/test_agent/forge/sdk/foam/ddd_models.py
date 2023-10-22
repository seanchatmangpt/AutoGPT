from typing import Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from utils.yaml_tools import YAMLMixin

T = TypeVar("T", bound="YAMLMixin")


# Base classes
class Require(YAMLMixin, BaseModel):
    condition: str


class Ensure(YAMLMixin, BaseModel):
    condition: str


# Domain classes
class Factory(YAMLMixin, BaseModel):
    name: str
    parameters: List[Dict[str, str]]


class Method(YAMLMixin, BaseModel):
    name: str
    parameters: List[Dict[str, str]]


class Repository(YAMLMixin, BaseModel):
    name: str
    methods: List[Method]


class ValueObject(YAMLMixin, BaseModel):
    name: str
    definition: str
    properties: List[Dict[str, str]]


class BusinessFunction(YAMLMixin, BaseModel):
    name: str
    parameters: List[Dict[str, str]]
    definition: str
    contract: Dict[str, List[Union[Require, Ensure]]]


class Entity(YAMLMixin, BaseModel):
    name: str
    definition: str
    business_functions: List[BusinessFunction]
    factories: List[Factory]
    repositories: List[Repository]


class Aggregate(YAMLMixin, BaseModel):
    root_entity: str
    entities: List[Entity]
    value_objects: List[ValueObject]
    aggregate_business_functions: List[BusinessFunction]


class DDD(YAMLMixin, BaseModel):
    aggregates: List[Aggregate]
