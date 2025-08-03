from calculator import  add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_iteself():
    assert add("77") == 77

def test_two_numbers_returns_sum():
    assert add("1,2") == 3

def test_unknown_number_of_integers():
    assert add("1,2,3,4,5") == 15