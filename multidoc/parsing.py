import re
import os
import yaml
import pathlib
from multidoc.template import render_python_docstring
from multidoc.template import render_cpp_docstring

CPP_PATTERN = re.compile(r"(?P<indent>[^\S\r\n]+)?\/\/!\s+@get_docstring\((?P<name>[\w,.]+)?(,\s?(?P<variant>\w+))?\)",
                         flags=re.MULTILINE)
PY_PATTERN = re.compile(r"(?P<indent>[^\S\r\n]+)?#\s+@get_docstring\((?P<name>[\w,.]+)?(,\s?(?P<variant>\w+))?\)",
                        flags=re.MULTILINE)


# def yaml2dict(path, tags=None):
#     re.compile()
#     with open(path) as file:
#         dict_ = yaml.load(file, Loader=yaml.FullLoader)
#         return dict_


def yaml2dict(path, _locals: dict = None, include_unknown=False):
    """

    Parameters
    ----------
    path : os.PathLike or str
        Path of the ``yaml`` file to be loaded.
    _locals : Dict[str, Any]
        List of definitions to parse in the yaml files. See examples for how
        they affect yaml loading.
    include_unknown : bool, default=True
        Include tag evaluations that return an error

    Examples
    ========
    Given the following example ``yaml`` file:

    .. code-block:: yaml
        :caption: example.yaml

        package:
          name: name-cpp    # [cpp]
          name: name-py     # [py]

        modules:
          - module
          - module-py       # [py]
          - module-cpp      # [cpp]
          - module-both     # [py or cpp]

    >>> yaml2dict("example.yaml")
    {'package': None, 'modules': ['module']}

    >>> yaml2dict("example.yaml", _locals={"cpp":True})
    {'package': {'name': 'name-cpp'}, 'modules': ['module', 'module-cpp', 'module-both']}

    >>> yaml2dict("example.yaml", _locals={"py": True})
    {'package': {'name': 'name-py'}, 'modules': ['module', 'module-py', 'module-both']}


    Returns
    -------
    dict
        ``yaml`` loaded into memory as Python dict, parsed for definitions.

    """
    locals().update(_locals) if _locals else None
    regex = re.compile(r".*#\s*\[(?P<expr>.*)\]")
    with open(path) as file:
        _lines = file.readlines()
        lines = []
        for line in _lines:
            match = regex.match(line)
            if match:  # there's an expr on this line
                try:
                    # if the expr is True, add to lines, else ignore
                    if eval(match.group("expr")):
                        lines += line
                except NameError:
                    # if the expr raises a NameError (e.g. undefined var in expr)
                    if include_unknown:
                        lines += line
                    else:
                        pass
            else:
                lines += line
        dict_ = yaml.load("".join(lines), yaml.Loader)
        return dict_


def recursive_parse(module_prefix, _locals: dict = None):
    structure = {}

    # module is defined as directory
    if os.path.isdir(module_prefix):
        has_submodules = True
        module_yaml = yaml2dict(os.path.join(module_prefix, "__module__.yaml"), _locals)
        structure["modules"] = module_yaml["modules"]

    # module is defined as .yaml file
    elif os.path.isfile(str(module_prefix) + ".yaml"):
        has_submodules = False
        module_yaml = yaml2dict(str(module_prefix) + ".yaml", _locals)

    # module is defined as .yml file
    elif os.path.isfile(str(module_prefix) + ".yml"):
        has_submodules = False
        module_yaml = yaml2dict(str(module_prefix) + ".yml", _locals)

    # module api is not defined correctly
    else:
        raise ModuleNotFoundError("module api is not defined correctly")

    structure["name"] = os.path.basename(module_prefix)

    # module level functions
    if "functions" in module_yaml.keys():
        structure["functions"] = module_yaml["functions"]
        for function in module_yaml["functions"]:
            structure[function["name"]] = parse_function(function, _locals)

    # module level functions
    if "classes" in module_yaml.keys():
        structure["classes"] = module_yaml["classes"]
        for _class in module_yaml["classes"]:
            structure[_class["name"]] = parse_class(_class, _locals)

    # module level functions
    if "constants" in module_yaml.keys():
        structure["constants"] = module_yaml["constants"]
        for constant in module_yaml["constants"]:
            structure[constant["name"]] = parse_constant(constant, _locals)

    if has_submodules:
        # iterate through api level modules
        for submodule in structure["modules"]:
            submodule_prefix = os.path.join(module_prefix, submodule)
            structure[submodule] = recursive_parse(submodule_prefix, _locals)
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
    if "cpp" in _locals.keys() and "py" in _locals.keys():
        assert (_locals["cpp"] == _locals["cpp"] & _locals["cpp"] is True) is False
    if "cpp" in _locals.keys():
        if _locals["cpp"]:
            return render_cpp_docstring(function)

    if "py" in _locals.keys():
        if _locals["py"]:
            return render_python_docstring(function)


def parse_class(_class, _locals):
    """

    Parameters
    ----------
    _class
    _locals

    Returns
    -------

    """
    _return = {}
    _return[""]
    if "methods" in _class.keys():
        for function in _class["methods"]:
            _return[function["name"]] = parse_function(function, _locals)

    return _class


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


def parse_api_docstrings(prefix: str, _locals: dict = None):
    """

    Parameters
    ----------
    prefix
    _locals

    Returns
    -------

    """
    structure = dict()
    structure["prefix"] = prefix

    # api definition is a .yaml file
    if os.path.isfile(os.path.join(prefix, "__api__.yaml")):
        api_yaml_path = os.path.join(prefix, "__api__.yaml")
        api_yaml = yaml2dict(api_yaml_path, _locals)

    # api definition is a .yml file
    elif os.path.isfile(os.path.join(prefix, "__api__.yml")):
        api_yaml_path = os.path.join(prefix, "__api__.yml")
        api_yaml = yaml2dict(api_yaml_path, _locals)

    # api docstrings are not defined correctly
    else:
        raise FileNotFoundError("__api__.yml or __api__.yaml must be in api docstrings prefix.")

    # api has to have modules
    structure["modules"] = api_yaml["modules"]
    structure["name"] = api_yaml["package"]["name"]

    # module level functions
    if "functions" in api_yaml.keys():
        structure["functions"] = api_yaml["functions"]
        for function in api_yaml["functions"]:
            structure[function["name"]] = parse_function(function, _locals)

    # module level functions
    if "classes" in api_yaml.keys():
        structure["classes"] = api_yaml["classes"]
        for _class in api_yaml["classes"]:
            structure[_class["name"]] = parse_class(_class, _locals)

    # module level functions
    if "constants" in api_yaml.keys():
        structure["constants"] = api_yaml["constants"]
        for constant in api_yaml["constants"]:
            structure[constant["name"]] = parse_constant(constant, _locals)

    # iterate through api level modules
    for module in structure["modules"]:
        module_path = os.path.join(prefix, module)
        structure[module] = recursive_parse(module_path, _locals)

    return structure
