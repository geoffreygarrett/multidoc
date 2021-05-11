import re
from pathlib import Path
import yaml
from multidoc.parsing import parse_api_docstrings


def test_parsing_module_not_found():
    try:
        structure = parse_api_docstrings("test-docstrings-1")
    except Exception as e:
        assert type(e) == ModuleNotFoundError


def test_parsing():
    structure = parse_api_docstrings("test-docstrings")
    print("\n")
    for x in structure["interface"]["spice"]["functions"]:
        print(x)
    # print(structure)


def test_parse_cpp():
    test_file = list(Path("../../../tudat").rglob("spiceInterface.h"))[0]
    parse_file(test_file, CPP_PATTERN)


if __name__ == "__main__":
    test_parsing()

    api = parse_api_docstrings("../docstrings")
    print(api)
    # generate_pybind_docstrings(
    #
    # )
    #
    # replace_cpp_docstrings(
    #
    # )
