import pytest
  # замените 'your_module' на имя вашего модуля

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
def test_only_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") == 0

def test_mixed_string():
    assert count_vowels("Hello World!") == 3

def test_empty_string():
    assert count_vowels("") == 0

def test_vowels_and_numbers():
    assert count_vowels("a1e2i3o4u5") == 5

def test_uppercase_and_lowercase():
    assert count_vowels("aEiOu") == 5

if __name__ == "__main__":
    pytest.main()