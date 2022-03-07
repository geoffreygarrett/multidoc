from setuptools import setup
import setuptools

setup(name='multidoc',
      version='0.0.1',
      description="Automated API Documentation.",
      long_description=("A Python library that automates C++/Pybind11/Python" +
                        " docstring generation from a single source."),
      author='geoffreygarrett',
      author_email='geoffreygarrett99@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      zip_safe=False,
      data_files=[
          ('multidoc', ['multidoc/templates/cpp.jinja2']),
          ('multidoc', ['multidoc/templates/cpp-sphinx-module.jinja2']),
          ('multidoc', ['multidoc/templates/docstring_h.jinja2']),
          ('multidoc', ['multidoc/templates/enum-member.jinja2']),
          ('multidoc', ['multidoc/templates/numpydoc.jinja2']),
          ('multidoc', ['multidoc/templates/property.jinja2']),
          ('multidoc', ['multidoc/templates/py.jinja2']),
          ('multidoc', ['multidoc/templates/py-sphinx-module.jinja2']),
          ('multidoc', ['multidoc/templates/pybind_base.jinja2']),
          ('multidoc', ['multidoc/templates/reStructuredText.jinja2']),
      ],
      install_requires=[
          'jinja2',
          'pyyaml',
          'pydantic',
      ],
      )
