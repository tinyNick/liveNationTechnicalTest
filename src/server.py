from math import *
from random import *
from health import *
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Counter
import time

app = Flask(__name__)

graphs = {}
graphs['tcount'] = Counter("total_requests", "Total number of requests processed.")
graphs['acount'] = Counter("add_requests", "Total number of add requests processed.")
graphs['scount'] = Counter("subtraction_requests", "Total number of subtraction requests processed.")
graphs['dcount'] = Counter("division_requests", "Total number of diviision requests processed.")
graphs['rcount'] = Counter("random_requests", "Total number of random requests processed.")


@app.route("/add/{x}/{y}")
def add(x,y):
  astart = time.time()
  graphs['acount'].inc()
  return math.addNumbers(x,y,astart)

@app.route("/subtract/{x}/{y}")
def subtract(x,y):
  sstart = time.time()
  graphs['scount'].inc()
  return math.subtractNumbers(x,y,sstart)

@app.route("/division/{x}/{y}")
def divide(x,y):
  dstart = time.time()
  graphs['dcount'].inc()
  return math.divideNumbers(x,y,dstart)

@app.route("/random/{count}")
def random(count):
  rstart = time.time()
  graphs['rcount'].inc()
  return random.randomNumbers(rstart,count)

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
  '/metrics': make_wsgi_app()
})

@app.route("/readiness")
def readiness():
  return health.health()

@app.route("/liveness")
def liveness():
  return health.alive()
