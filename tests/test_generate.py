from jinja2 import Template
from multidoc.generate import (generate_cpp_documented,
                               generate_pybind_documented,
                               generate_pybind_docstring,
                               generate_cpp_docstring,
                               generate_cpp_sphinx,
                               generate_py_sphinx)
import os
import shutil


def test_cpp_documented():
    generate_cpp_documented(api_prefix="test-docstrings",
                            target_src="test-cpp")

    # test the documented source is generated
    assert os.path.exists(".test-cpp-documented")

    # remove the generated documented source
    shutil.rmtree(".test-cpp-documented")


def test_pybind_documented():
    generate_pybind_documented(api_prefix="test-docstrings",
                               target_src="test-pybind")

    # test the documented source is generated
    assert os.path.exists(".test-pybind-documented")

    # remove the generated documented source
    shutil.rmtree(".test-pybind-documented")


def test_generate_pybind_docstring():
    generate_pybind_docstring(api_prefix="test-docstrings",
                              dest="docstrings.h")


def test_generate_cpp_docstring():
    generate_cpp_docstring(api_prefix="test-docstrings",
                           include_path="test-cpp/include", dest="test-cpp-doc-dest")


def test_generate_cpp_sphinx():
    generate_cpp_sphinx(
        api_prefix="../tests/test-docstrings",
        dest_dir="test-sphinx-cpp")

def test_generate_py_sphinx():
    generate_py_sphinx(
        api_prefix="../tests/test-docstrings",
        dest_dir="test-sphinx-py")


generate_template = """        } else if (name == "@docstring_key") {
            
            return "@docstring_body";"""
