# tests/test_main.py
from hello.main import add


def test_add():
    assert add(2, 3) == 5
