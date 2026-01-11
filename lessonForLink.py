#example

from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.timeanddate.com/weather/")

if response.status_code == 200:
    rows= soup.find_all("tr")

soup= BeautifulSoup(response.content, features="html.parser")

for row in rows:
    city= row.find("a")
    temp= row.find("td", class_="rbi")

if city and temp:
    if city.text == "Dubai":
        print("Temperature in Dubai:")
        print(temp.text)
        break
