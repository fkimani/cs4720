from flask import Flask, render_template, request # request object in flask helps you get form body
import requests #send http requests 
from datetime import datetime 	# to get timestamp
import datetime

app = Flask(__name__)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
	#this function checks for valid zip inputs. If input is not numeric, its invalid and results wont render
	def validatezip():	
		error = None
		if request.method == 'POST':
			if (request.form['zip']).isdigit():
				return request.form['zip']
		else:
			error = 'invalid entry. Need numeric.'
	zipcode = validatezip()
	#zipcode = request.form['zip']
	user_apiid = '5cb00286a7cf3a8f11164ed76bcaf93e' #replace with your user_apiid. For the purposes of this project, lets use my user_apiid
	url = "http://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&APPID={}".format(zipcode,user_apiid)
	r = requests.get(url)
	json_object = r.json() #r.text()
	temp_f = float(json_object['main']['temp']) #imperial
	#temp_k = float(json_object['main']['temp'])
	#temp_f = (temp_k - 273.15) * 1.8 + 32
	test_success = ' test success'
	pressure_imperial = float(json_object['main']['pressure']) 
	humidity_imperial = float(json_object['main']['humidity'])
	temp_min_imperial = float(json_object['main']['temp_min'])	
	temp_max_imperial = float(json_object['main']['temp_max'])	
	city_coord_lat = (json_object['coord']['lat'])
	city_coord_lon = (json_object['coord']['lon'])
	#city_weather = (json_object['weather'][1]) #gives weather child with value in this current case ['mist']
	#city_clouds = (json_object['name'])
	city_dt = (json_object['dt']) #convert time
	city_name = (json_object['name'])
	city_country = (json_object['sys']['country'])
	city_sunrise_dt = (json_object['sys']['sunrise'])#convert time
	city_sunset_dt = (json_object['sys']['sunset'])#convert time

	#convert times from raw dt to date string format for times
	def dt_to_strtime(dt):
		return datetime.datetime.fromtimestamp(int(dt)).strftime('%H:%M') #format that has the time
	local_time = dt_to_strtime(city_dt)
	city_sunrise = dt_to_strtime(city_sunrise_dt)
	city_sunset	= dt_to_strtime(city_sunset_dt)
	#wind_degree = json_object['wind']['deg']
	wind_degree = float(json_object['wind']['deg'])
	#convert wind degrees to compass direction
	def degToCompass(num):
		val=int((num/22.5)+.5)
		arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
		return arr[(val % 16)]
	#call function we defined to convert degrees to compass directions
	wind_deg_to_dir = degToCompass(json_object['wind']['deg'])

	#You'll get the icon code from the object that your JSON call returns,
	icon_code = json_object['weather'][0]['icon']
	icon_description = json_object['weather'][0]['main']
	#and then use that to construct a url which points to the current weather icon
	icon_url = "http://openweathermap.org/img/w/{}.png".format(icon_code)
	#and then write that on the html <img> tag as seen on the temperature page

	return render_template('temperature.html',  temp=temp_f, zipc = zipcode, tester=test_success, city = city_name, pressure = pressure_imperial, humidity=humidity_imperial, temp_min = temp_min_imperial, temp_max = temp_max_imperial , country=city_country, city_sunrise =city_sunrise, city_sunset=city_sunset, city_lat=city_coord_lat, city_lon=city_coord_lon, time = local_time, icon_url = icon_url, icon_desc = icon_description, wind_dir = wind_deg_to_dir)


#this is the index page route and is the root hence the '/'
@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)

#sample weather data format we expect in results on /temperature.html for zip code 30144 (Kennesaw). This was taken at 12/7/16 23:41 hrs
'''
{
"coord":{"lon":-84.62,"lat":34.02},
"weather":[{"id":300,"main":"Drizzle","description":"light intensity drizzle","icon":"09n"}],
"base":"stations",
"main":{"temp":52.27,"pressure":1015,"humidity":87,"temp_min":50,"temp_max":53.6},
"visibility":16093,
"wind":{"speed":4.7,"deg":270},
"clouds":{"all":90},
"dt":1481085660,
"sys":{"type":1,"id":748,"message":0.1839,"country":"US","sunrise":1481113880,"sunset":1481149752},
"id":4203696,
"name":"Kennesaw",
"cod":200}
'''
