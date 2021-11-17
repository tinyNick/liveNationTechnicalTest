from random import *
from prometheus_client import Histogram
import time

graphs = {}
graphs['rhist'] = Histogram("random_request_duration_in_seconds", "Histogram of the random request duration in seconds.", buckets=(2))

def randomNumbers(rstart,count=10):
  array = []
  while count > 1:
    array.append(randint())
    count -= 1
  
  numberList = sample(array, 10)
  rend = time.time()
  graphs['rhist'].observe(rend - rstart)
  return print(numberList)
