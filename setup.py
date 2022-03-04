from setuptools import setup

setup(name='multidoc',
      version='0.0.1',
      description="Automated API Documentation.",
      long_description=("A Python library that automates C++/Pybind11/Python" +
                        " docstring generation from a single source."),
      author='geoffreygarrett',
      author_email='geoffreygarrett99@gmail.com',
      license='MIT',
      packages=['multidoc'],
      zip_safe=False,
      install_requires=[
          'jinja2',
          'pyyaml',
          'pydantic',
          # 'Sphinx',
          # ^^^ Not sure if this is needed on readthedocs.org
          # 'something else?',
      ],
      )
