from project import *

def test_add_empty_string():
    assert add("") == 0

def test_add_sigle_digit():
    assert add("1") == 1

def test_add_two_digits():
    assert add("1,2") == 3

def test_add_mult_digits():
    assert add("1,2,3,4,5") == 15
    assert add("10,2,5,22,1,1") == 41

def test_newline_split():
    assert add("1\n2,3") == 6