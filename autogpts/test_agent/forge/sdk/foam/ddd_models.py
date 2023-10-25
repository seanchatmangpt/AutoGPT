from typing import Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field


# Base classes
class Require(BaseModel):
    condition: str


class Ensure(BaseModel):
    condition: str


# Domain classes
class Factory(BaseModel):
    name: str
    parameters: List[Dict[str, str]]


class Method(BaseModel):
    name: str
    parameters: List[Dict[str, str]]


class Repository(BaseModel):
    name: str
    methods: List[Method]


class ValueObject(BaseModel):
    name: str
    definition: str
    properties: List[Dict[str, str]]


class BusinessFunction(BaseModel):
    name: str
    parameters: List[Dict[str, str]]
    definition: str
    contract: Dict[str, List[Union[Require, Ensure]]]


class Entity(BaseModel):
    name: str
    definition: str
    business_functions: List[BusinessFunction]
    factories: List[Factory]
    repositories: List[Repository]


class Aggregate(BaseModel):
    root_entity: str
    entities: List[Entity]
    value_objects: List[ValueObject]
    aggregate_business_functions: List[BusinessFunction]


class DDD(BaseModel):
    aggregates: List[Aggregate]
