from bs4 import BeautifulSoup
import requests

url = "https://ru.wikipedia.org/wiki/Python"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
print(text)
