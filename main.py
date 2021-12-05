import time

from selenium import webdriver


def activate_steam_key(driver, steam_key):
    driver.get('https://store.steampowered.com/account/registerkey')

    key_textbox = driver.find_element_by_id('product_key')
    key_textbox.send_keys(steam_key)

    terms_conditions_checkbox = driver.find_element_by_id('accept_ssa');
    terms_conditions_checkbox.click()

    continue_button = driver.find_element_by_id('register_btn')
    continue_button.click()

    time.sleep(1)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://store.steampowered.com/account/registerkey')

    input("Press Enter to continue...")

    keys_file = open('Keys.txt', 'r')
    keys = keys_file.readlines()

    for key in keys:
        activate_steam_key(driver, key)
