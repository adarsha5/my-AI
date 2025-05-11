# Hindi or English - command
# English - reply

# Step - 1


# Step - 2
# Three Function 
# 1 - listen
# 2 - English Translate
# 3 - Connect

import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator # pip install googletrans==3.0.0

#1 - Liste : Hindi or English

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #Listening
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="bn-IN")

    except:
        return ""

    query = str(query).lower()
    return query



# print(Listen())


# 2 - Transtale

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}")
    return data 

# print(TranslationHinToEng("কেমন আছেন"))

# 3 - connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    print(data)
    return data

# print(MicExecution())