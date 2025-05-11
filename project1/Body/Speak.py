#  Speak Function -Two Speak Function

# Windows Based & Chrome Based


# Windows Based

import pyttsx3

def Speak(Text):
    engine = pyttsx3.init("sapi5") # sapi5 windows API to help to speak
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    print("")
    print(f"You: {Text}")
    print("")
    engine.say(Text)
    engine.runAndWait()



# Chrome Based

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

chrome_options= Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "DataBase\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)
driver.maximize_window()

website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by= By.XPATH, value='/html/body/div[4]/div[2]/form/select'))

ButtonSelection.select_by_visible_text('British English / Brian')
# ButtonSelection.select_by_visible_text('Mexican Spanish / Mia')

def Speak(Text):
    lengthOfText = len(str(Text))
    if lengthOfText==0:
        pass
    else:
        print("")
        print(f"AI : {Text}.")
        print("")
        data = str(Text)
        driver.find_element(By.XPATH, value = '/html/body/div[4]/div[2]/form/textarea').send_keys(data)
        driver.find_element(By.XPATH, value = '//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH, value = '/html/body/div[4]/div[2]/form/textarea').clear()

        if lengthOfText >= 30:
            sleep(4)

        elif lengthOfText >= 40:
            sleep(6)

        elif lengthOfText >= 55:
            sleep(8)

        elif lengthOfText >= 70:
            sleep(10)

        elif lengthOfText >= 100:
            sleep(13)

        elif lengthOfText >= 120:
            sleep(14)

        else:
            sleep(2)

# Speak("hi I'm  Jarvis... how are you sir ")





