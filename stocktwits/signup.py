# import asyncio
# import csv
# import random
# import time
# import traceback
# from selenium_driverless import webdriver

# # Helper function to simulate random sleep asynchronously
# async def random_sleep(min_seconds=2, max_seconds=5):
#     sleep_time = random.uniform(min_seconds, max_seconds)
#     await asyncio.sleep(sleep_time)  # Use async sleep instead of time.sleep()

# # Read the next unprocessed user from the CSV file
# def get_next_unprocessed_user(csv_file="stocktwits_accounts.csv"):
#     try:
#         with open(csv_file, 'r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             rows = list(reader)
#             for row in rows:
#                 if row.get("Stocktwits Processed") != "Yes":  # Skip rows marked as "Yes"
#                     return row, rows.index(row)  # Return the user and its index
#         print("No unprocessed users found.")
#         return None, None
#     except Exception as e:
#         print(f"Error reading CSV file: {e}")
#         return None, None

# # Update the CSV file to mark the user as processed
# def mark_user_as_processed(csv_file, row_index):
#     try:
#         rows = []
#         with open(csv_file, 'r', newline='', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             rows = list(reader)
#             fieldnames = reader.fieldnames  # Read the fieldnames from the original file

#         if row_index is not None and row_index < len(rows):
#             rows[row_index]["Stocktwits Processed"] = "Yes"  # Mark user as processed

#         # Ensure that 'Stocktwits Processed' is in the fieldnames
#         if 'Stocktwits Processed' not in fieldnames:
#             fieldnames.append('Stocktwits Processed')  # Add 'Stocktwits Processed' if it's missing

#         # Write back to the CSV file with the updated 'Stocktwits Processed' column
#         with open(csv_file, 'w', newline='', encoding='utf-8') as file:
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()  # Write the header row
#             writer.writerows(rows)  # Write the updated rows

#         print(f"User at index {row_index} marked as processed in {csv_file}.")
    
#     except Exception as e:
#         print(f"Error updating CSV file: {e}")

# # Function to sign up on StockTwits
# async def stocktwits_signup(driver, csv_file="stocktwits_accounts.csv"):
#     try:
#         # Get the next unprocessed user
#         user, row_index = get_next_unprocessed_user(csv_file)
#         if not user:
#             print("Error: No unprocessed users found. Exiting.")
#             return False

#         username = user.get("Stocktwits Username")
#         password = user.get("Stocktwits Password")
#         if not username or not password:
#             print("Error: Missing Stocktwits Username or Password. Exiting.")
#             return False

#         await driver.get("https://stocktwits.com/signup?next=/", wait_load=True, timeout=120)
#         print("StockTwits website opened successfully.")

#         # Enter the email (username)
#         email_field = await driver.find_element("xpath", "//input[@name='email']", timeout=10)
#         if not email_field:
#             print("Email field not found. Exiting.")
#             return False

#         await email_field.click()
#         await email_field.send_keys(username)
#         print(f"StockTwits Username '{username}' entered.")
#         await random_sleep()

#         # Check if the signup button is enabled after entering the email
#         signup_button = await driver.find_element("xpath", "//button[@type='submit' and contains(@class, 'Button_primary__PFIP8') and text()='Sign Up']", timeout=10)
#         if not signup_button:
#             print("Signup button not found. Exiting.")
#             return False

#         # Check if the signup button is still disabled
#         is_disabled = await driver.execute_script("return arguments[0].disabled;", signup_button)
#         if is_disabled:
#             print("Signup button is disabled, marking user as processed.")
#             # Mark the user as processed in the CSV file
#             mark_user_as_processed(csv_file, row_index)
#             print("User marked as processed in CSV.")
#             return False  # Exit the program

#         # If the signup button is enabled, proceed to click it
#         await driver.execute_script("arguments[0].click();", signup_button)
#         print("Signup button clicked.")

#         # Wait and check the current URL
#         await asyncio.sleep(5)  # Allow time for the redirect
#         current_url = await driver.current_url  # Use await to get the URL value

#         if not current_url:
#             print("Failed to fetch current URL. Exiting.")
#             return False
        
#         # Proceed with after signup process (if necessary)
#         await after_signup_process(driver, user)
#         return True

#     except Exception as e:
#         print(f"Error during StockTwits signup: {e}")
#         traceback.print_exc()
#         return False

# # Function to be called after successful signup (if applicable)
# async def after_signup_process(driver, user):
#     try:
#         # Retrieve name and username from user dictionary
#         name = user.get("Username")
#         username = user.get("Username")
#         password = user.get("Stocktwits Password")

#         if not name:
#             print("Error: Missing Name field. Exiting.")
#             return False

#         # Find the name field and enter the user's name
#         name_field = await driver.find_element("xpath", "//input[@name='name']", timeout=10)
#         if not name_field:
#             print("Name field not found. Exiting.")
#             return False

#         await name_field.click()
#         await name_field.send_keys(name)
#         print(f"StockTwits Name '{name}' entered.")
#         await random_sleep()

#         # Find the username field and enter the user's name
#         username_field = await driver.find_element("xpath", "//input[@name='login']", timeout=10)
#         if not username_field:
#             print("Username field not found. Exiting.")
#             return False

#         await username_field.click()
#         await username_field.send_keys(username)
#         print(f"Username '{username}' entered.")
#         await random_sleep()

#         # Find the password field and enter the user's name
#         password_field = await driver.find_element("xpath", "//input[@name='password']", timeout=10)
#         if not password_field:
#             print("Password field not found. Exiting.")
#             return False

#         await password_field.click()
#         await password_field.send_keys(password)
#         print(f"Password '{password}' entered.")
#         await random_sleep()

#         # Click the signup button
#         login_button = await driver.find_element("xpath", "//button[@type='submit' and text()='Sign Up']", timeout=30)
#         if not login_button:
#             print("Login button not found. Exiting.")
#             return False

#         await driver.execute_script("arguments[0].click();", login_button)
#         print("Login button clicked.")
#         await random_sleep()
#         time.sleep(10)

#         print("After signup process completed.")

#     except Exception as e:
#         print(f"Error during after signup process: {e}")
#         traceback.print_exc()

# # # Entry point to run the signup process
# # async def main():
# #     try:
# #         # Initialize WebDriver
# #         options = webdriver.ChromeOptions()
# #         driver = await webdriver.Chrome(options=options)

# #         # Run the signup process
# #         await stocktwits_signup(driver)

# #     except Exception as e:
# #         print(f"Unexpected error: {e}")
# #         traceback.print_exc()

# #     finally:
# #         if 'driver' in locals():
# #             await driver.quit()

# # # Run the script
# # if __name__ == "__main__":
# #     asyncio.run(main())


import asyncio
import csv
import random
import time
import traceback
from selenium_driverless import webdriver

# Helper function to simulate random sleep asynchronously
async def random_sleep(min_seconds=2, max_seconds=5):
    sleep_time = random.uniform(min_seconds, max_seconds)
    await asyncio.sleep(sleep_time)  # Use async sleep instead of time.sleep()

# Read the next unprocessed user from the CSV file
def get_next_unprocessed_user(csv_file="stocktwits_accounts.csv"):
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            for row in rows:
                if row.get("Stocktwits Processed") != "Yes":  # Skip rows marked as "Yes"
                    return row, rows.index(row)  # Return the user and its index
        print("No unprocessed users found.")
        return None, None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None, None

# Update the CSV file to mark the user as processed
def mark_user_as_processed(csv_file, row_index):
    try:
        rows = []
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            fieldnames = reader.fieldnames  # Read the fieldnames from the original file

        if row_index is not None and row_index < len(rows):
            rows[row_index]["Stocktwits Processed"] = "Yes"  # Mark user as processed

        # Ensure that 'Stocktwits Processed' is in the fieldnames
        if 'Stocktwits Processed' not in fieldnames:
            fieldnames.append('Stocktwits Processed')  # Add 'Stocktwits Processed' if it's missing

        # Write back to the CSV file with the updated 'Stocktwits Processed' column
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            writer.writerows(rows)  # Write the updated rows

        print(f"User at index {row_index} marked as processed in {csv_file}.")
    
    except Exception as e:
        print(f"Error updating CSV file: {e}")

# Function to get all users that need processing (skip those already verified)
def get_unverified_users(csv_file):
    users = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Skip users where Stocktwits Processed is "Yes"
                if row.get("Stocktwits Processed") != "Yes" and row.get("Processed") == "Yes":
                    users.append(row)
        if not users:
            print("No unverified users found.")
        return users
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

# Function to sign up on StockTwits
async def stocktwits_signup(driver, csv_file="stocktwits_accounts.csv"):
    try:
        # Get the next unprocessed user
        user, row_index = get_next_unprocessed_user(csv_file)
        if not user:
            print("Error: No unprocessed users found. Exiting.")
            return False

        username = user.get("Stocktwits Username")
        password = user.get("Stocktwits Password")
        if not username or not password:
            print("Error: Missing Stocktwits Username or Password. Exiting.")
            return False

        await driver.get("https://stocktwits.com/signup?next=/", wait_load=True, timeout=120)
        print("StockTwits website opened successfully.")

        # Enter the email (username)
        email_field = await driver.find_element("xpath", "//input[@name='email']", timeout=10)
        if not email_field:
            print("Email field not found. Exiting.")
            return False

        await email_field.click()
        await email_field.send_keys(username)
        print(f"StockTwits Username '{username}' entered.")
        await random_sleep()

        # Check if the signup button is enabled after entering the email
        signup_button = await driver.find_element("xpath", "//button[@type='submit' and contains(@class, 'Button_primary__PFIP8') and text()='Sign Up']", timeout=10)
        if not signup_button:
            print("Signup button not found. Exiting.")
            return False

        # Check if the signup button is still disabled
        is_disabled = await driver.execute_script("return arguments[0].disabled;", signup_button)
        if is_disabled:
            print("Signup button is disabled, marking user as processed.")
            # Mark the user as processed in the CSV file
            mark_user_as_processed(csv_file, row_index)
            print("User marked as processed in CSV.")
            return False  # Exit the program

        # If the signup button is enabled, proceed to click it
        await driver.execute_script("arguments[0].click();", signup_button)
        print("Signup button clicked.")

        # Wait and check the current URL
        await asyncio.sleep(5)  # Allow time for the redirect
        current_url = await driver.current_url  # Use await to get the URL value

        if not current_url:
            print("Failed to fetch current URL. Exiting.")
            return False
        
        # Proceed with after signup process (if necessary)
        await after_signup_process(driver, user)
        return True

    except Exception as e:
        print(f"Error during StockTwits signup: {e}")
        traceback.print_exc()
        return False

# Function to be called after successful signup (if applicable)
async def after_signup_process(driver, user):
    try:
        # Retrieve name and username from user dictionary
        name = user.get("Username")
        username = user.get("Username")
        password = user.get("Stocktwits Password")

        if not name:
            print("Error: Missing Name field. Exiting.")
            return False

        # Find the name field and enter the user's name
        name_field = await driver.find_element("xpath", "//input[@name='name']", timeout=10)
        if not name_field:
            print("Name field not found. Exiting.")
            return False

        await name_field.click()
        await name_field.send_keys(name)
        print(f"StockTwits Name '{name}' entered.")
        await random_sleep()

        # Find the username field and enter the user's name
        username_field = await driver.find_element("xpath", "//input[@name='login']", timeout=10)
        if not username_field:
            print("Username field not found. Exiting.")
            return False

        await username_field.click()
        await username_field.send_keys(username)
        print(f"Username '{username}' entered.")
        await random_sleep()

        # Find the password field and enter the user's name
        password_field = await driver.find_element("xpath", "//input[@name='password']", timeout=10)
        if not password_field:
            print("Password field not found. Exiting.")
            return False

        await password_field.click()
        await password_field.send_keys(password)
        print(f"Password '{password}' entered.")
        await random_sleep()

        # Click the signup button
        login_button = await driver.find_element("xpath", "//button[@type='submit' and text()='Sign Up']", timeout=30)
        if not login_button:
            print("Login button not found. Exiting.")
            return False

        await driver.execute_script("arguments[0].click();", login_button)
        print("Login button clicked.")
        await random_sleep()
        time.sleep(10)

        print("After signup process completed.")

    except Exception as e:
        print(f"Error during after signup process: {e}")
        traceback.print_exc()

# Entry point to run the signup process
async def main():
    try:
        # Initialize WebDriver
        options = webdriver.ChromeOptions()
        driver = await webdriver.Chrome(options=options)

        # Run the signup process
        await stocktwits_signup(driver)

    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()

    finally:
        if 'driver' in locals():
            await driver.quit()

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
