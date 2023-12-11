from pydantic import BaseModel
from typing import List, Optional, Union
from multidoc.parsing.io import yaml2dict


#
# class DocStyle(BaseModel):
#     pass
#
# #
# class NumpyDoc(DocStyle):
#     name: str
#     short_summary: Optional[str]
#     deprecation_warning: Optional[str]
#     extended_summary: Optional[str]
#     parameters: Optional[List[Parameter]]
#     returns: Optional[Returns] or Optional[List[Returns]]
#     yields: Optional[List[Yields] or Yields]
#     other_parameters: Optional[List[Parameter]]
#     raises: Optional[List[Raises] or Raises]
#     warns: Optional[List[Raises] or Raises]
#     warnings: Optional[str]
#     see_also: Optional[str]
#     notes: Optional[str]
#     references: Optional[str]
#     examples: Optional[str]


# class APIElement(BaseModel):
#     name: str

class APIDeclaration:
    pass


class FileBased(BaseModel):
    """FileBased declaration ``pydantic.BaseModel`` data structure.

    Attributes
    ----------


    """
   
    
    @classmethod
    def parse_yaml(cls, path, **kwargs):
        """

        Parameters
        ----------
        path
        local

        Returns
        -------

        """
        return cls.parse_obj(yaml2dict(path, **kwargs))


class DirBased(FileBased):

    @classmethod
    def parse_yaml(cls, path, local: dict = None):
        """

        Parameters
        ----------
        path
        local

        Returns
        -------

        """
        local = local if local is not None else {}
        return cls.parse_obj(yaml2dict(path, local))


class Parameter(BaseModel):
    """Parameter docstring ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Parameter.name : str
    Parameter.type : Optional[str] = None
    Parameter.description : Optional[str] = None

    Examples
    --------


    .. code-block:: yaml
      :caption: Used in :class:`~multidoc.parsing.Function` parameters.

      functions:
       - name: foo_function
         parameters:
          - name: bar_parameter
            type: Any
            description: "The bar parameter"

    .. code-block:: yaml
       :caption: Used in :class:`~multidoc.parsing.Class` method parameters.

       classes:
        - name: FooClass
          methods:
           - name: bar_method
             parameters:
              - name: bar_parameter
                type: Any
                description: "The bar parameter"

    """
    name: str
    type: Optional[str] = None
    description: Optional[str] = None


class Property(BaseModel):
    """
    Attributes
    ----------
    Property.name : str
    Property.type : Optional[str] = None
    Property.description : Optional[str] = None
    Property.readonly : bool = False
    """
    name: str
    type: Optional[str] = None
    description: Optional[str] = None
    readonly : bool = False


class Returns(BaseModel):
    """Returns docstring ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Returns.name : Optional[str] = None
    Returns.type : Optional[str] = None
    Returns.description : Optional[str] = None

    """

    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None

class AutoClassConfig(BaseModel):
    """
    See https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoclass
    """
    members: Optional[str] = None
    undoc_members: Optional[str] = None
    private_members: Optional[str] = None
    special_members: Optional[str] = None
    no_undoc_members: Optional[bool] = None
    inherited_members: Optional[bool] = None

class Yields(BaseModel):
    """Yields docstring ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Yields.name: Optional[str] = None
    Yields.type: Optional[str] = None
    Yields.description: Optional[str] = None

    """
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None


class Raises(BaseModel):
    """Raises docstring ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Raises.name: str
    Raises.type: Optional[str] = None
    Raises.description: Optional[str] = None

    """
    name: str
    type: Optional[str] = None
    description: Optional[str] = None
    
class Warns(BaseModel):
    """Warns docstring ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Warns.name: Optional[str] = None
    Warns.type: Optional[str] = None
    Warns.description: Optional[str] = None

    """
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None


class Function(BaseModel):
    """Function docstring ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Function.name : str
    Function.short_summary: Optional[str] = None  # test
    Function.deprecation_warning : Optional[str]= None
    Function.extended_summary : Optional[str]= None
    Function.parameters : Optional[Union[List[Parameter], Parameter]] = None
    Function.returns: Optional[Union[List[Returns], Returns]] = None
    Function.yields: Optional[Union[List[Yields], Yields]] = None
    Function.other_parameters: Optional[Union[List[Parameter], Parameter]] = None
    Function.raises: Optional[Union[List[Raises], Raises]] = None
    Function.warns : Optional[Union[List[Warns], Warns]] = None
    Function.warnings : Optional[str]= None
    Function.see_also : Optional[str]= None
    Function.notes : Optional[str]= None
    Function.references : Optional[str]= None
    Function.examples : Optional[str]= None

    """
    name: str
    short_summary: Optional[str] = None
    deprecation_warning: Optional[str] = None
    extended_summary: Optional[str] = None
    parameters: Optional[Union[List[Parameter], Parameter]] = None
    returns: Optional[Union[List[Returns], Returns]] = None
    yields: Optional[Union[List[Yields], Yields]] = None    
    other_parameters: Optional[Union[List[Parameter], Parameter]] = None
    raises: Optional[Union[List[Raises], Raises]] = None
    warns: Optional[Union[List[Warns], Warns]] = None
    warnings: Optional[str] = None
    see_also: Optional[str] = None
    notes: Optional[str] = None
    references: Optional[str] = None
    examples: Optional[str] = None


class EnumMember(BaseModel):
    name: str
    description: Optional[str] = None
    value: Optional[int] = None


class Class(BaseModel):
    """Class docstring ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Class.name : str
    Class.short_summary : Optional[str] = None  # test
    Class.deprecation_warning : Optional[str] = None
    Class.extended_summary : Optional[str] = None
    Class.parameters : Optional[Union[List[Parameter], Parameter]] = None
    Class.attributes : Optional[Union[List[Parameter], Parameter]] = None
    Class.properties : Optional[List[Property]] = None 
    Class.yields : Optional[Union[List[Yields], Yields]] = None
    Class.other_parameters : Optional[Union[List[Parameter], Parameter]] = None
    Class.raises : Optional[Union[List[Raises], Raises]] = None
    Class.warns : Optional[Union[List[Warns], Warns]] = None
    Class.warnings : Optional[str] = None
    Class.see_also : Optional[str] = None
    Class.notes : Optional[str] = None
    Class.references : Optional[str] = None
    Class.examples : Optional[str] = None
    Class.methods : Optional[str] = None
    Class.autoclass: Optional[AutoClassConfig] = None

    """

    name: str
    short_summary: Optional[str] = None
    deprecation_warning: Optional[str] = None
    extended_summary: Optional[str] = None
    parameters: Optional[Union[List[Parameter], Parameter]] = None
    attributes: Optional[Union[List[Parameter], Parameter]] = None
    properties: Optional[List[Property]] = None 
    yields: Optional[Union[List[Yields], Yields]] = None
    other_parameters: Optional[Union[List[Parameter], Parameter]] = None
    raises: Optional[Union[List[Raises], Raises]] = None
    warns: Optional[Union[List[Warns], Warns]] = None
    warnings: Optional[str] = None
    see_also: Optional[str] = None
    notes: Optional[str] = None
    references: Optional[str] = None
    examples: Optional[str] = None
    methods: Optional[List[Function]] = None
    autoclass: Optional[AutoClassConfig] = None


class Enum(BaseModel):
    name: str
    short_summary: Optional[str] = None
    extended_summary: Optional[str] = None
    members: Optional[List[EnumMember]] = None


class Constant(BaseModel):
    """Constant docstring ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Constant.summary: str
    Constant.extended_summary: Optional[str] = None
    Constant.see_also: Optional[str] = None
    Constant.references: Optional[str] = None
    Constant.examples: Optional[str] = None

    """
    summary: str
    extended_summary: Optional[str] = None
    see_also: Optional[str] = None
    references: Optional[str] = None
    examples: Optional[str] = None


class Config(BaseModel):
    """Multidoc module config ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Config.name: Optional[str] = None
    Config.version: Optional[str] = None

    """
    name: Optional[str] = None
    version: Optional[str] = None


class Module(FileBased):
    """Module docstring ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Module.config: Optional[Config] = None  
    
    Module.summary: Optional[str] = None
    Module.extended_summary: Optional[str] = None
    Module.routine_listings: Optional[str] = None
    Module.see_also: Optional[str] = None
    Module.notes: Optional[str] = None
    Module.references: Optional[str] = None
    Module.examples: Optional[str] = None
    
    Module.enums: Optional[List[Enum]] = None
    Module.classes: Optional[List[Class]] = None
    Module.functions: Optional[List[Function]] = None
    Module.constants: Optional[List[Constant]] = None

    """
    config: Optional[Config] = None
    
    summary: Optional[str] = None
    extended_summary: Optional[str] = None
    routine_listings: Optional[str] = None
    see_also: Optional[str] = None
    notes: Optional[str] = None
    references: Optional[str] = None
    examples: Optional[str] = None
    

    # MODULE structure
    enums: Optional[List[Enum]] = None
    classes: Optional[List[Class]] = None
    functions: Optional[List[Function]] = None
    constants: Optional[List[Constant]] = None


class Package(Module):
    """Module docstring ``pydantic.BaseModel`` data structure.

    Attributes
    ----------
    Package.config: Optional[Config] = None
    Package.summary: Optional[str] = None
    Package.extended_summary: Optional[str] = None
    Package.routine_listings: Optional[str] = None
    Package.see_also: Optional[str] = None
    Package.notes: Optional[str] = None
    Package.references: Optional[str] = None
    Package.examples: Optional[str] = None
    Package.classes: Optional[List[Class]] = None
    Package.functions: Optional[List[Function]] = None
    Package.constants: Optional[List[Constant]] = None
    Package.modules: Optional[List[str]] = None

    """
    modules: Optional[List[str]] = None

    # def __init__(self):
    #     super().__init__()
    #


if __name__ == "__main__":
    import json

    # r = Package.schema()
    # print(json.dumps(r, indent=4))
    # p = Package()
    # print(p)
