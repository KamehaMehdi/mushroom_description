from flask import Flask, render_template, request
from pickle import load
from numpy import array
from json import loads

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	pass

@app.route('/results')
def result():
	reg = load(open('./mushrooms.pkl', 'rb'))
	mushroom = loads(request.args.get('mushroom'))
	np_mushroom = array([mushroom])
	prediction = reg.predict(np_mushroom)
	return str(prediction[0] * 1)
	pass

if __name__ == '__main__':
	app.run(port=5000)
	pass
