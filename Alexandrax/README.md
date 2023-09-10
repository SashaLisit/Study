# Google Drive Automation Script Readme

## Introduction

This script is designed to automate interactions with Google Drive using the Selenium web automation library. It allows you to log in to your Google Drive account and retrieve a list of files. This README provides instructions on how to set up and use the script effectively.

## Prerequisites

Before using the script, ensure you have the following prerequisites in place:

1. **Python and Pip**: Make sure you have Python installed on your system. You'll also need Pip to install the necessary libraries.

2. **Selenium Library**: Install the Selenium library using Pip:

   ```
   pip install selenium
   ```

3. **WebDriver Installation**: Download the WebDriver for your web browser. This script is configured to use the Chrome WebDriver. Download the appropriate version of the Chrome WebDriver that matches your Chrome browser version. You can download it from the official Selenium WebDriver website: [Selenium WebDriver Downloads](https://selenium-python.readthedocs.io/installation.html#drivers)

4. **Path Configuration (Optional)**: Ensure that the WebDriver executable is in your system's PATH environment variable. Alternatively, you can specify the WebDriver's path explicitly in the script (see script customization below).

## Providing Login Credentials

To provide your Google Drive login credentials to the script, follow these steps:

1. Open the script in a text editor or Python IDE.

2. Locate the following line in the script:

   ```python
   google_drive.login_to_google_drive('s72186017@gmail.com', '1234qwer!@#$')
   ```

3. Replace the email and password within the single quotes with your Google account's email and password.

## Executing the Script

To execute the script, follow these steps:

1. Open a command prompt or terminal window on your computer.

2. Navigate to the directory where you have saved the script.

3. Run the script using Python:

   ```
   python lumix.py
   ```

   Replace `script_name.py` with the actual name of your script file.

4. The script will:

   - Open a Chrome web browser.
   - Automatically log in to your Google Drive account using the provided credentials.
   - Retrieve a list of files from your Google Drive.
   - Print the details of each file.

5. After completing the script's tasks, it will automatically close the Chrome browser.

## Script Customization

You can customize the script further to perform additional actions on the Google Drive files or adjust wait times to suit your environment:

- Modify the script to interact with the file elements as needed. For example, you can add code to click on a file element, download files, or perform other actions.

- Adjust the sleep and wait times in the script to ensure that web elements load correctly. The script contains sleep and wait times specified as `time.sleep(30)` and `WebDriverWait(self.driver, 40)`. Modify these values to match your system and network speed.

By following these instructions, you can use the provided script to automate interactions with Google Drive, making it easier to manage and access your files.
