import jinja2
import os
from multidoc import TEMPLATE_DIR
from multidoc.parsing import parse_api_docstrings
import json
from multidoc.template import DEFAULT_PYBIND_TEMPLATE, generate_pybind_docstring




def test_pybind_template():
    structure = parse_api_docstrings("test-docstrings")
    # print(structure["name"])

    # s = json.dumps(structure, indent=4)
    # print(s)
    with open(os.path.join(TEMPLATE_DIR, "pybind_docstring.jinja2"), "r") as f:
        t = jinja2.Template(f.read())

    with open(os.path.join(".", "docstrings.h"), "w") as f:
        f.write(t.render(api_structure=structure))


if __name__ == "__main__":
    structure = parse_api_docstrings("test-docstrings")
    print(structure)

    with open(os.path.join(TEMPLATE_DIR, "pybind_docstring.jinja2"), "r") as f:
        t = jinja2.Template(f.read())
    print(t.render(structure))
