from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from pureBeurre.settings.settings import BASE_DIR


class TestIdentification(StaticLiveServerTestCase):
    
    def test_register(self):
        # Open the browser with webdrive
        self.service = Service(executable_path=(BASE_DIR + "/tests/tests_functional/chromedriver"))
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)
        self.driver.get(self.live_server_url + reverse("register"))

        id_username = self.driver.find_element(By.ID, "id_username")
        id_username.send_keys("user1")
        id_last_name = self.driver.find_element(By.ID, "id_last_name")
        id_last_name.send_keys("last_name_user1")
        id_email = self.driver.find_element(By.ID, "id_email")
        id_email.send_keys("user1@email.com")
        id_password1 = self.driver.find_element(By.ID, "id_password1")
        id_password1.send_keys("Password1!")
        id_password2 = self.driver.find_element(By.ID, "id_password2")
        id_password2.send_keys("Password1!")
        signup = self.driver.find_element(By.ID, "submit_register")
        signup.submit()

        self.assertEqual(self.driver.find_element(By.TAG_NAME, 'h2').text,
                         "Créer son espace utilisateur")
        self.assertEqual(self.driver.current_url, self.live_server_url +
                         reverse("register"))
        # close the browser
        time.sleep(3)
        self.driver.close()
