# -*- coding: utf-8 -*-
"""
https://the-internet.herokuapp.com/login
web creada para automatizacion
sin captcha
estable selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import subprocess, sys

subprocess.run([sys.executable, "-m", "pip", "install", "selenium", "webdriver-manager"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!"+Keys.RETURN)
driver.quit()
