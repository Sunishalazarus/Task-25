from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class IMDb:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Explicit wait
        self.wait = WebDriverWait(self.driver, 30)
        self.act = ActionChains(self.driver)

    def boot(self):
        """
        This method is to open up the chrome browser with the URL and makes the browser to go fullscreen.
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def quit(self):
        """
        This method is used to close the webbrowser
        """
        self.driver.quit()

    def fill_names(self):
        """"
        To fill data and do a search.
        """
        try:

            self.boot()

            for _ in range(9):
                self.act.send_keys(Keys.DOWN).perform()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Expand all')]"))).click()

            for _ in range(9):
                self.act.send_keys(Keys.DOWN).perform()

            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Name']"))).send_keys("Sunisha")
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Enter birth date from']"))).send_keys("19061995")
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Enter birthday']"))).send_keys("0619")

            for _ in range(9):
                self.act.send_keys(Keys.DOWN).perform()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='test-chip-id-oscar_best_actress_nominees']"))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='BIRTH_PLACE']"))).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='e.g. Arrested']"))).send_keys("Jamshedpur")


            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='adv-search-get-results']"))).click()
            print("Success: Filled successfully!")


        except Exception as e:
            print("Error", e)
        finally:
            self.quit()

obj= IMDb("https://www.imdb.com/search/name/")
obj.fill_names()

"""
Output- Success: Filled successfully!
"""