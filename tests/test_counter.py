from lib.counter import Counter

def test_counts_single_number_added():
  counter = Counter()
  counter.add(5)
  result = counter.report()
  assert result == "Counted to 5 so far."

def test_counts_multiple_numbers_added():
  counter = Counter()
  counter.add(5)
  counter.add(3)
  result = counter.report()
  assert result == "Counted to 8 so far."

def test_counter_initially_reports_zero():
  counter = Counter()
  assert counter.report() == "Counted to 0 so far."