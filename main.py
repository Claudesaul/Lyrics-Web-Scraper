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
search.click()

search.send_keys(song + " " + artist + Keys.ENTER)


driver.find_element(By.CLASS_NAME, "mini_card-subtitle").click()

time.sleep(4)

lyrics = driver.find_elements(By.CSS_SELECTOR, ".Lyrics__Container-sc-1ynbvzw-5.Dzxov")

print(driver.title)

for i in lyrics:
    print(i.text)