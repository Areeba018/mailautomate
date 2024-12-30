import asyncio
from selenium_driverless import webdriver
import random
import time
import traceback

# Helper functions
def random_sleep(min_seconds=2, max_seconds=5):
    sleep_time = random.uniform(min_seconds, max_seconds)
    time.sleep(sleep_time)

async def mail_login(driver):
    try:
        await driver.maximize_window()
        await driver.get("https://mail.aeroforcebase.com/", wait_load=True, timeout=120)
        print("website opened successfully.")


        # Enter the username
        username_field = await driver.find_element("xpath", "//*[@id='login_user']", timeout=20)
        if not username_field:
            print("Username field not found. Exiting.")
            return False
        
        await username_field.click() 
        await username_field.send_keys("Areeba")  
        print("Username entered.")
        random_sleep()

        # Wait for the password field to appear
        password_field = await driver.find_element("xpath", "//*[@id='pass_user']", timeout=20)
        if not password_field:
            print("Password field not found. Exiting.")
            return False

        await password_field.click()  # Await click coroutine
        await password_field.send_keys("Areeb@$$")  # Await send_keys coroutine
        print("Password entered.")
        random_sleep()

        # Click the login button using the correct XPath
        login_button = await driver.find_element("xpath", "//button[@type='submit' and @class='btn btn-xs-lg btn-success' and @value='Login' and text()='Login']", timeout=30)
        
        if not login_button:
         print("Login button not found. Exiting.")
         return False
        await driver.execute_script("arguments[0].click();", login_button)
        print("Login button clicked.")


        # Wait and check the current URL
        await asyncio.sleep(5)  # Allow time for the redirect
        current_url = await driver.current_url  # Use await to get the URL value

        if not current_url:
            print("Failed to fetch current URL. Exiting.")
            return False

        print(f"Current URL after login: {current_url}")  # Debug log
        if "signin" in current_url:
            print("Login failed.")
            return False

        print("Login successful.")
        return True

    except Exception as e:
        print(f"Error during login: {e}")
        traceback.print_exc() 
        return False
