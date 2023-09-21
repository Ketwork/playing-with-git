from lib.password_checker import PasswordChecker
import pytest

# if password is above 8+ characters returns True
def test_above_7_characters():
    password_checker = PasswordChecker()
    result = password_checker.check("12345678")
    assert result == True

# if password is less then 8 char return error message
def test_below_8_charaters():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
    