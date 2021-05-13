from multidoc.parsing import parse_api_docstrings
from multidoc.parsing import yaml2dict


def test_yaml_parser():
    t1 = yaml2dict("example.yaml")
    t2 = yaml2dict("example.yaml", {"py": True})
    t3 = yaml2dict("example.yaml", {"cpp": True})
    t4 = yaml2dict("example.yaml", {"cpp": True, "py": True})
    t5 = yaml2dict("example.yaml", {"cpp": True, "py": False})
    t6 = yaml2dict("example.yaml", {"cpp": False, "py": True})
    t7 = yaml2dict("example.yaml", {"cpp": False, "py": False})
    assert t1 == {'package': None, 'modules': ['module']}
    assert t2 == {'package': {'name': 'name-py'}, 'modules': ['module', 'module-py']}
    assert t3 == {'package': {'name': 'name-cpp'}, 'modules': ['module', 'module-cpp']}
    assert t4 == {'package': {'name': 'name-py'}, 'modules': ['module', 'module-py', 'module-cpp', 'module-both']}
    assert t5 == {'package': {'name': 'name-cpp'}, 'modules': ['module', 'module-cpp', 'module-not-py']}
    assert t6 == {'package': {'name': 'name-py'}, 'modules': ['module', 'module-py', 'module-not-cpp']}
    assert t7 == {'package': None, 'modules': ['module', 'module-not-cpp', 'module-not-py']}


def test_parsing_module_not_found():
    try:
        structure = parse_api_docstrings("test-docstrings-1")
    except Exception as e:
        assert type(e) == ModuleNotFoundError


def test_parsing():
    structure = parse_api_docstrings("test-docstrings")
    print(structure)

