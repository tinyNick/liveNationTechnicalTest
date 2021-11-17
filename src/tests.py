from math import *
from random import *


# Addition Tests
def test_adding_pass_int(x,y):
  assert addNumbers() == 5

def test_adding_pass_float(x,y):
  assert addNumbers() == 5

def test_adding_fail(x,y):
  assert addNumbers() == 5

def test_adding_fail_str(x,y):
  assert addNumbers() == 5


# Subtraction Tests
def test_subtract_pass_int(x,y):
  assert subtractNumbers() == 5

def test_subtract_pass_float(x,y):
  assert subtractNumbers() == 5

def test_subtract_fail(x,y):
  assert subtractNumbers() == 5

def test_subtract_fail_str(x,y):
  assert subtractNumbers() == 5


# Division Tests
def test_divide_pass_int(x,y):
  assert divideNumbers() == 3

def test_divide_pass_float(x,y):
  assert divideNumbers() == 3.0

def test_divide_fail_symbol_int(x,y):
  assert divideNumbers() == 6

def test_divide_fail_symbol_float(x,y):
  assert divideNumbers() == 6.0

def test_divide_fail_str(x,y):
  assert divideNumbers() == 3


# Random Tests
def test_random_pass_default():
  assert len(randomNumbers) == 10

def test_random_pass_count(x):
  assert len(randomNumbers()) == 5

def test_random_fail_count(x):
  assert len(randomNumbers()) == 5

def test_random_fail_count_str(x):
  assert len(randomNumbers()) == 5


if __name__ == "__main__":
    test_adding_pass_int(2,3)
    test_adding_pass_float(2,3.0)
    test_adding_fail(2,0)
    test_adding_fail_str(2,"0")
    test_subtract_pass_int(8,3)
    test_subtract_pass_float(8.2,3.2)
    test_subtract_fail(6,0)
    test_subtract_fail_str(5,"0")
    test_divide_pass_int(9,3)
    test_divide_pass_float(9.0,3.0)
    test_divide_fail_symbol_int(6,1)
    test_divide_fail_symbol_float(6.0,1.0)
    test_divide_fail_str(9,"3")
    test_random_pass_default()
    test_random_pass_count(5)
    test_random_fail_count(6)
    test_random_fail_count_str("5")
    print("Everything passed")
