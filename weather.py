
import requests

city = input("Enter the City name : ")
print(city)

print("Displaying weathe report for : "+city)

url="https://wttr.in/{}".format(city)
res = requests.get(url)
print(res.text)



import requests
res = requests.get('https://ipinfo.io/')
data = res.json()
citydata = data['city']
print(citydata)
url = 'https://wttr.in/{}'.format(citydata)
res = requests.get(url)
print(res.text)



import requests
from bs4 import BeautifulSoup
city=input("Enter the city")
url="https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div',attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
data = str.split("\n")
time = data[0]
sky = data [1]

listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
 
# particular list with required data
strd = listdiv[5].text
 
# formatting the string
pos = strd.find('Wind')
other_data = strd[pos:]
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)
