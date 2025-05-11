#https://github.com/UB-Mannheim/tesseract/wiki
import pyautogui
import pytesseract
from PIL import Image
from time import sleep
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

 
def click_on_anything_using_voice_command():

    # Capture a screenshot of the screen
    screenshot = pyautogui.screenshot()

    # Save the screenshot as an image file
    screenshot.save('screenshot.png')

    # Open the screenshot image using PIL
    image = Image.open('screenshot.png')

    # Perform OCR on the image
    text_data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    from Body.Speak import Speak
    Speak("Speak")
    from Body.Listen import MicExecution
    # Define the target text
    # target_text = MicExecution()
    target_text=input(" Enter : ")
    try:
        # Find the coordinates of the target text in the OCR output
        target_coordinates = []
        for i in range(len(text_data['text'])):
            if target_text.lower() in text_data['text'][i].lower():
                x = text_data['left'][i]
                y = text_data['top'][i]
                target_coordinates.append((x, y))

        # Print the found coordinates
        for item in target_coordinates:
            print("X-coordinate:", item[0])
            print("Y-coordinate:", item[1])
            print()

        # Get the current screen resolution
        screen_width, screen_height = pyautogui.size()

        # Define the target coordinates where you want to click
        target_x = item[0]
        target_y = item[1]
        
        # Move the mouse cursor to the target coordinates
        pyautogui.moveTo(target_x, target_y)

        # Perform a left mouse button click
        pyautogui.click()
        pyautogui.click()
    except:
        print("Not find")


def image_to_txt():
    from Body.Speak import Speak
    image1 = Image.open('motivation.png')
    txt= pytesseract.image_to_string(image1)
    Speak("hello sir")
    print(txt)
    Speak(txt)
    if len(str(txt))>100:
        sleep(40)


# image_to_txt()
while True:
    click_on_anything_using_voice_command()

















