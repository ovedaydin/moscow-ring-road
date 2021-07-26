import os
from dotenv import load_dotenv

from flask import Blueprint, render_template, request
import requests
import xml.etree.ElementTree as ET
from .utils import *
import logging

# loading .env file
load_dotenv()

# Setting blueprint static and template files
geo = Blueprint("geo", __name__, static_folder="static",template_folder="template")

# api's url
URL = "https://geocode-maps.yandex.ru/1.x/?apikey="

# getting api key from .env file
API_KEY = os.environ.get("API_KEY")

#Creating a logger to keep logs
mylogger = logging.getLogger('mylogger')
#Creating a handler to keep logs in geo.log file
handler = logging.FileHandler('geo.log')
# Creating a format with date time and message
formatter = logging.Formatter('%(asctime)s -  %(message)s')
# Adding the format to the handler
handler.setFormatter(formatter)

#Adding the handler to the logger
mylogger.addHandler(handler)
#Changing log time to INFO so that we can save it otherwise only WARNINGs are saved
mylogger.setLevel(logging.INFO)

#Creating routes so that it'll work with both / and /home and able to work with POST and Get
#It is function based view which is common for Flask and suitable for a simple project
@geo.route("/home")
@geo.route('/',methods = ['POST', 'GET'])
def home():
    #This will be shown for the first time
    show = "Type a place"
    #When we get POST request / form submitted
    if request.method == 'POST':
        #We get the form from request
        result = request.form
        #We get the place from form
        place = result['place']
        #Preparing the url_link for the get request we'll make to the Yandex API
        url_link = URL + API_KEY + "&geocode=" + place
        #Get request done
        r = requests.get(url_link)
        #if get request successful and place is not blank
        if r.status_code == 200 and not place == "":
            #We're using try just in case if we get anything nonsense from the API
            #We do not want it to crush
            try:
                #Parsing
                root = ET.fromstring(r.text)
                #Lower point
                low = root[0][1][0][3][0][0]
                #Upper point
                up = root[0][1][0][3][0][1]
                #actual point
                point = root[0][1][0][4][0]
                #We can use lower and upper to make a more accurate calculation but it is not neccesary at this point
                #data[low.tag] = [float(i) for i in low.text.split()]
                #data[up.tag] = [float(i) for i in up.text.split()]

                #Splitting up the points to two pieces
                point = [float(i) for i in point.text.split()]

                #Putting the point to the calculator function in utils.py file
                show = distance(point)
            except:
                #If we get any errors while parsing, we'll show "There is a problem, try again"
                show = "There is a problem, try again"

        else:
            #If the request was not succesful or the place is blank we'll show "Invalid Place Name, try again"
            show = "Invalid Place Name, try again"
        #Whatever happens we are saving them as logs
        mylogger.info('Place: {}, Result: {}'.format(place, show))
    #returning the html and the data to show
    return render_template("home.html", data=show)
