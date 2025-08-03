import pytest

from calculator import  add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_iteself():
    assert add("77") == 77

def test_two_numbers_returns_sum():
    assert add("1,2") == 3

def test_unknown_number_of_integers():
    assert add("1,2,3,4,5") == 15

def test_new_line_as_delimiter():
    assert add("1\n2,3\n4\n5") == 15

def test_custom_delimiter():
    assert add("//;\n1;2;3") == 6

def test_empty_values_between_commas_are_skipped():
    assert add("1,,2") == 3

def test_leading_and_trailing_delimiters():
    assert add(",1,2,") == 3

def test_one_negative_number_throw_not_allowed_error():
    with pytest.raises(ValueError, match="negative numbers not allowed -5"):
        add(" 1, -5, 5")

def test_multiple_negative_number_throw_not_allowed_error():
    with pytest.raises(ValueError, match="negative numbers not allowed -5, -3, -2"):
        add(" 1, -5, 5, -3, -2")

def test_ignores_greater_than_1000_numbers():
    assert add("1,2,3,4,1010,5") == 15

def test_invalid_number_raises_exception():
    with pytest.raises(ValueError, match=r"invalid number found: a"):
        add("1,2,a")

def test_invalid_number_with_custom_delimiter():
    with pytest.raises(ValueError, match=r"invalid number found: xyz"):
        add("//;\n1;xyz;2")

def test_delimiter_of_any_length():
    assert add("//***\n1***2***3***4***5") == 15

def test_multiple_delimiters():
    assert add("//[*][#][&][,]\n1*2#3&4\n5")


