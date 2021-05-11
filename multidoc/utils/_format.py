from textwrap import indent


def indent_line(s, indent_with):
    return indent(s, indent_with, lambda line: True)


def snake2camel(s):
    return ''.join(word.title() for word in s.split('_'))


def snake2pascal(s):
    camel = snake2camel(s)
    return camel[0].lower() + camel[1:]
