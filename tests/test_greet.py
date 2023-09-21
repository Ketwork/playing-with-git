from lib.greet import *

def test_greet_returns_hello_username():
  result = greet("Dave")
  assert result == "Hello, Dave!"