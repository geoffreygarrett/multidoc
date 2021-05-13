import re

CPP_TAG = re.compile(
    r"(?P<indent>[^\S\r\n]+)?"   # Matches named group indent from start of line until comment.
    r"\/\/!"                     # Matches //! as user designed indentation of docstring.
    r"\s+"                       # Allows any number of whitespaces between start of comment and @.
    r"@get_docstring\("          # Matches '@get_docstring(' exactly.
    r"(\s+)?"                    # Allows any number (zero include) of whitespaces from '( until 'class' or 'func' name.
    r"("                         # Start of (optional) class regex group.
    r"(?P<cls>[\w]+)"                # Match a named group 'class' for a word of any length.
    r"\."                            # . match for separation between class name and method name.
    r"(?P<method>[\w]+)"             # Match a named group 'method' for a word of any length.
    r")?"                        # End of class regex group.
    r"(?P<func>\w+)?"                # Match (optional) named group 'func' for a word of any length.
    r"("                         # Start of overload matching group.
    r"(\s+)?"                        # Any number of whitespaces before comma.
    r","                             # Matches comma separating cls.method|func from overload variable.
    r"(\s+)?"                        # Any number (optional) of whitespaces after comma.
    r"(overload(\s+)?=(\s+)?"    # matches optional format of overload with overload key "overload = n"
    r")?"                      
    r"(?P<variant>[0-9]+)"       # Named group 'variant', int value between 0 and 9 ([0-9]), unlimited times (+)
    r")?"
    r"(\s+)?"                    # Optional whitespaces between closing parenthesis.
    r"\)",
    flags=re.MULTILINE)


PYTHON_TAG = re.compile(
    r"(?P<indent>[^\S\r\n]+)?"   # Matches named group indent from start of line until comment.
    r"#"                         # Matches # as user designed indentation of docstring.
    r"\s+"                       # Allows any number of whitespaces between start of comment and @.
    r"@get_docstring\("          # Matches '@get_docstring(' exactly.
    r"(\s+)?"                    # Allows any number (zero include) of whitespaces from '( until 'class' or 'func' name.
    r"("                         # Start of (optional) class regex group.
    r"(?P<cls>[\w]+)"                # Match a named group 'class' for a word of any length.
    r"\."                            # . match for separation between class name and method name.
    r"(?P<method>[\w]+)"             # Match a named group 'method' for a word of any length.
    r")?"                        # End of class regex group.
    r"(?P<func>\w+)?"                # Match (optional) named group 'func' for a word of any length.
    r"("                         # Start of overload matching group.
    r"(\s+)?"                        # Any number of whitespaces before comma.
    r","                             # Matches comma separating cls.method|func from overload variable.
    r"(\s+)?"                        # Any number (optional) of whitespaces after comma.
    r"(overload(\s+)?=(\s+)?"    # matches optional format of overload with overload key "overload = n"
    r")?"                      
    r"(?P<variant>[0-9]+)"       # Named group 'variant', int value between 0 and 9 ([0-9]), unlimited times (+)
    r")?"
    r"(\s+)?"                    # Optional whitespaces between closing parenthesis.
    r"\)",
    flags=re.MULTILINE)


API_TAG = re.compile(r".*#\s*\[(?P<expr>.*)\]")


# import re
#
# r_yaml: re.compile(r"(?P<name>\w+)(?P<ext>.yml|.yaml)")
# r = re.compile("__package__.(?P<ext>.yml|.yaml)")


# r = re.compile(r"__api__.(?P<ext>\w+)")
# api_file = list(filter(r.match, os.listdir(prefix)))
#
# if len(api_file) == 0:
#     raise ModuleNotFoundError("__api__.yaml/yml not found in prefix.")
# elif len(api_file) > 1:
#     raise ModuleNotFoundError("Multiple __api__.yaml/yml found in prefix.")

# load module from __module__.yaml/yml
# module = Module.from_yaml(os.path.join(prefix, api_file[0]), local)

