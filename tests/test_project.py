import shutil
import os
from pathlib import Path
from multidoc.generate import generate_cpp_documented, generate_pybind_documented
from multidoc.parsing import parse_api_docstrings


def test_cpp_project():
    # parse api docstring structure
    structure = parse_api_docstrings("test-docstrings")


def recurse_print_modules(structure, parent=""):
    if "modules" in structure.keys():
        for module in structure["modules"]:
            if parent:
                print(parent + "." + module)
            else:
                print(module)
            recurse_print_modules(structure[module], parent=module)


def test_pybind_project():
    # parse api docstring structure
    structure = parse_api_docstrings("test-docstrings")

    recurse_print_modules(structure)
    # for module in structure["modules"]:
    #     print(module)
    #     if "modules" in structure[module].keys():
    #         for


if __name__ == "__main__":
    generate_cpp_documented("../../tudat")
    generate_pybind_documented("../../tudatpy")
