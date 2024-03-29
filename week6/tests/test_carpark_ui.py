import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

#
# The setup_function(function) only runs if "pytest" entered into the terminal
# This is required for all tests as it removes any cars from previous tests
# In addition, main.py is required to be running for the tests to work as expected
#

def setup_function(function):
    if os.path.exists("week6/data/vehicles.json"):
        os.remove("week6/data/vehicles.json")


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_adding_item(driver):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.ID, "txtreg").send_keys("test")
    driver.find_element(By.ID, "btnadd").click()

    assert driver.find_element(By.ID, "result").text == "Car added successfully"
    assert driver.find_element(By.ID, "spacecount").text == "14"
    assert driver.find_elements(By.CSS_SELECTOR, "#spaces li")[-1].text == "test"
