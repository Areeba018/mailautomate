import asyncio
import random
from selenium_driverless import webdriver
from user_dashboard.user_login import user_mail_login
from user_dashboard.webmail import click_webmail_button
from user_dashboard.confirm_account import confirm_stocktwits_account


# Random sleep function
async def random_sleep(min_seconds=10, max_seconds=15):
    await asyncio.sleep(random.uniform(min_seconds, max_seconds))


# Main execution function
async def main():

    # Instance 2 for User operations
    options_user = webdriver.ChromeOptions()
    user_driver = await webdriver.Chrome(options=options_user)

    try:
 

        # Login to the mail system using credentials from the CSV (User)
        await user_mail_login(user_driver, 'stocktwits_accounts.csv')
        
        # Perform webmail operations (User)
        await click_webmail_button(user_driver)

        await confirm_stocktwits_account(user_driver, 'stocktwits_accounts.csv')

    finally:
        print("Closing User driver...")
        await user_driver.quit()


if __name__ == "__main__":
    asyncio.run(main())
