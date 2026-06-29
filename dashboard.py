import requests
import json
from bs4 import BeautifulSoup

city=input("Enter your city")

# Weather
response = requests.get("https://wttr.in/" + city + "?format=j1")
data=response.json()

temp=data["current_condition"][0]["temp_C"]
feels=data["current_condition"][0]["FeelsLikeC"]
desc=data["current_condition"][0]["weatherDesc"][0]["value"]

#quote
scrape=requests.get("https://quotes.toscrape.com")
soup=BeautifulSoup(scrape.text, "html.parser")
quotes=soup.find_all("span",class_="text")
authors = soup.find_all("small", class_="author")

import random
i=random.randint(0,len(quotes)-1)
quote=quotes[i].text
author=authors[i].text

#save to json

dashboard={
"city":city,
"temperature":temp,
"feels_like":feels,
"condition": desc,
"quote": quote,
"author": author
}
f=open("dashboard.json","w")
json.dump(dashboard,f)
f.close()

#print dashboard

print("="*30)
print("Your Daily Dashboard")
print("="*30)
print("city:",city)
print("temperature:",temp,"°C")
print("Feels like:", feels, "°C")
print("Condition:", desc)
print("-"*30)
print("Quote:", quote)
print("Author:", author)
print("="*30)
print("Saved to dashboard.json")
