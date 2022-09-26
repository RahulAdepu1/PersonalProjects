# A new line added
import time

from selenium import webdriver
from selenium import Service
from selenium import Options
from selenium import By


driver_service = Service(executable_path='/Users/rahuladepu/Desktop/My Files/Software/chromedriver')

options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=driver_service, options=options)
driver.maximize_window()

# songName = "Mehrama"
# driver.get('https://www.google.com/search?q='+songName+' song lyrics')
# time.sleep(5)

driver.get('https://lyricsraag.com/mehrama')
links = driver.find_element(By.LINK_TEXT, "Title of Song:")
print(links)