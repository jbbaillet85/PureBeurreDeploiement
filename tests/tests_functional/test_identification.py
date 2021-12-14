import os
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from django.urls import reverse
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
class TestIdentification(StaticLiveServerTestCase):
    
    def test_register(self):
        # Open the browser with webdrive
        path_register = reverse('register')
        driver.get('%s%s' % (self.live_server_url, path_register))

        id_username = driver.find_element(By.ID, "id_username")
        id_username.send_keys("user1")
        id_last_name = driver.find_element(By.ID, "id_last_name")
        id_last_name.send_keys("last_name_user1")
        id_email = driver.find_element(By.ID, "id_email")
        id_email.send_keys("user1@email.com")
        id_password1 = driver.find_element(By.ID, "id_password1")
        id_password1.send_keys("Password1!")
        id_password2 = driver.find_element(By.ID, "id_password2")
        id_password2.send_keys("Password1!")
        signup = driver.find_element(By.ID, "submit_register")
        signup.submit()

        self.assertEqual(driver.find_element(By.TAG_NAME, 'h2').text,
                         "Créer son espace utilisateur")
        self.assertEqual(driver.current_url, self.live_server_url +
                         reverse("register"))
        # close the browser
        time.sleep(3)
        driver.close()
