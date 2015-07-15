from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
  return "Hello!\n"

@app.route("/index")
def index():
  return render_template('index.html')

@app.route("/foo")
def foo():
  return "foo\n"

@app.route('/baz')
def baz():
  return request.args.get('name')

@app.route("/<bar>")
def bar(bar):
  return "{}".format(bar)

if __name__ == "__main__":
  app.run(debug=True)
