from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
driver.maximize_window()

try:
    # Open the website
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    print("Website opened successfully.")

    # Wait for the login form to be present
    wait = WebDriverWait(driver, 20)
    username_field = wait.until(EC.presence_of_element_located((By.ID, "txt-username")))
    password_field = wait.until(EC.presence_of_element_located((By.ID, "txt-password")))
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "btn-login")))

    print("Located username, password fields, and login button.")

    # Fill in the login details
    username_field.send_keys("John Doe")  # Use the demo account username
    password_field.send_keys("ThisIsNotAPassword")  # Use the demo account password
    print("Filled in login credentials.")

    # Click the login button
    login_button.click()
    print("Clicked login button.")

    # Wait for the appointment page link
    make_appointment_button = wait.until(EC.element_to_be_clickable((By.ID, "btn-make-appointment")))
    make_appointment_button.click()
    print("Navigated to the appointment page.")

    # Fill in the appointment form
    facility_dropdown = wait.until(EC.presence_of_element_located((By.ID, "combo_facility")))
    facility_dropdown.send_keys("Tokyo CURA Healthcare Center")  # Example facility

    healthcare_program_checkbox = driver.find_element(By.ID, "chk_hospotal_readmission")
    healthcare_program_checkbox.click()  # Check this option

    medicaid_radio = driver.find_element(By.ID, "radio_program_medicaid")
    medicaid_radio.click()  # Select Medicaid as healthcare program

    visit_date_field = driver.find_element(By.ID, "txt_visit_date")
    visit_date_field.send_keys("12/25/2024")  # Set the visit date

    comment_field = driver.find_element(By.ID, "txt_comment")
    comment_field.send_keys("Looking forward to the appointment.")  # Add a comment

    # Submit the appointment form
    book_appointment_button = driver.find_element(By.ID, "btn-book-appointment")
    book_appointment_button.click()
    print("Appointment request submitted.")

    # Confirm successful booking
    confirmation_header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "page-header")))
    print("Appointment booked successfully! Confirmation page header text:", confirmation_header.text)

except Exception as e:
    print("An error occurred during the test:", e)

finally:
    # Wait to observe the results and close the WebDriver
    time.sleep(5)
    driver.quit()
