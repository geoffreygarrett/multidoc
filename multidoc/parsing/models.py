from pydantic import BaseModel
from typing import List, Optional
from multidoc.parsing.io import yaml2dict


class FileBased(BaseModel):

    @classmethod
    def from_yaml(cls, path, local: dict = None):
        local = local if local is not None else {}
        return cls.parse_obj(yaml2dict(path, local))


class Parameter(BaseModel):
    name: str
    type: Optional[str]
    description: Optional[str]


class Returns(BaseModel):
    name: Optional[str]
    type: Optional[str]
    description: str


class Yields(BaseModel):
    name: Optional[str]
    type: Optional[str]
    description: Optional[str]


class Raises(BaseModel):
    name: str
    type: Optional[str]
    description: Optional[str]


class Function(BaseModel):
    name: str

    short_summary: Optional[str]  # test
    deprecation_warning: Optional[str]
    extended_summary: Optional[str]
    parameters: Optional[List[Parameter]]
    returns: Optional[Returns] or Optional[List[Returns]]
    yields: Optional[List[Yields] or Yields]
    other_parameters: Optional[List[Parameter]]
    raises: Optional[List[Raises] or Raises]
    warns: Optional[List[Raises] or Raises]
    warnings: Optional[str]
    see_also: Optional[str]
    notes: Optional[str]
    references: Optional[str]
    examples: Optional[str]


class Class(BaseModel):
    name: str  # test
    short_summary: Optional[str]
    deprecation_warning: Optional[str]
    extended_summary: Optional[str]
    parameters: Optional[List[Parameter]]
    attributes: Optional[str]
    yields: Optional[List[Yields] or Yields]
    other_parameters: Optional[List[Parameter] or Parameter]
    raises: Optional[List[Raises] or Raises]
    warns: Optional[List[Raises] or Raises]
    warnings: Optional[str]
    see_also: Optional[str]
    notes: Optional[str]
    references: Optional[str]
    examples: Optional[str]
    methods: Optional[List[Function]]


class Constant(BaseModel):
    summary: str
    extended_summary: Optional[str]
    see_also: Optional[str]
    references: Optional[str]
    examples: Optional[str]


class Config(BaseModel):
    name: Optional[str]
    version: Optional[str]


class Module(FileBased):
    config: Optional[Config]

    summary: Optional[str]
    extended_summary: Optional[str]
    routine_listings: Optional[str]
    see_also: Optional[str]
    notes: Optional[str]
    references: Optional[str]
    examples: Optional[str]

    # MODULE structure
    classes: Optional[List[Class]]
    functions: Optional[List[Function]]
    constants: Optional[List[Constant]]


class Package(Module):
    modules: Optional[List[str]]
