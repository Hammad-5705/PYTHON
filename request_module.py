import requests
from bs4 import BeautifulSoup

url="https://stackoverflow.com/questions/1614059/how-to-make-python-speak"

r=requests.get(url)

soup=(BeautifulSoup(r.text,"html.parser"))
# print(soup.prettify())

for h in soup.find_all("ol"):
    print(h)
# print(r.text)