import asyncio
from selenium_driverless import webdriver
import random
import time
import traceback

# Helper function for random sleep
def random_sleep(min_seconds=2, max_seconds=5):
    sleep_time = random.uniform(min_seconds, max_seconds)
    time.sleep(sleep_time)

async def click_webmail_button(driver):  # Accept driver as an argument
    try:
        # Navigate to the target page
        target_url = "https://mail.aeroforcebase.com/user"  
        await driver.get(target_url, wait_load=True, timeout=120)
        print("Page opened successfully.")

        # Allow time for the page to load completely
        await asyncio.sleep(5)

        # Find the button using XPath
        button = await driver.find_element("xpath", "//*[@id='collapse-tab-user-auth']/div[1]/div[2]/a", timeout=30)

        if button:
            # Click the button
            await button.click()
            print("Mailboxes button clicked successfully!")
            await asyncio.sleep(10)
        else:
            print("Mailboxes button not found.")

        # Wait and check the current URL
        await asyncio.sleep(5)  # Allow time for the redirect
    #     current_url = await driver.current_url  # Use await to get the URL value

    #     if not current_url:
    #         print("Failed to fetch current URL. Exiting.")
    #         return False

    #     print(f"Current URL after login: {current_url}")  # Debug log
    #     if "INBOX" in current_url:
    #         print(" failed.")
    #         return False

    #     print("successful.")
    #     return True

    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     traceback.print_exc()

# Get the updated list of tabs
        original_tabs = await driver.window_handles
        print(f"Original tabs: {original_tabs}")

        new_tabs = await driver.window_handles
        print(f"Updated tabs: {new_tabs}")

        # Identify the new tab
        new_tab = list(set(new_tabs) - set(original_tabs))
        if not new_tab:
            print("New tab did not open. Exiting.")
            return False

        new_tab_handle = new_tab[0]
        print(f"New tab handle: {new_tab_handle}")

        # Switch to the new tab
        await driver.switch_to.window(new_tab_handle)
        print("Switched to the new tab.")

        # Allow time for the new tab to load
        await asyncio.sleep(5)

        # Get the URL of the new tab
        new_tab_url = await driver.current_url
        print(f"New tab URL: {new_tab_url}")

        # Perform additional checks if needed
        if not new_tab_url:
            print("Failed to fetch the new tab URL. Exiting.")
            return False

        print("Operation successful.")
        return new_tab_url
    

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
        return False
    

