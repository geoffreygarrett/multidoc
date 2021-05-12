import re

CPP_TAG = re.compile(
    r"(?P<indent>[^\S\r\n]+)?\/\/!\s+@get_docstring\((\s+)?((?P<cls>[\w]+)\.(?P<method>[\w]+))?(?P<func>\w+)?((\s+)?,(\s+)?(overload(\s+)?=(\s+)?)?(?P<variant>[0-9]+))?(\s+)?\)",
    flags=re.MULTILINE)

PYTHON_TAG = re.compile(
    r"(?P<indent>[^\S\r\n]+)?#\s+@get_docstring\((\s+)?((?P<cls>[\w]+)\.(?P<method>[\w]+))?(?P<func>\w+)?((\s+)?,(\s+)?(overload(\s+)?=(\s+)?)?(?P<variant>[0-9]+))?(\s+)?\)",
    flags=re.MULTILINE)
