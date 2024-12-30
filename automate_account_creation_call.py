import asyncio
import random
from selenium_driverless import webdriver
from automate_account_creation.login import mail_login
from automate_account_creation.add_mailbox import click_mailboxes_button
from automate_account_creation.add_mailbox_form import add_mailbox_form, get_first_username_and_password_from_csv
from user_dashboard.user_login import user_mail_login
from user_dashboard.webmail import click_webmail_button
from user_dashboard.confirm_account import confirm_stocktwits_account
from stocktwits.create_stocktwits_csv import create_extended_csv
from stocktwits.signup import stocktwits_signup

# Random sleep function
async def random_sleep(min_seconds=10, max_seconds=15):
    await asyncio.sleep(random.uniform(min_seconds, max_seconds))


# Main execution function
async def main():
    # # Instance 1 for Admin operations
    # options_admin = webdriver.ChromeOptions()
    # admin_driver = await webdriver.Chrome(options=options_admin)

    # try:
    #     # Login to the mail system (Admin)
    #     await mail_login(admin_driver)

    #     # Click the mailboxes button (Admin)
    #     await click_mailboxes_button(admin_driver)

    #     # Add mailbox form (Admin)
    #     username, password = get_first_username_and_password_from_csv('processed.csv')
    #     await add_mailbox_form(admin_driver, username, password)

    # finally:
    #     print("Closing Admin driver...")
    #     await admin_driver.quit()

    # Instance 2 for User operations
    options_user = webdriver.ChromeOptions()
    user_driver = await webdriver.Chrome(options=options_user)

    try:

        # run stocktwits account csv creation
        create_extended_csv()

        # Run the signup process
        await stocktwits_signup(user_driver)

        

        # # Login to the mail system using credentials from the CSV (User)
        # await user_mail_login(user_driver, 'stocktwits_accounts.csv')
        
        # # Perform webmail operations (User)
        # await click_webmail_button(user_driver)

        # await confirm_stocktwits_account(user_driver, 'stocktwits_accounts.csv')

    finally:
        print("Closing User driver...")
        await user_driver.quit()


if __name__ == "__main__":
    asyncio.run(main())
