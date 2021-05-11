from collections import namedtuple
from jinja2 import Template
import os
from multidoc.utils import indent_line
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")


def add_line_prefix(multi_line_string, prefix="* "):
    res = prefix + ("\n" + prefix).join(multi_line_string.split("\n"))
    return res



# load the template arguments for
LanguageTemplates = namedtuple('LanguageTemplates', "cpp py")

with open(os.path.join(TEMPLATE_DIR, "numpydoc.jinja2"), 'r') as f_py, open(os.path.join(TEMPLATE_DIR, "cpp.jinja2"),
                                                                       'r') as f_cpp:
    t = LanguageTemplates(
        cpp=Template(f_cpp.read(), lstrip_blocks=True, trim_blocks=True),
        py=Template(f_py.read()))
# trim_blocks and lstrip_blocks
t.cpp.globals["add_line_prefix"] = add_line_prefix
t.cpp.globals["indent_line"] = indent_line

# jinja2 template arguments for multiline cpp
cpp_args = dict(start=r"/** ",
                suffix=" * ",
                end=" */",
                package={'name': 'tudat'})

# jinja2 template arguments for python, this is superfluous, but fixes error
py_args = dict(
    start="",
    suffix="",
    end="",
    package={'name': 'tudatpy'}
)


# render the templates to source code
def render_cpp_docstring(args):
    return t.cpp.render(**args, **cpp_args)


def render_python_docstring(args):
    return t.py.render(**args, **py_args)
