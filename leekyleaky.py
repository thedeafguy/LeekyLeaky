# This unofficial tool serves as standard HIBP search (no API key needed)
# Author: Sira
# ChromeDriver is required, download here: https://chromedriver.chromium.org/. Dont't forget to add it to system's PATH

import sys
import os.path
import json
import requests
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def driver():
    global driver
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_opt)
    driver.set_window_position(-10000,0)

def pasteExists(urlAdd):
    r = requests.get(urlAdd)
    if r.status_code == 200:
        return True
    else:
        return False

def checkAddress(email):
    Url = 'https://haveibeenpwned.com/unifiedsearch/' + email
    driver.get(Url)
    try:
        driver.find_element_by_xpath('html/body/pre')
    except NoSuchElementException:
        if "--only_valid" not in sys.argv:
            print("No breaches have been found for " + email + "!")
    else:
        print("\n==Results for " + email + "==")
        array = json.loads(driver.find_element_by_xpath('html/body/pre').text)
        if array["Breaches"] is not None:
            for i in range(len(array["Breaches"])):
                print("Title: " + array["Breaches"][i]["Title"])
                print("-Date: " + array["Breaches"][i]["BreachDate"])
        if array["Pastes"] is not None:
            print("\nSearching for pastes that are up...")
            for j in range(len(array["Pastes"])):
                pastes = array["Pastes"][j]["Id"]
                if pastes.startswith("https://"):
                    if pasteExists(pastes):
                        print("Paste: " + pastes)
                else:
                    binUrl = "https://pastebin.com/raw/" + pastes
                    if pasteExists(binUrl):
                        print(binUrl)
        print("\n==End of results for " + email + "==")
    sleep(2) # Prevents ratelimiting ban

def readLinesInFile(fileemails):
    fileMails = open(fileemails, 'r')
    MailsLines = fileMails.readlines()
    for line in MailsLines:
        checkAddress(line.strip())

def main():
    if len(sys.argv)-1 == 0:
        print("Error: No files nor e-mail addresses have been specified.\n\nUsage:\t leekyleaky.py <path to file with e-mail address inside/e-mail address>\nExample: leekyleaky.py example@example.org example.txt\nArguments:  --only_valid - outputs non-empty reults only\n\nYou can specify as many paths or addresses as you like.\nNOTE: To prevent ratelimit ban, there's a two-second pause after each e-mail.")
    else:
        driver()
        for i in range(1, len(sys.argv)):
            if os.path.isfile(sys.argv[i]):
                readLinesInFile(sys.argv[i])
            else:
                checkAddress(sys.argv[i])
        driver.close()

if __name__ == "__main__":
    main()