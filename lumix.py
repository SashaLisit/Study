from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GoogleDriveAutomation:
    def __init__(self):
        # Step 1: Set up the Selenium driver (you need to download the appropriate driver for your browser)
        self.driver = webdriver.Chrome()

    def login_to_google_drive(self, email, password):
        # Step 2: Open Google Drive and navigate to the login page
        self.driver.get("https://drive.google.com/drive/my-drive")

        # Step 3: Find and fill in the email field
        email_field = self.driver.find_element(By.NAME, 'identifier')
        email_field.send_keys(email)

        # Press Enter or Return key to proceed
        email_field.send_keys(Keys.RETURN)

        # Wait for 2 seconds (adjust this time as needed)
        time.sleep(30)

        # Step 4: Find and fill in the password field
        password_field = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.NAME, 'Passwd')))
        password_field.send_keys(password)
        # Press Enter or Return key to log in
        password_field.send_keys(Keys.RETURN)

    def get_file_list(self):
        # Step 5: Retrieve a list of file elements
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="row"]')))
        file_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="row"]')

        # Step 6: Print the total number of files
        print(f"Total number of files: {len(file_elements)}")

        # Step 7: Loop through each file element and print their details
        for file_element in file_elements:
            filename = file_element.text
            print("Filename:", filename)

            # Additional interaction with the file element can be added here, if needed
            # For example, you can click on the file element, download, or perform other actions.

    def close_browser(self):
        # Step 8: Close the browser window when done
        self.driver.quit()


if __name__ == "__main__":
    google_drive = GoogleDriveAutomation()
    google_drive.login_to_google_drive('s72186017@gmail.com', '1234qwer!@#$')
    google_drive.get_file_list()
    google_drive.close_browser()
