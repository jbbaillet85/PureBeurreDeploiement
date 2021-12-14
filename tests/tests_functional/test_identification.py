from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from django.urls import reverse
import time
from pureBeurre.settings.travis import BASE_DIR


class TestIdentification(StaticLiveServerTestCase):
    options = Options()
    options.binary_location = "C:\\path\\to\\chrome.exe"    #chrome binary location specified here
    options.add_argument("--start-maximized") #open Browser in maximized mode
    options.add_argument("--no-sandbox") #bypass OS security model
    options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, executable_path= BASE_DIR + 'tests/tests_functional/chromedriver')
    
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
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))

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
        self.driver.close()
