from numbers.math import *
from numbers.random import randomNumbers
from misc.health import health, alive


# Addition Tests
def test_adding_pass_int():
  assert math.addNumbers(2 + 3) == 5

def test_adding_pass_float():
  assert math.addNumbers(2 + 3.0) == 5

def test_adding_fail():
  assert math.addNumbers(2 + 0) == 5

def test_adding_fail_str():
  assert math.addNumbers(2 + "0") == 5


# Subtraction Tests
def test_subtract_pass_int():
  assert math.subtractNumbers(8 - 3) == 5

def test_subtract_pass_float():
  assert math.subtractNumbers(8.2 - 3.2) == 5

def test_subtract_fail():
  assert math.subtractNumbers(6 - 0) == 5

def test_subtract_fail_str():
  assert math.subtractNumbers(5 - "0") == 5


# Division Tests
def test_divide_pass_int():
  assert math.divideNumbers(9 // 3) == 3

def test_divide_pass_float():
  assert math.divideNumbers(9.0 / 3.0) == 3.0

def test_divide_fail_symbol_int():
  assert math.divideNumbers(6 / 1) == 6

def test_divide_fail_symbol_float():
  assert math.divideNumbers(6.0 // 1.0) == 6.0

def test_divide_fail_str():
  assert math.divideNumbers(9 // "3") == 3


# Random Tests
def test_random_pass_default():
  assert len(math.randomNumbers) == 10

def test_random_pass_count():
  assert len(math.randomNumbers(5)) == 5

def test_random_fail_count():
  assert len(math.randomNumbers(6)) == 5

def test_random_fail_count_str():
  assert len(math.randomNumbers("5")) == 5
