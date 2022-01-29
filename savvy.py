import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit as pwt
import pywhatkit
import pyjokes
import operator
from playsound import playsound
from turtle import *



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
# setter method .[0]=male voice and 
# [1]=female voice in set Property.
engine.setProperty('voice', voices[0].id)



def speak(audio):
    # Method for the speaking of the the assistan
    engine.say(audio)
    engine.runAndWait()

def wishme():
    # Method for the wishing of the the assistant
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("good evening sir")
    speak("i am savvy.I am created by Mr Tushar and Aditya Please tell me how may i help you ")
def takecommand():
# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
#it takes microphone input from user and return the string output
    r=sr.Recognizer()
    # from the speech_Recognition module 
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        # seconds of non-speaking audio before 
        # a phrase is considered complete
        print("Listening...")
        r.pause_threshold=1 #if we takes 1 sec gape it doesnt complete the sentence
        audio=r.listen(source)
    # Now we will be using the try and catch
    # method so that if sound is recognized 
    # it is good else we will have exception 
    # handling
    try:
        print("Recognizing...")
        # for Listening the command in indian
        # english we can also use 'hi-In' 
        # for hindi recognizing
        query=r.recognize_google(audio, language='en-IN')
        print(f"user said: {query}\\n")

    except Exception as e:
        # print(e)

        print("Say that again please....")
        return "none"
    return query


if __name__ == "__main__":
    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate 
    # the program
    wishme()
    while True:
        query = takecommand().lower()

        # logic for executing task based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=1)
            speak("Accoroding to wikipedia")
            print(results)
            speak(results)
        # executing Websites.
        # in the open method we just to give the link
         # of the website and it automatically open 
         # it in your default browser
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open lpu live' in query:
            webbrowser.open('https://lpulive.lpu.in/')
        elif 'open my class' in query:
            webbrowser.open('https://myclass.lpu.in/')
        elif 'open u m s' in query:
            webbrowser.open('https://ums.lpu.in/lpuums/')
        elif 'open s q l' in query:
            webbrowser.open('http://127.0.0.1:8080/apex/f?p=4500:1000:179658696921669')
        # elif 'play' in query:
        #     song=query.replace("play", "")
        #     pywhatkit.playonyt(song)
        elif 'time' in query:
            time=datetime.datetime.now().strftime('%I %M %p')
            print(time)
            speak("current time is:" + time)
        
        #executing apps

        elif 'open code' in query:
            codePath="C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open spider' in query:
            codePath="C:\\Users\\tusha\\anaconda3\\Scripts\\spyder-script.py"
            os.startfile(codePath)
        elif 'open sublime text' in query:
            codePath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)
        elif 'open telegram' in query:
            codePath="C:\\Users\\tusha\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(codePath)
        elif 'open spotify' in query:
            codePath="C:\\Users\\tusha\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
        
        #searching in google
        elif 'search' in query:
            result=query.replace('searching','')
            speak("sir, as you searched")
            pwt.search(result)
        
        #playing video in youtube
        elif 'play' in query:
            video=query.replace('playing video','')
            speak("As Your Said to play")
            pywhatkit.playonyt(video)
        
        #jokes
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        #calculator
        elif 'do some calculation' in query or 'can you calculate' in query:
            r=sr.Recognizer()
            with sr.Microphone() as source:
                speak("Sir please say waht you want to calculate, example: 3 plus 3")
                print("listening.....")
                r.adjust_for_ambient_noise(source)
                r.pause_threshold=1 #if we takes 1 sec gape it doesnt complete the sentence
                audio=r.listen(source)
            my_string=r.recognize_google(audio, language='en-IN')
            print(my_string)

            #definig operator
            def get_operator_fn(op):
                return{
                    '+' : operator.add, #plus
                    '-' : operator.sub, #miinus
                    'x' : operator.mul, #multiplied
                    'divided' : operator.__truediv__, #devide
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2= int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("your result is")
            speak(eval_binary_expr(*(my_string.split())))
            print(eval_binary_expr(*(my_string.split())))

        #make jarvis remember something
        elif 'remember that' in query:
            rememberMsg=query.replace("remember that",' ')
            rememberMsg=rememberMsg.replace("savvy", ' ')
            speak("you tell me to remind you that: "+rememberMsg)
            remember=open('remember.txt','w')
            remember.write(rememberMsg)
            remember.close()

                
            
        #savvy reminding you
        elif 'did i told you to remember something' in query or 'do you remember what i told you' in query:
            remember=open('remember.txt','r')
            speak("you told me that" + remember.read())
        
        #alarm
        elif'alarm' in query:
            speak("enter the time!")
            time=input(": Enter the time :")
            
            while True:
                time_now= datetime.datetime.now()
                now=time_now.strftime("%H:%M:%S")

                if now==time:
                    speak("time to wake up sir!")
                    playsound('iron-Man.mp3')
                    speak("alarm closed!")
                elif now>time:
                    break
        
        
        
        elif 'shutdown' in query:
            speak("on your command sir, system will be shutdown in 20 second")
            pwt.shutdown(time=20)
        elif 'cancel shutdown' in query:
            speak("sir as commanded, shutdown process is terminated")
            pwt.cancel_shutdown()
        
        #exit
        elif 'quit' in query or 'exit' in query:
            speak("Ok sir it was pleasure serving you")
            exit()

        
       

