# Import
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# url = "https://lyricsraag.com/kiston"
url = "https://www.lyricsgoal.com/kiston"

page = requests.get(url)
soup = bs(page.text, features="html.parser")
table = soup.find('table')
print(table)
