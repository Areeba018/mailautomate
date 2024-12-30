import asyncio
import csv
import random
import time
import traceback
from selenium_driverless import webdriver

# Helper function to simulate random sleep
def random_sleep(min_seconds=2, max_seconds=5):
    sleep_time = random.uniform(min_seconds, max_seconds)
    time.sleep(sleep_time)

# Read the next unprocessed user from the CSV file
def get_next_unprocessed_user(csv_file="stocktwits_accounts.csv"):
    try:
        with open(csv_file, 'r') as file:
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
        random_sleep()

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
    # Implement after-signup logic if needed
    print("After signup process completed.")

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





