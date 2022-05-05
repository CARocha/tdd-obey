from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

browser = driver
browser.get("http://localhost:8000")

assert "The install worked successfully! Congratulations!" in browser.title
