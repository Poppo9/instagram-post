import time
from funcs.selenium_utils import setup_driver

def main():

    driver = setup_driver(headless=False)
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    time.sleep(3)
    title = driver.title
    print(title)


if __name__=='__main__':
    main()