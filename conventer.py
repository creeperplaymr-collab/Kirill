import requests
from bs4 import BeautifulSoup
response= requests.get("https://p2p.army/en/rates/banks/KZ/Halyk")
soup= BeautifulSoup(response.text, "html.parser")
cny_rate= None
rows= soup.find_all("ts")

for row in rows:
    text= row.get_text(" ", strip= True)
    if text.startswith("CNY"):
        parts= text.split()
        cny_rate= float(parts[1])
        break
class Converter:
    def __init__(self, cny_rate):
        self.cny_rate= cny_rate
    def kzt_to_cny(self, kzt):
        return kzt/self.cny_rate
convert= Converter(cny_rate)
print(f"CNY today is:{cny_rate} KZT")
tenge= float(input("Enter the value of tenge: "))
yan= convert.kzt_to_cny(tenge)
print(f"It's approximately {yan:2f} CNY")