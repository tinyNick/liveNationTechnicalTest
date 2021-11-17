from flask import Response

def health():
  return Response("{'a':'b'}", status=200, mimetype='application/json')

def alive():
  return Response("{'a':'b'}", status=200, mimetype='application/json')
