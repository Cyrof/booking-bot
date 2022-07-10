import requests
from bs4 import BeautifulSoup


url = "https://www.cdc.com.sg/"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html')
print(soup.prettify())