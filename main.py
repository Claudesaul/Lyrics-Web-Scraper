from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time

# Path of Microsoft Edge driver
webdriver_path = "C:\\Users\\CSB\\Documents\\msedgedriver.exe"


# Create an instance of the Edge browser
edge_service = EdgeService(executable_path=webdriver_path)
driver = webdriver.Edge(service=edge_service)

# Get song and artist name
artist = input("What is the artist's name?")
song = input("What is the song name?")

# Go to site and search
driver.get('https://genius.com')


search = driver.find_element(By.NAME, 'q')

search.send_keys(song + " " + artist)

time.sleep(1)

search.send_keys(Keys.DOWN)
time.sleep(2)
search.send_keys(Keys.ENTER)

print(driver.title)

