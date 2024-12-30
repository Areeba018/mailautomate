import asyncio
from selenium_driverless import webdriver
import random
import time
import traceback
import csv

# Helper function for random sleep
def random_sleep(min_seconds=2, max_seconds=5):
    sleep_time = random.uniform(min_seconds, max_seconds)
    time.sleep(sleep_time)

# Read the next unprocessed user from the CSV file
def get_next_unprocessed_user(csv_file="stocktwits_accounts.csv"):
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            for row in rows:
                if row.get("Stocktwits_Account_Verfied") != "Verified":  
                    return row, rows.index(row)  
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
            fieldnames = reader.fieldnames  

        if row_index is not None and row_index < len(rows):
            rows[row_index]["Stocktwits_Account_Verfied"] = "Verified"  

        # Ensure that 'Stocktwits_Account_Verfied' is in the fieldnames
        if 'Stocktwits_Account_Verfied' not in fieldnames:
            fieldnames.append('Stocktwits_Account_Verfied') 

        # Write back to the CSV file with the updated 'Stocktwits_Account_Verfied' column
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            writer.writerows(rows)  # Write the updated rows

        print(f"User at index {row_index} marked as processed in {csv_file}.")
    
    except Exception as e:
        print(f"Error updating CSV file: {e}")

# Function to confirm Stocktwits account
async def confirm_stocktwits_account(driver, csv_file="stocktwits_accounts.csv"): 
    try:
        # Get the next unprocessed user
        user, row_index = get_next_unprocessed_user(csv_file)
        if not user:
            print("Error: No unprocessed users found. Exiting.")
            return False

        print(f"Processing user: {user}")
        
        # Allow time for the page to load completely
        await asyncio.sleep(5)

        # Find the email element
        email_element = await driver.find_element("xpath", "//button[@aria-label='Verify Your Email on Stocktwits' and contains(@class, 'md-no-style') and contains(@class, 'md-button')]",timeout=70)

        # Click the email element
        await email_element.click()  
        print("Clicked on the Stocktwits email.")
        random_sleep()

        # Find the Verify Email element
        verify_email_element = await driver.find_element(
            "xpath", 
            "//a[text()='Verify Your Email']", 
            timeout=50
        )

        # Click the Verify Email link
        await verify_email_element.click()  
        print("Clicked on the Verify Email.")
        random_sleep()

        # Mark the user as processed in the CSV file
        mark_user_as_processed(csv_file, row_index)
        print("User verification completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

# # Main function to initialize the driver and process the accounts
# async def main():
#     csv_file = "stocktwits_accounts.csv"  # Path to your CSV file
#     driver = webdriver.Chrome()  # Initialize your Selenium driver
#     try:
#         await confirm_stocktwits_account(driver, csv_file)
#     finally:
#         await driver.quit()

# # Run the script
# asyncio.run(main())
