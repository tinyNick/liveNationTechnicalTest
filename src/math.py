from prometheus_client import Histogram
import time

graphs = {}
graphs['ahist'] = Histogram("add_request_duration_in_seconds", "Histogram of the add request duration in seconds.", buckets=(1))
graphs['shist'] = Histogram("subtract_request_duration_in_seconds", "Histogram of the subtract request duration in seconds.", buckets=(2))
graphs['dhist'] = Histogram("divide_request_duration_in_seconds", "Histogram of the divide request duration in seconds.", buckets=(1))

def addNumbers(x,y,astart):
  try:
    isinstance(x, (int, float))
  except Exception as err:
    print(f"First value entered, {x}, is not a number.\n {err}\n")
  try:
    isinstance(y, (int, float))
  except Exception as err:
    print(f"Second value entered, {y}, is not a number.\n {err}\n")
  sum = x+y
  aend = time.time()
  graphs['ahist'].observe(aend - astart)
  return print(f"The sum of {x} and {y} is: ", sum)

def subtractNumbers(x,y,sstart):
  try:
    isinstance(x, (int, float))
  except Exception as err:
    print(f"First value entered, {x}, is not a number.\n {err}\n")
  try:
    isinstance(y, (int, float))
  except Exception as err:
    print(f"Second value entered, {y}, is not a number.\n {err}\n")
  result = x-y
  send = time.time()
  graphs['shist'].observe(send - sstart)
  return print(f"The result of {x} - {y} is: ", result)

def divideNumbers(x,y,dstart):
  try:
    isinstance(x, (int, float))
  except Exception as err:
    print(f"First value entered, {x}, is not a number.\n {err}\n")
  try:
    isinstance(y, (int, float))
  except Exception as err:
    print(f"Second value entered, {y}, is not a number.\n {err}\n")

  if type(x) == int:
    if type(y) == int:
      result = x//y
    else:
      newY = round(y)
      result = x//newY
  elif type(y) == float:
      result = x/y
  else:
      float(y)
      result = x/y
  dend = time.time()
  graphs['dhist'].observe(dend - dstart)
  return print(f"The result of {x} / {y} is: ", result)
