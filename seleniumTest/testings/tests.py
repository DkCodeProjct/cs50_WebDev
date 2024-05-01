from django.test import TestCase

# Create your tests here.
import os
import pathlib
import unittest

from selenium import webdriver

# Finds the Uniform Resourse Identifier of a file
def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

# Sets up web driver using Google chrome
driver = webdriver.Chrome()

# Create your tests here.
from selenium.webdriver.common.by import By

class TestWebSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def testIncrease(self):
        self.driver.get(file_uri("index.html"))
        increase = self.driver.find_element(By.ID, "increase")
        increase.click()
        h1_element = self.driver.find_element(By.TAG_NAME, "h1")
        h1_text = int(h1_element.text)
        self.assertEqual(h1_text, 1)
    
    def testDecrease(self):
        self.driver.get(file_uri("index.html"))
        decrease = self.driver.find_element(By.ID, "decrease")
        decrease.click()
        h1 = self.driver.find_element(By.TAG_NAME, "h1")
        h1Txt = int(h1.text)
        self.assertEqual(h1Txt, -1)
    
    def testMulIncrease(self):
        self.driver.get(file_uri("index.html"))  # Corrected typo: "index.html" instead of "index.hmtl"
        increase = self.driver.find_element(By.ID, "increase")
        for i in range(3):
            increase.click()
        h1 = self.driver.find_element(By.TAG_NAME, "h1")
        h1Txt = int(h1.text)
        self.assertEqual(h1Txt, 3)


if __name__ == "__main__":
    unittest.main()
