from flask import Flask, render_template, request # request object in flask helps you get form body
import requests #send http requests 
from datetime import datetime 	# to get timestamp

app = Flask(__name__)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
	zipcode = request.form['zip']
	user_apiid = '5cb00286a7cf3a8f11164ed76bcaf93e'
	#r = requests.get("http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&units=imperial&APPID='+user_apiid'")
	#r = requests.get("http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&units=imperial&APPID="+user_apiid)
	r = requests.get("http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&APPID="+user_apiid)
	json_object = r.json() #r.text()
	#temp_f = float(json_object['main']['temp'])
	temp_k = float(json_object['main']['temp'])
	temp_f = (temp_k - 273.15) * 1.8 + 32
	test_success = ' test success'
	pressure_imperial = float(json_object['main']['pressure']) 	#"pressure":1018,
	humidity_imperial = float(json_object['main']['humidity'])	#"humidity":88,
	temp_min_imperial = float(json_object['main']['temp_min'])	#"temp_min":292.15
	temp_max_imperial = float(json_object['main']['temp_max'])	#"temp_max":294.15 
	# can put the above in an array/list and call the list. see flask tut when he calls links . i think its part1
	city_coord = (json_object['coord'])#do we need to split out lat and lon. will remove this
	city_coord_lat = (json_object['coord']['lat'])
	city_coord_lon = (json_object['coord']['lon'])
	#city_weather = (json_object['weather'][1]) #gives weather child with value in this current case ['mist']
	#city_clouds = (json_object['name'])
	city_dt = (json_object['dt']) #convert time
	#city_dt = (json_object['dt']).strftime("%B %d, %Y") #my_datetime.strftime("%B %d, %Y")
	city_name = (json_object['name'])
	city_country = (json_object['sys']['country'])
	city_sunrise = (json_object['sys']['sunrise'])#convert time
	city_sunset = (json_object['sys']['sunset'])#convert time
	return render_template('temperature.html',  temp=temp_f, zipc = zipcode, tester=test_success, city = city_name, pressure = pressure_imperial, humidity=humidity_imperial, temp_min = temp_min_imperial, temp_max = temp_max_imperial , city_coord=city_coord , country=city_country, city_sunrise =city_sunrise , city_sunset=city_sunset, city_lat=city_coord_lat, city_lon=city_coord_lon, time = city_dt)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

'''
{
"coord":{"lon":-80.12,"lat":26.72},
"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50d"}],
"base":"stations",
"main":{"temp":293.14,"pressure":1018,"humidity":88,"temp_min":292.15,"temp_max":294.15},
"visibility":16093,
"wind":{"speed":3.6,"deg":330},
"clouds":{"all":75},
"dt":1478346780,
"sys":{"type":1,"id":734,"message":0.1918,"country":"US","sunrise":1478345606,"sunset":1478385265},
"id":4172248,
"name":"Schall Circle",
"cod":200
}
'''
