#import flask, urllib
import flask
from flask import Flask, render_template, request, jsonify, url_for
import requests, datetime, time
from datetime import datetime


# import json to load JSON data to a python dictionary 
import json

# urllib.request to make a request to api
#import urllib.request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
    else:
        #for default name mathura
       city = 'Toronto'

    source = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53')
    #return 'Hello, Flask!'
    list_of_data = source.json()#json.loads(source)
    print(list_of_data)
    timestamp = list_of_data['dt']
    print(timestamp)
    weatherdesc = str(list_of_data['weather'][0]['description'])
    image = ""
    if weatherdesc == "few clouds":
        image = 'Few-Clouds.jpeg'

    data = {
        "country_code": str(list_of_data['name']+ ', ' + list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "date": datetime.fromtimestamp(timestamp),
        "temp": str(round(list_of_data['main']['temp'] - 273.15, 0)),
        "feelslike": str(round(list_of_data['main']['feels_like'] - 273.15)),
        "image": image,
        "weatherdesc": weatherdesc,
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    print(data)
   # return jsonify({'data': data})
    return render_template('index.html',data=data)

@app.route('/hourly', methods=['GET', 'POST'])
def hourlyweather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        #for default name mathura
       city = 'mathura'

    source = requests.get('http://api.openweathermap.org/data/2.5/forecast/hourly?q=' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53')
    #return 'Hello, Flask!'
    list_of_data = source.json()#json.loads(source)
    print(list_of_data)
   # timestamp = list_of_data['dt']
   # print(timestamp)
    data = {
        "country_code": str(list_of_data['name']+ ', ' + list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        "date": datetime.fromtimestamp(timestamp),
        "temp": str(round(list_of_data['main']['temp'] - 273.15, 0)),
        "feelslike": str(round(list_of_data['main']['feels_like'] - 273.15)),
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
   # print(data)
    return jsonify({'data': data})
    return render_template('index.html',data=data)
#
if __name__ == '__main__':
    app.run(debug=True)