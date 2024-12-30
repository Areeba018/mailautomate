# import asyncio
# import csv
# from selenium_driverless import webdriver
# import random
# import time
# import traceback

# # Helper function for random sleep
# def random_sleep(min_seconds=2, max_seconds=5):
#     sleep_time = random.uniform(min_seconds, max_seconds)
#     time.sleep(sleep_time)

# # Read the first username from the CSV file
# def get_first_username_and_password_from_csv(csv_file):
#     with open(csv_file, 'r') as file:
#         reader = csv.DictReader(file)  # Read as a dictionary
#         first_row = next(reader)  # Get the first row
#         return first_row.get('Username'), first_row.get('Password')

# async def add_mailbox_form(driver, username, password):  
#     try:
#         # Enter username into the input field using the XPath
#         username_input = await driver.find_element("xpath", "//input[@name='local_part']", timeout=30)
#         if username_input:
#             await username_input.send_keys(username)  # Enter the username into the input field
#             print(f"Username '{username}' entered successfully!")
#             await asyncio.sleep(5)
#         else:
#             print("Username input field not found.")
        
#         # Enter password into the 'password' input field
#         password_input = await driver.find_element("xpath", "//input[@type='password']", timeout=30)
#         if password_input:
#             await password_input.send_keys(password)  
#             print(f"Password '{password}' entered successfully!")
#             await asyncio.sleep(5)
#         else:
#             print("Password input field not found.")

#         # Enter Confirm password into the 'password' input field
#         password2_input = await driver.find_element("xpath", "//input[@name='password2']", timeout=30)
#         if password_input:
#             await password2_input.send_keys(password)  
#             print(f"Confirm Password '{password}' entered successfully!")
#             await asyncio.sleep(5)
#         else:
#             print("confirm Password input field not found.")

#         # Enter quota into the 'quota' input field
#         quota_input = await driver.find_element("xpath", "//input[@name='quota']", timeout=30)
#         if password_input:
#             await quota_input.clear()
#             await quota_input.send_keys("1024")  
#             print(f"Quota '{1024}' entered successfully!")
#             await asyncio.sleep(5)
#         else:
#             print("quota input field not found.")

#         # Find the button using the provided XPath and click it
#         button = await driver.find_element("xpath", "//button[@class='btn btn-xs-lg d-block d-sm-inline btn-success' and @data-action='add_item']", timeout=30)
#         if button:
#             await button.click() 
#             print("Item Add Successfully!")
#             time.sleep(5)
#         else:
#             print("Button not found.")



       
        
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         traceback.print_exc()


import asyncio
import csv
from selenium_driverless import webdriver
import random
import time
import traceback

# Helper function for random sleep
def random_sleep(min_seconds=2, max_seconds=5):
    sleep_time = random.uniform(min_seconds, max_seconds)
    time.sleep(sleep_time)

# Read the next unprocessed username and password from the CSV
def get_first_username_and_password_from_csv(csv_file, output_file="processed.csv"):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)  # Read as a dictionary
        rows = list(reader)  # Load all rows into memory
        processed_row = None

        for row in rows:
            if row.get("Processed") != "Yes":  # Find the first unprocessed row
                processed_row = row
                row["Processed"] = "Yes"  # Mark it as processed
                break

        # Update the file with the "Processed" status
        fieldnames = reader.fieldnames + ["Processed"] if "Processed" not in reader.fieldnames else reader.fieldnames

        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    if processed_row:
        return processed_row.get("Username"), processed_row.get("Password")
    else:
        print("All rows have been processed.")
        return None, None

async def add_mailbox_form(driver, username, password):  
    try:
        # Enter username into the input field using the XPath
        username_input = await driver.find_element("xpath", "//input[@name='local_part']", timeout=30)
        if username_input:
            await username_input.send_keys(username)  # Enter the username into the input field
            print(f"Username '{username}' entered successfully!")
            await asyncio.sleep(5)
        else:
            print("Username input field not found.")
        
        # Enter password into the 'password' input field
        password_input = await driver.find_element("xpath", "//input[@type='password']", timeout=30)
        if password_input:
            await password_input.send_keys(password)  
            print(f"Password '{password}' entered successfully!")
            await asyncio.sleep(5)
        else:
            print("Password input field not found.")

        # Enter Confirm password into the 'password' input field
        password2_input = await driver.find_element("xpath", "//input[@name='password2']", timeout=30)
        if password_input:
            await password2_input.send_keys(password)  
            print(f"Confirm Password '{password}' entered successfully!")
            await asyncio.sleep(5)
        else:
            print("Confirm Password input field not found.")

        # Enter quota into the 'quota' input field
        quota_input = await driver.find_element("xpath", "//input[@name='quota']", timeout=30)
        if quota_input:
            await quota_input.clear()
            await quota_input.send_keys("1024")  
            print(f"Quota '{1024}' entered successfully!")
            await asyncio.sleep(5)
        else:
            print("Quota input field not found.")

        # Find the button using the provided XPath and click it
        button = await driver.find_element("xpath", "//button[@class='btn btn-xs-lg d-block d-sm-inline btn-success' and @data-action='add_item']", timeout=30)
        if button:
            await button.click() 
            print("Item added successfully!")
            await asyncio.sleep(5)
        else:
            print("Button not found.")

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

