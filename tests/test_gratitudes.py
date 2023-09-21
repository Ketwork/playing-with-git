from lib.gratitudes import Gratitudes

# test default text if nothing input
def test_default_text_if_no_input():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "

# test if correct string is output with an input gratitude
def test_if_one_input_outputs_correct_string():
    gratitude = Gratitudes()
    gratitude.add("time")
    assert gratitude.format() == "Be grateful for: time"

# test if correct string is output for multiple inputs
def test_if_multiple_inputs_outputs_correct_string():
    gratitude = Gratitudes()
    gratitude.add("time")
    gratitude.add("friends")
    assert gratitude.format() == "Be grateful for: time, friends"