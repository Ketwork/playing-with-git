from lib.check_codeword import *

# test if codeword is correct
def test_with_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

# test if codeword is wrong
def test_with_wrong_codeword():
    result = check_codeword("hors")
    assert result == "WRONG!"

# test if codeword is wrong but close
def test_with_close_codeword():
    result = check_codeword("hose")
    assert result == "Close, but nope."

# test if first letter is right and last letter is wrong
def test_with_right_first_letter_wrong_last_letter():
    result = check_codeword("hord")
    assert result == "WRONG!"

# test if first letter is wrong and last letter is right
def test_with_right_first_letter_wrong_last_letter():
    result = check_codeword("morde")
    assert result == "WRONG!"