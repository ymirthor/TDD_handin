from project import *

def test_add_empty_string():
    assert add("") == 0

def test_add_sigle_digit():
    assert add("1") == 1

def test_add_two_digits():
    assert add("1,2") == 3
