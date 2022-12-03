import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def activate_steam_key(_driver, steam_key):
    _driver.get('https://store.steampowered.com/account/registerkey')

    key_textbox = _driver.find_element(By.ID, 'product_key')
    key_textbox.send_keys(steam_key)

    terms_conditions_checkbox = _driver.find_element(By.ID, 'accept_ssa');
    terms_conditions_checkbox.click()

    continue_button = _driver.find_element(By.ID, 'register_btn')
    continue_button.click()

    time.sleep(1)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://store.steampowered.com/account/registerkey')

    input("Press Enter to continue...")

    keys_file = open('Keys.txt', 'r')
    keys = keys_file.readlines()

    for key in keys:
        activate_steam_key(driver, key)
