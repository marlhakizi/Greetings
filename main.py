from flask import Flask,request
from flask import jsonify
from timing import mealrec
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("hello")
    return ("Hello and  Welcome! <br> If you need to check which meal time it is, check the meal path. ")


@app.route('/meal/<name>')
def meal(name):
    print(f"This was placed in the url: new-{name}")
    hr=int(name[0])
    period=name[1:]
    result=mealrec(hr,period)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)