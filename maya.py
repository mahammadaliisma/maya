###### Maya ######
# Speech Assistant #

import speech_recognition as sr  # recognise speech
import pyttsx3 # text to Speech (TTS)
import pywhatkit # for advance control on browser
import playsound  # to play an audio file
import pyjokes # for jokes
import datetime # for datetime
import wikipedia # searching on wikipedia
import webbrowser # open browser
import pyautogui  # screenshot
from gtts import gTTS  # google text to speech
import random
import re

listener = sr.Recognizer() # initialise a recogniser
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # changing index, changes voices. o for male, 1 for female


def talk(text):
    engine.say(text)
    text = str(text)
    tts = gTTS(text=text, lang='en')  # text to speech(voice)
    r = random.randint(1, 20)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source: # microphone as source
            print('listening...')
            voice = listener.listen(source) # listen for the audio via source
            command = listener.recognize_google(voice) # convert voice to text
            command = command.lower()
            if 'maya' in command:
                command = command.replace('maya', '')
    except:
        talk('I think there is nobody here')
    return command

# greeting
talk('Hello, my name is Maya. How can I help you?')
def run_maya():
    command = take_command()
    print(command)

    # Hi Maya. My name is Mahammadali.
    if 'my name is' in command:
        name = re.sub('[ ]*[hi|hello|hey]*[ ]*my[ ]*name[ ]*is[ ]*', '', command)
        talk("Nice to meet you" + name + "How are you?")

    elif "how are you" in command:
        talk("Thanks I'm great")

    # my friend is here Ali
    elif 'here' in command:
        friend_name = command.replace('my friend is here', '')
        talk("Nice to meet you" + friend_name + "How are you?")

    # searching on google
    elif 'search' in command:
        something = command.replace('search','')
        talk('searching' + something)
        url = ('https://www.google.com/search?q=' + something)
        webbrowser.get().open(url)
        talk("Here is what I found for" + something + "on google")

    # searching on wikipedia
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    # playing video on youtube
    elif 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    # what time is it now?
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)

    # are you single?
    elif 'single' in command:
        talk("Hahahah. I am in relationship with wifi")

    # will you marry me?
    elif 'marry' in command:
        talk('oh my god yes yes yes yes yes my honey')

    # I'm looking for a girlfriend so
    elif 'looking' in command:
        talk("Oh no. Don't even think about it")

    # I have crush on you
    elif 'crush' in command:
        talk('Shut up')

    # tell me a joke
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    # screenshot
    elif 'screenshot' in command:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('screen.png')

    # bye-bye
    elif 'bye-bye' in command:
        talk('bye-bye')
        exit()
    else:
        talk("I didn't understand you")

while True:
    run_maya()
    talk("tell me something please")