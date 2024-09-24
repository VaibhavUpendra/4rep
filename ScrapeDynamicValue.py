from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disbale-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    driver.get("https://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    return float(text.split(":")[1])


def main():
    driver = get_driver()
    time.sleep(2)
    dynamic_element= driver.find_
    return clean_text(dynamic_element.text)element(By.XPATH,"/html/body/div[1]/div/h1[2]")

print(main())