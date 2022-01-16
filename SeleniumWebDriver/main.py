
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start the driver
with webdriver.Chrome() as driver:
    # Open URL
    # get geeksforgeeks.org
    driver.get("https://www.geeksforgeeks.org/")
    
    # get element 
    elements = driver.find_elements(By.TAG_NAME, "a")
    for elem in elements:
    # get_attribute() to get all href
        e = elem.get_attribute("href")

    a = [x for x in elements if x.text == "Web Development"]
    #a = list(filter(lambda x: "Web Development" == x.text, elements))
    print(a[0])




