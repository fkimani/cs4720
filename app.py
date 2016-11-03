from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
	#zipcode = request.from['zip']
	zip = requests.get("http://localhost:5000/")
	user_apiid = '5cb00286a7cf3a8f11164ed76bcaf93e'
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&APPID='+user_apiid +'")
	json_object = r.json()
	temp_k = float(json_object['main']['temp'])
	temp_f = (temp_k - 273.15) * 1.8 +3.2
	return render_template('temperature.html', temp=temp_f)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
