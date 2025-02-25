from selenium import webdriver

"""
https://admin-demo.nopcommerce.com/login

admin@yourstore.com

admin

Dashboard / nopCommerce administration is the title

"""



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:

    rul = "http://localhost:4444/wd/hub"
    driver = webdriver.Remote(command_executor=rul,options=webdriver.ChromeOptions())


    driver.get("https://admin-demo.nopcommerce.com/login")


    driver.find_element(by=By.NAME,value="Email").clear()
    driver.find_element(by=By.NAME,value="Email").send_keys("admin@yourstore.com")

    driver.find_element(by=By.ID,value="Password").clear()
    driver.find_element(by=By.ID,value="Password").send_keys("admin")

    driver.find_element(by=By.CSS_SELECTOR,value="button").click()


    actual_title = driver.title

    expected_title = "Dashboard / nopCommerce administration"

    if actual_title == expected_title:
        print("Login test passed")
    else:
        print("Login test failed")

    driver.close()
except:
    print("could not start the browser")