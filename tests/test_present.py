from lib.present import Present
import pytest

# test wrap and then unwrap. Should return content
def test_wrap_and_unwrap_when_contents_is_none():
    present = Present()
    present.wrap('wine')
    result = present.unwrap()
    assert result == "wine"

# if we wrap already wrapped content we get an error message
def test_wrapping_already_wrapped_content():
    present = Present()
    present.wrap('wine')
    with pytest.raises(Exception) as e:
        present.wrap('wine')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

# if we unwrap before wrapping we get an error message
def test_unwrapping_unwrapped_content():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

# if we try to wrap an already-wrapped present the first-wrapped value is unchanged
def test_wrapping_already_wrapped_preserves_value():
    present = Present()
    present.wrap('wine')
    with pytest.raises(Exception) as e:
        present.wrap('toy')
    assert present.unwrap() == 'wine'