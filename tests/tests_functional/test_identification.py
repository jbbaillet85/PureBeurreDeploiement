from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from django.urls import reverse
import time


class TestIdentification(StaticLiveServerTestCase):
    
    def test_register(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # path_register = reverse('register')
        path_register="/spaceUser/register/"
        driver.get(path_register)
        # Open the browser with webdrive
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
        time.sleep(300)
        driver.close()

if __name__=="__main__":
    test=TestIdentification()
    test.test_register()