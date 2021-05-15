from setuptools import setup

setup(name='multidoc',
      version='0.0.1',
      description="Automated API Documentation.",
      long_description="Automated API Documentation for multiple programming languages",
      author='TODO',
      author_email='todo@example.org',
      license='TODO',
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