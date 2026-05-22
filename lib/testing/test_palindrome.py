from palindrome import longest_palindromic_substring


def test_single_character_string():
    assert longest_palindromic_substring("a") == "a"


def test_entire_string_is_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_even_length_palindrome():
    assert longest_palindromic_substring("cbbd") == "bb"


def test_odd_length_palindrome():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]


def test_no_long_palindrome_returns_single_character():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]


def test_longer_palindrome_inside_string():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"


def test_digits_and_letters():
    assert longest_palindromic_substring("abc1234321xyz") == "1234321"