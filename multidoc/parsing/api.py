import re
import os
from multidoc.template import render_python_docstring
from multidoc.template import render_cpp_docstring
from multidoc.parsing.io import yaml2dict
from multidoc.parsing import logger


def recursive_parse(module_prefix, local: dict = None):
    local = local if local is not None else {}
    structure = {}

    # module is defined as directory
    if os.path.isdir(module_prefix):
        has_submodules = True
        module_yaml = yaml2dict(os.path.join(module_prefix, "__module__.yaml"), local)
        structure["modules"] = module_yaml["modules"]

    # module is defined as .yaml file
    elif os.path.isfile(str(module_prefix) + ".yaml"):
        has_submodules = False
        module_yaml = yaml2dict(str(module_prefix) + ".yaml", local)

    # module is defined as .yml file
    elif os.path.isfile(str(module_prefix) + ".yml"):
        has_submodules = False
        module_yaml = yaml2dict(str(module_prefix) + ".yml", local)

    # module api is not defined correctly
    else:
        raise ModuleNotFoundError("module api is not defined correctly")

    structure["name"] = os.path.basename(module_prefix)

    # module level functions
    if "functions" in module_yaml.keys():
        structure["functions"] = module_yaml["functions"]
        for function in module_yaml["functions"]:
            structure[function["name"]] = parse_function(function, local)

    # module level functions
    if "classes" in module_yaml.keys():
        structure["classes"] = module_yaml["classes"]
        for _class in module_yaml["classes"]:
            structure[_class["name"]] = parse_class(_class, local)

    # module level functions
    if "constants" in module_yaml.keys():
        structure["constants"] = module_yaml["constants"]
        for constant in module_yaml["constants"]:
            structure[constant["name"]] = parse_constant(constant, local)

    if has_submodules:
        # iterate through api level modules
        for submodule in structure["modules"]:
            submodule_prefix = os.path.join(module_prefix, submodule)
            structure[submodule] = recursive_parse(submodule_prefix, local)
        return structure
    else:
        return structure


# from abc import ABC, abstractmethod
#
#
# class BaseDocstring(ABC):
#
#     @abstractmethod
#     def render(self, structure):
#         pass
#
#
# class CppDocstring(BaseDocstring):
#     _locals = {"cpp": True}
#
#     def render(self, structure):
#         return render_cpp_docstring(structure)


def parse_function(function, _locals):
    """

    Parameters
    ----------
    function
    _locals

    Returns
    -------

    """
    logger.info(f"Parsing function: {function['name']} with locals: {_locals}")
    if "cpp" in _locals.keys() and "py" in _locals.keys():
        assert (_locals["cpp"] == _locals["cpp"] & _locals["cpp"] is True) is False
    if "cpp" in _locals.keys():
        if _locals["cpp"]:
            return render_cpp_docstring(function)

    if "py" in _locals.keys():
        if _locals["py"]:
            # print(function)
            return render_python_docstring(function)


def parse_method(function, _locals):
    """

    Parameters
    ----------
    function
    _locals

    Returns
    -------

    """
    logger.info(f"Parsing method: {function['name']} with locals: {_locals}")
    if "cpp" in _locals.keys() and "py" in _locals.keys():
        assert (_locals["cpp"] == _locals["cpp"] & _locals["cpp"] is True) is False
    if "cpp" in _locals.keys():
        if _locals["cpp"]:
            return render_cpp_docstring(function)

    if "py" in _locals.keys():
        if _locals["py"]:
            # print(function)
            return render_python_docstring(function)


import json


def parse_class(_class, _locals):
    """

    Parameters
    ----------
    _class
    _locals

    Returns
    -------

    """
    logger.info(f"Parsing class: {_class['name']} with locals: {_locals}")
    _return = {}
    methods = _class["methods"] if "methods" in _class.keys() else None
    if methods:
        for method in methods:
            _return[method["name"]] = parse_method(method, _locals)
    _return["__docstring__"] = parse_method(_class, _locals)
    return _return


def parse_constant(constant, _locals):
    """

    Parameters
    ----------
    constant
    _locals

    Returns
    -------

    """
    return constant

from multidoc.parsing.models import Module


def parse_api_docstrings(prefix: str, local: dict = None):
    """

    Parameters
    ----------
    prefix
    local

    Returns
    -------

    """
    structure = dict()
    structure["prefix"] = prefix
    local = local if local is not None else dict()

    r = re.compile(r"__api__.(?P<ext>\w+)")
    api_file = list(filter(r.match, os.listdir(prefix)))

    if len(api_file) == 0:
        raise ModuleNotFoundError("__api__.yaml/yml not found in prefix.")
    elif len(api_file) > 1:
        raise ModuleNotFoundError("Multiple __api__.yaml/yml found in prefix.")

    # load module from __module__.yaml/yml
    module = Module.from_yaml(os.path.join(prefix, api_file[0]), local)

    # are there submodules present?
    structure["modules"] = module.modules
    structure["name"] = module.package.name

    # module level functions
    if module.functions:
        structure["functions"] = module.functions
        for function in module.functions:
            structure[function.name] = parse_function(function, local)

    # module level functions
    if module.classes:
        structure["classes"] = api_yaml["classes"]
        for _class in api_yaml["classes"]:
            structure[_class["name"]] = parse_class(_class, local)

    # module level functions
    if module.constants:
        structure["constants"] = api_yaml["constants"]
        for constant in api_yaml["constants"]:
            structure[constant["name"]] = parse_constant(constant, local)

    # iterate through api level modules
    if module.modules:
        for submodule in module.modules:
            module_path = os.path.join(prefix, module)
            structure[module] = recursive_parse(module_path, local)

    return structure
