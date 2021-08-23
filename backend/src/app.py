from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/max")
def max():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == "__main__":
  app.run()