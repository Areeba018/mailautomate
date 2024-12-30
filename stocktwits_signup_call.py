import asyncio
import random
from selenium_driverless import webdriver
from stocktwits.create_stocktwits_csv import create_extended_csv
from stocktwits.signup import stocktwits_signup

# Random sleep function
async def random_sleep(min_seconds=10, max_seconds=15):
    await asyncio.sleep(random.uniform(min_seconds, max_seconds))


# Main execution function
async def main():

    # Instance 2 for User operations
    options_user = webdriver.ChromeOptions()
    user_driver = await webdriver.Chrome(options=options_user)

    try:
        # run stocktwits account csv creation
        # create_extended_csv()

        # Run the signup process
        await stocktwits_signup(user_driver)



    finally:
        print("Closing User driver...")
        await user_driver.quit()


if __name__ == "__main__":
    asyncio.run(main())
