from lib.string_builder import StringBuilder

# innitially the output is empty
def test_stringBuilder_string_is_empty():
    builder = StringBuilder()
    assert builder.output() == ""

# when adding multiple string the outout is those string concatenated.
def test_adding_multiple_strings_outputs_concatenated_string():
    builder = StringBuilder()
    builder.add("hello")
    builder.add(" world")
    assert builder.output() == "hello world"

# when adding multiple string the size is added.
def test_adding_multiple_strings_has_total_size():
    builder = StringBuilder()
    builder.add("hello")
    builder.add(" ")
    builder.add("world")
    assert builder.size() == 11