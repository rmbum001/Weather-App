from tkinter import messagebox
from tkinter import *
from configparser import ConfigParser
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celcius = temp_kelvin - 273.15
        temp_fareinheit = (temp_kelvin-273.15)*9/5 + 32
        icon = json['weather']['icon']
        weather = json['Weather'][0]['main']
        final = (city, country, temp_celcius, temp_fareinheit, icon, weather)
        return  final
    else:
        return None
    print(get_weather('London'))

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
       location_label['text']='{},{}'.format(weather[0], weather[1])
       image['bitmap'] ='weather_icons/{}.png'.format(weather[4])
       temp_label['text']='{:.2f}*C, {:.2f}*F'.format(weather[2], weather[3])
       weather_label['text']= weather[5]

    else:
        messagebox.showerror('Error','Cannot find city{}'.format(city))



app = Tk()
app.title("Weather app")
app.geometry('700x350')
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_button = Button(app, text='Search weather', width=12, command=search)
search_button.pack()
location_label = Label(app, text='', font=('bold', 20))
location_label.pack()

image = Label(app, bitmap='')
image.pack()

temp_label = Label(app, text='')
temp_label.pack()

weather_label = Label(app, text='')
weather_label.pack()

app.mainloop()
