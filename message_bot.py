import time

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

whatsapp_api = "https://api.whatsapp.com/send?phone=91"  # format of url to open chat with someone

hello = "Beep Boop, I'm a bot\nHey, "  # what to print before name

# what to print after name
message = "This is to remind you that Ready Set Code is tomorrow at 3:30pm!" \
          " Location will be given out soon (Most probably in D-building, 3rd floor)." \
          "\nSee you tomorrow! :)\n- The Script Group\n"


# method to send a message to someone
def sendMessage(num, name, browser):
    api = whatsapp_api + str(num)  # specific url
    final = hello + name + "!\n" + message  # full message with name
    print(api, name)
    browser.get(api)  # open url in browser
    browser.find_element_by_xpath('//*[@id="action-button"]').click()  # click on "send message" button

    # wait till the text box is loaded onto the screen
    try:
        element_present = ec.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer'
                                                                    '/div[1]/div[2]/div/div[2]'))
        WebDriverWait(browser, 10000).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")

    # type out and send the full message
    browser.find_element_by_xpath(
        '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]'
    ).send_keys(final)

    time.sleep(3)  # just so that we can supervise, otherwise it's too fast


if __name__ == "__main__":
    # read all entries to send message to
    excel = pd.read_excel("Tests.xlsx")
    numbers = excel['Number'].tolist()
    names = excel['Name'].tolist()

    # create a browser instance, login to whatsapp (one time per run)
    webbrowser = webdriver.Firefox(executable_path='geckodriver.exe')
    webbrowser.get('https://web.whatsapp.com/')
    input('\npress enter when whatsapp login is done\n')

    # send messages to all entries in file
    for num, name in zip(numbers, names):
        sendMessage(num, name, webbrowser)

    webbrowser.close()  # close browser
