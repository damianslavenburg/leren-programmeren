from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SurveyBot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

        # Set up the Selenium web driver
        options = Options()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

        # Navigate to the Opinieland login page
        self.driver.get("https://www.opinieland.nl/login")

        # Enter your Opinieland login credentials
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        email_input.send_keys("99072038@mydavinci.nl")
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        password_input.send_keys("T3st4321")
        password_input.send_keys(Keys.ENTER)

        # Wait for the login to complete and navigate to the survey page
        time.sleep(5)  # Wait for the login to complete
        self.driver.get("https://www.opinieland.nl/auth/surveys#/Beginnen")

    def initUI(self):
        self.setWindowTitle("Survey Bot")

        self.status_label = QLabel(self)
        self.status_label.setGeometry(20, 20, 200, 20)
        self.status_label.setText("Ready")

        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(20, 50, 80, 30)
        self.start_button.clicked.connect(self.start_bot)

        self.quit_button = QPushButton("Quit", self)
        self.quit_button.setGeometry(120, 50, 80, 30)
        self.quit_button.clicked.connect(self.quit_bot)

        self.setGeometry(100, 100, 220, 100)
        self.show()

    def start_bot(self):
        self.status_label.setText("Running")

        # Loop through all available surveys and answer them
        while True:
            # Get the HTML source of the survey page
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, "html.parser")

            # Find all survey links on the page
            survey_links = soup.find_all("a", class_="poll-link")
            if not survey_links:
                # No more surveys available, exit the loop
                break

            # Loop through all survey links and answer them
            for survey_link in survey_links:
                survey_url = survey_link["href"]
                self.driver.get(survey_url)

                # Find all question checkboxes on the survey page and select them
                checkboxes = self.driver.find_elements_by_xpath("//input[@type='checkbox']")
                for checkbox in checkboxes:
                    checkbox.click()

                # Submit the survey
                submit_button = self.driver.find_element_by_xpath("//input[@type='submit']")
                submit_button.click()

                # Wait for the submission to complete
                time.sleep(3)

        self.status_label.setText("Done")

    def quit_bot(self):
        # Close the web driver
        self.driver.quit()

        QApplication.quit()


if __name__ == "__main__":
    app = QApplication([])
    survey_bot = SurveyBot()
    app.exec_()