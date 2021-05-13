from pydantic import BaseModel
from typing import List, Optional
from multidoc.parsing.io import yaml2dict


class FileBased(BaseModel):
    base_file: str

    @classmethod
    def from_yaml(cls, path, local: dict = None):
        local = local if local is not None else {}
        return cls.parse_obj(yaml2dict(path, local))


class Parameter(BaseModel):
    name: str
    type: Optional[str]
    desc: Optional[str]


class Returns(BaseModel):
    name: Optional[str]
    type: Optional[str]
    desc: str


class Yields(BaseModel):
    name: Optional[str]
    type: Optional[str]
    desc: Optional[str]


class Raises(BaseModel):
    name: str
    type: Optional[str]
    desc: Optional[str]


class Function(BaseModel):
    name: str

    short_summary: Optional[str]  # test
    deprecation_warning: Optional[str]
    extended_summary: Optional[str]
    parameters: Optional[List[Parameter]]
    returns: Optional[List[Returns] or Returns]
    yields: Optional[List[Yields] or Yields]
    other_parameters: Optional[List[Parameter] or Parameter]
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


class Module(FileBased):
    summary: Optional[str]
    extended_summary: Optional[str]
    routine_listings: Optional[str]
    see_also: Optional[str]
    notes: Optional[str]
    references: Optional[str]
    examples: Optional[str]

    # MODULE structure
    classes: Optional[List[str]]
    functions: Optional[List[str]]
    constants: Optional[List[str]]


class Package(FileBased):
    summary: Optional[str]
    extended_summary: Optional[str]
    routine_listings: Optional[str]
    see_also: Optional[str]
    notes: Optional[str]
    references: Optional[str]
    examples: Optional[str]

    # MODULE structure
    classes: Optional[List[str]]
    functions: Optional[List[str]]
    constants: Optional[List[str]]
    modules: Optional[List[Module]]