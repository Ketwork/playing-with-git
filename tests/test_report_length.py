from lib.report_length import *

def test_report_length_returns_string_with_length():
    result = report_length('hello')
    assert result == "This string was 5 characters long."