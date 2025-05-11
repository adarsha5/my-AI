
import os
import webbrowser
# import wikipedia
import subprocess
import webbrowser
import http.server
import socketserver
from time import sleep
import keyboard
import pyautogui



def run_php_locally(php_file_path):
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", 8000), handler) as httpd:
        print("Server running at http://localhost/project1/")
        webbrowser.open_new_tab("http://localhost/project1/" + php_file_path)

from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Second")
from Body.Speak import Speak

Speak(">> Starting The Jarvis : Wait For Some Second")

def analog_clock_show():
    run_php_locally('Analog_Clock/index.html')

def time():
    from datetime import datetime
    current_time = datetime.now().strftime('%H:%M:%S')
    print("Current time:", current_time)
    Speak(f"Current time: {current_time}")
    analog_clock_show()

def webcam():
    Speak(">> You can say now")
    while True:
        Data = MicExecution()
        # Data = input("Enter (talk):")
        Data = str(Data)
        Data = Data.lower()
        if 'task' in Data:
            tasks()
            break
        if 'stop' in Data:
            Speak("Ok sir ")
            break
        elif 'time' in Data:
            analog_clock_show()
        else:
            from Brain.AIBrain import ReplyBrain
            Reply = ReplyBrain(Data)
            Speak(Reply)
        sleep(5)
        Speak(">> give me the next command...")

def tasks():
    Speak(">> You can execute the tasks using jarvis ...")
    while True:
        query = MicExecution()
        # query = input("Enter (task): ")
        query = str(query)
        query = query.lower()
        # if 'wikipedia' in query:
        #     Speak("Searching wikipedia")
        #     query= query.replace("wikipedia ","")
        #     results = wikipedia.summary(query,sentences=2)
        #     Speak("Accpording to wikipedia")
        #     print(results)
        #     Speak(results)
        if 'stop' in query:
            Speak("Ok sir ")
            break
        elif 'play death note' in query:
            Speak("opening deth note")
            death_note= 'D:\\deth note'
            movie=os.listdir(death_note)
            # print(songs)
            import random
            os.startfile(os.path.join(death_note,movie[random.randint(0,35)]))
        elif "visit" in query:
            query=query.replace("visit ","")
            if "whatsapp" in query:
                link= f"https://web.whatsapp.com/"
                print (link)
                Speak(f"Visiting {query}")
                webbrowser.open(link)
            else:
                link= f"https://www.{query}.com/"
                print (link)
                Speak(f"Visiting {query}")
                webbrowser.open(link)
        elif 'open'  in query:
            query=query.replace("open ","")
            pyautogui.press('win')
            sleep(1)
            keyboard.write(query)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
            Speak(f"Opening {query}")
        elif 'talk' in query:
                webcam()
                break
        elif 'time' in query:
            time()
        sleep(5)
        Speak(">> give me the next task...")

def MainExecution():
    Speak("Hello Sir")
    while True:
        Data1 = MicExecution()
        # Data1 = input("Satrt Ener :  ")
        Data1 = Data1.lower()
        if 'talk' in Data1:
            Speak("Yes sir... I'm Jarvis , I'm Ready to talk with you Sir.....")
            sleep(2)
            webcam()
            Speak("good bye ....")
            break
        elif 'task' in Data1:
            Speak("Yes sir... I'm Jarvis , I'm Ready to do task for you...")
            sleep(2)
            tasks()
            Speak("good bye ....")
            break
        elif 'stop' in Data1:
            Speak("Ok sir ")
            break
        else:
            Speak("Pleas say again")

def ClapDetect():
    from Features.clap_detection import Tester
    query = Tester()
    if "True-Mic" == query:
        run_php_locally("another1.php")
        print("")
        Speak(">> Clap detected!! >>")
        print("")
        MainExecution()
    else:
        pass



ClapDetect()






































# webcam()
# ClapDetect()
# time()
# MainExecution()
# while True:
#     from Brain.AIBrain import ReplyBrain
#     kk= input("Enter : ")
#     print(ReplyBrain(kk))
# tasks()
# from Brain.AIBrain import ReplyBrain
# abc = ReplyBrain("hi jarvis")
# Speak(abc)


# from clapNewDetection import clapNewDetection
# def clap():
#     if clapNewDetection()==True:
#         run_php_locally("another1.php")
#         print("")
#         Speak(">> Clap detected!! >>")
#         print("")
#         MainExecution()
#     else:
#         pass

# clap()




# analog_clock_show()

