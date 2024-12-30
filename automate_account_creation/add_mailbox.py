import asyncio
from selenium_driverless import webdriver
import random
import time
import traceback

# Helper function for random sleep
def random_sleep(min_seconds=2, max_seconds=5):
    sleep_time = random.uniform(min_seconds, max_seconds)
    time.sleep(sleep_time)

async def click_mailboxes_button(driver):  # Accept driver as an argument
    try:
        # Navigate to the target page
        target_url = "https://mail.aeroforcebase.com/mailbox"  
        await driver.get(target_url, wait_load=True, timeout=120)
        print("Page opened successfully.")

        # Allow time for the page to load completely
        await asyncio.sleep(5)

        # Find the button using XPath
        button = await driver.find_element("xpath", "//*[@id='mail-content']/ul/li[2]/button", timeout=30)

        if button:
            # Click the button
            await button.click()
            print("Mailboxes button clicked successfully!")
        else:
            print("Mailboxes button not found.")

        # Now, click on the element using the new XPath
        add_mailbox_button = await driver.find_element("xpath", "//*[@id='collapse-tab-mailboxes']/div[1]/div[2]/a[3]", timeout=30)
        if add_mailbox_button:
            await add_mailbox_button.click()  # Click the element with the specified XPath
            print("Add Mailbox button clicked successfully!")
            await asyncio.sleep(5)
        else:
            print("Add Mailbox button not found.")

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
