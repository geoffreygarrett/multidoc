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
          ('share/templates', ['multidoc/templates/cpp.jinja2']),
          ('share/templates', ['multidoc/templates/cpp-sphinx-module.jinja2']),
          ('share/templates', ['multidoc/templates/docstring_h.jinja2']),
          ('share/templates', ['multidoc/templates/enum-member.jinja2']),
          ('share/templates', ['multidoc/templates/numpydoc.jinja2']),
          ('share/templates', ['multidoc/templates/property.jinja2']),
          ('share/templates', ['multidoc/templates/py.jinja2']),
          ('share/templates', ['multidoc/templates/py-sphinx-module.jinja2']),
          ('share/templates', ['multidoc/templates/pybind_base.jinja2']),
          ('share/templates', ['multidoc/templates/reStructuredText.jinja2']),
      ],
      install_requires=[
          'jinja2',
          'pyyaml',
          'pydantic',
      ],
      )
