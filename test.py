import wikipediaapi

import wikipedia

import requests as req

import re
	
# from nltk import sent_tokenize
from bs4 import BeautifulSoup

list_of_cities = ["Montreal", "Vancouver", "Edmonton"]
# list_of_cities = ["Montreal"]


for city in list_of_cities:
	pg = wikipedia.page(city)
	content = pg.content.replace("=", "")
	m = re.findall('[^.]+', content)
	
