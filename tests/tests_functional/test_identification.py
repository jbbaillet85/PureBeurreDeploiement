from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from django.urls import reverse
import time


class TestIdentification(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    def test_register(self):
        # Open the browser with webdrive
        path_register = reverse('register')
        self.selenium.get('%s%s' % (self.live_server_url, path_register))

        id_username = self.selenium.find_element(By.ID, "id_username")
        id_username.send_keys("user1")
        id_last_name = self.selenium.find_element(By.ID, "id_last_name")
        id_last_name.send_keys("last_name_user1")
        id_email = self.selenium.find_element(By.ID, "id_email")
        id_email.send_keys("user1@email.com")
        id_password1 = self.selenium.find_element(By.ID, "id_password1")
        id_password1.send_keys("Password1!")
        id_password2 = self.selenium.find_element(By.ID, "id_password2")
        id_password2.send_keys("Password1!")
        signup = self.selenium.find_element(By.ID, "submit_register")
        signup.submit()

        self.assertEqual(self.selenium.find_element(By.TAG_NAME, 'h2').text,
                         "Créer son espace utilisateur")
        self.assertEqual(self.selenium.current_url, self.live_server_url +
                         reverse("register"))
        # close the browser
        time.sleep(3)
        self.selenium.close()
