# import asyncio
# from selenium_driverless import webdriver
# import random
# import time
# import traceback
# import csv

# # Helper functions
# def random_sleep(min_seconds=2, max_seconds=5):
#     sleep_time = random.uniform(min_seconds, max_seconds)
#     time.sleep(sleep_time)

# def get_processed_stocktwits_username_and_password_from_csv(csv_file):
#     try:
#         with open(csv_file, 'r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 if row.get("Processed") == "Yes":  # Pick rows with Processed: Yes
#                     return row.get("Stocktwits Username"), row.get("Stocktwits Password")
#         print("No rows marked as 'Processed: Yes'.")
#         return None, None
#     except Exception as e:
#         print(f"Error reading CSV file: {e}")
#         return None, None

# # Function to log in using credentials from the CSV file
# async def user_mail_login(driver, csv_file='stocktwits_account.csv'):
#     try:
#         # Get username and password marked as "Processed: Yes"
#         username, password = get_processed_stocktwits_username_and_password_from_csv(csv_file)
#         if not username or not password:
#             print("Error: No username/password found marked as 'Processed: Yes'. Exiting.")
#             return False

#         await driver.maximize_window()
#         await driver.get("https://mail.aeroforcebase.com/", wait_load=True, timeout=120)
#         print("Website opened successfully.")

#         # Enter the username
#         username_field = await driver.find_element("xpath", "//*[@id='login_user']", timeout=20)
#         if not username_field:
#             print("Username field not found. Exiting.")
#             return False

#         await username_field.click()
#         await username_field.send_keys(username)
#         print(f"Username '{username}' entered.")
#         await asyncio.sleep(5)

#         # Enter the password
#         password_field = await driver.find_element("xpath", "//*[@id='pass_user']", timeout=20)
#         if not password_field:
#             print("Password field not found. Exiting.")
#             return False

#         await password_field.click()
#         await password_field.send_keys(password)
#         print(f"Password entered for username '{username}'.")
#         await asyncio.sleep(5)

#         # Click the login button
#         login_button = await driver.find_element("xpath", "//button[@type='submit' and @class='btn btn-xs-lg btn-success' and @value='Login' and text()='Login']", timeout=30)
#         if not login_button:
#             print("Login button not found. Exiting.")
#             return False

#         await driver.execute_script("arguments[0].click();", login_button)
#         print("Login button clicked.")

#         # Wait for the page to load and check the current URL
#         await asyncio.sleep(10) 
#         time.sleep(5) # Allow time for the redirect
#         current_url = await driver.current_url

#         if not current_url:
#             print("Failed to fetch current URL. Exiting.")
#             return False

#         print(f"Current URL after login: {current_url}")
#         if "signin" in current_url:
#             print("Login failed.")
#             return False

#         print("Login successful.")
#         return True

#     except Exception as e:
#         print(f"Error during login: {e}")
#         traceback.print_exc()
#         return False
    

    
# # Entry point to run the signup process
# async def main():
#     try:
#         # Initialize WebDriver
#         options = webdriver.ChromeOptions()
#         driver = await webdriver.Chrome(options=options)

#         # Run the signup process
#         await user_mail_login(driver, 'stocktwits_accounts.csv')

#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         traceback.print_exc()

#     finally:
#         if 'driver' in locals():
#             await driver.quit()

# # Run the script
# if __name__ == "__main__":
#     asyncio.run(main())






import asyncio
from selenium_driverless import webdriver
import random
import time
import traceback
import csv

# Helper function to simulate random sleep
def random_sleep(min_seconds=2, max_seconds=5):
    sleep_time = random.uniform(min_seconds, max_seconds)
    time.sleep(sleep_time)

# Function to get all users that need processing (skip those already verified)
def get_unverified_users(csv_file):
    users = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Skip users where Stocktwits_Account_Verified is "Verified"
                if row.get("Stocktwits_Account_Verfied") != "Verified" and row.get("Processed") == "Yes":
                    users.append(row)
        if not users:
            print("No unverified users found.")
        return users
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

# Function to log in using credentials from the CSV file
async def user_mail_login(driver, csv_file='stocktwits_accounts.csv'):
    try:
        # Get all unverified and processed users
        users = get_unverified_users(csv_file)
        
        # If no valid user is found, exit
        if not users:
            print("No unverified and processed username/password found. Exiting.")
            return False
        
        for user in users:
            username = user.get("Stocktwits Username")
            password = user.get("Stocktwits Password")

            # Process the login for each user
            await driver.maximize_window()
            await driver.get("https://mail.aeroforcebase.com/", wait_load=True, timeout=120)
            print("Website opened successfully.")

            # Enter the username
            username_field = await driver.find_element("xpath", "//*[@id='login_user']", timeout=20)
            if not username_field:
                print(f"Username field not found for {username}. Exiting.")
                return False

            await username_field.click()
            await username_field.send_keys(username)
            print(f"Username '{username}' entered.")
            await asyncio.sleep(5)

            # Enter the password
            password_field = await driver.find_element("xpath", "//*[@id='pass_user']", timeout=20)
            if not password_field:
                print(f"Password field not found for {username}. Exiting.")
                return False

            await password_field.click()
            await password_field.send_keys(password)
            print(f"Password entered for username '{username}'.")
            await asyncio.sleep(5)

            # Click the login button
            login_button = await driver.find_element("xpath", "//button[@type='submit' and @class='btn btn-xs-lg btn-success' and @value='Login' and text()='Login']", timeout=30)
            if not login_button:
                print(f"Login button not found for {username}. Exiting.")
                return False

            await driver.execute_script("arguments[0].click();", login_button)
            print(f"Login button clicked for {username}.")

            # Wait for the page to load and check the current URL
            await asyncio.sleep(10)
            time.sleep(5)  # Allow time for the redirect
            current_url = await driver.current_url

            if not current_url:
                print("Failed to fetch current URL. Exiting.")
                return False

            print(f"Current URL after login: {current_url}")
            if "signin" in current_url:
                print(f"Login failed for {username}.")
                continue  # Skip this user and move to the next one

            print(f"Login successful for {username}.")
            
            # Mark the user as processed after a successful login
            mark_user_as_processed(csv_file, user)

        return True

    except Exception as e:
        print(f"Error during login: {e}")
        traceback.print_exc()
        return False

# Function to mark the user as processed in the CSV file
def mark_user_as_processed(csv_file, row):
    try:
        # Read the current CSV
        rows = []
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        # Find the row and update the "Processed" field
        for r in rows:
            if r == row:
                r["Processed"] = "Yes"

        # Write the updated data back to CSV
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            fieldnames = rows[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"User {row.get('Stocktwits Username')} marked as processed.")

    except Exception as e:
        print(f"Error updating CSV file: {e}")
        traceback.print_exc()

# Entry point to run the login process
async def main():
    try:
        # Initialize WebDriver
        options = webdriver.ChromeOptions()
        driver = await webdriver.Chrome(options=options)

        # Run the login process
        await user_mail_login(driver, 'stocktwits_accounts.csv')

    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()

    finally:
        if 'driver' in locals():
            await driver.quit()

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
