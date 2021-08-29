from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("hello")
    return ("Let's do some addition!")

@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"X": name,"Y":name}
    conti=val["X"]+val["Y"]
    return jsonify(conti)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
