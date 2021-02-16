import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

#URL from where we will fetch the details
url = "https://weather.com/en-IN/weather/today/l/c3e96d6cc4965fc54f88296b54449571c4107c73b9638c16aafc83575b4ddf2e"

master = Tk()
master.title("Weather App")
master.config(bg = 'white')

#giving image path and resizing
img = Image.open("C:/Users/msn21/PycharmProjects/WeatherApp/weather.png")
img = img.resize((100,100))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    location = soup.find('h1',class_="CurrentConditions--location--1Ayv3").text
    time = soup.find('div',class_="CurrentConditions--timestamp--1SWy5").text
    temperature = soup.find('span',class_="CurrentConditions--tempValue--3KcTQ").text
    weatherPred = soup.find('div',class_="CurrentConditions--phraseValue--2xXSr").text
    airquality = soup.find('text',class_="DonutChart--innerValue--k2Z7I").text
    #print(location,temperature,weatherPred,time)
    locationLabel.config(text=location)
    timeLabel.config(text=time)
    tempLabel.config(text=temperature)
    weatherPredLabel.config(text=weatherPred)
    airqualityLabel.config(text=airquality)

    timeLabel.after(60000, getWeather)
    tempLabel.after(60000,getWeather)   #every 1 min
    weatherPredLabel.after(60000, getWeather)
    airqltyLbl.after(300000,getWeather) #every 5 mins
    master.update()



#placing location label
locationLabel = Label(master,font=("Calibri bold",20),bg="white")
locationLabel.grid(row=0,sticky="N",padx=100)

#placing time label
timeLabel = Label(master,font=("Calibri",15),bg="white")
timeLabel.grid(row=1,sticky="N",padx=50)

#placing image
Label(master, image = img, bg="white").grid(row=2,sticky="E",padx=10)

#placing temperature label
tempLabel = Label(master,font=("Calibri bold",80),bg="white")
tempLabel.grid(row=2,sticky="W",padx=50)

#placing weather label
weather = Label(master,font=("Calibri bold",15),bg="white",text="Weather")
weather.grid(row=3,sticky="W",padx=50)
weatherPredLabel = Label(master,font=("Calibri bold",15),bg="white")
weatherPredLabel.grid(row=3,sticky="E",padx=50)

#placing air quality index label
airqltyLbl = Label(master,font=("Calibri bold",20),bg="white",text="Air Quality Index")
airqltyLbl.grid(row=4,sticky="W",padx=50)

airqualityLabel = Label(master,font=("Calibri bold",20),bg="white",text="Air Quality Index:")
airqualityLabel.grid(row=4,sticky="E",padx=50)

getWeather()
master.mainloop()