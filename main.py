from flask import Flask,request,render_template
from flask import jsonify
from timing import mealrec
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-from.html')
#def hello():
  #  """Return a friendly HTTP greeting."""
   # print("hello")
    #return ("Hello and  Welcome! <br> If you need to check which meal time it is, check the meal path. ")

    
#@app.route('/meal/<name>')
@app.route('/',methods=['POST'])
def my_form_post():
    #print(f"This was placed in the url: new-{name}")
    #name=request.form['text']
    #hr=int(name[0])
    hr=int(request.form.get("hour"))
    period=request.form.get("period")
    #period=name[1:]
    result=mealrec(hr,period)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
