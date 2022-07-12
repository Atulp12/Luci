import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from tkinter import *  
import subprocess
import pyjokes
import wolframalpha
# from ecapture import ecapture as ec

 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)          

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")
    
    speak("I am Luci..")


       
def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try :
        print("Recognizing..")
        query = r.recognize_google(audio,language = 'en-in')
        print("User said : ",query)
    except Exception as e:
        #print(e)
        print("Please , say it again... ")
        return "none"
    return query

def username():
    speak("What should i call you sir")
    uname = takecommand()
    speak("Welcome..")
    speak(uname)
    speak("How can i Help you, Sir")
    
    
# def Processing_Audio():
if __name__ == "__main__":   
     wishme()
     username()
     while True:
       query = takecommand().lower()
        
        
              
       if 'wikipedia' in query:
           speak('Searching Wikipedia....')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query,sentences = 2)
           speak("According to wikipedia...")
           speak(results)
           print(results)
           
       elif 'joke' in query:
              speak(pyjokes.get_joke()) 
           
       elif 'open youtube' in query:
           speak('Opening Youtube...')
           webbrowser.open("youtube.com")
           
       elif 'open google' in query:
           speak('Opening google...')
           webbrowser.open("google.com")
        
       elif 'open w3schools' in query:
           speak('Opening w3schools...')
           webbrowser.open("w3schools.com")
           
       elif 'play music' in query:
           music_dir = 'D:\\Songs'
           songs = os.listdir(music_dir)
           #os.startfile(os.path.join(music_dir,songs[0]))
           d=random.choice(songs)
           speak("Playing Music...")
           os.startfile(os.path.join(music_dir,d))
           
       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"The time is..{strTime}")
           
       elif 'open code' in query:
           path = "C:\\Users\\Atul Prajapati\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           speak("Opening Visual studio code...")
           os.startfile(path)
           
       elif 'open chrome' in query:
           path1 = "C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe"  
           speak("Opening google chrome...")
           os.startfile(path1)
        
       elif  'make a note' in query:
                query = query.replace("make a note", "")
                note(query)  
     
       elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            
       
       elif "what is" in query or "who is" in query:
             
            
            client = wolframalpha.Client("XG7G2W-3797PH4YVY")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
         
       elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
       elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
       elif "who made you" in query or "who created you" in query:
            speak("I have been created by Atul.")   
            
       elif "who are you" in query:
            speak("I am your virtual assistant created by Atul") 
       
       
    #    elif "camera" in query or "take a photo" in query:
    #         ec.capture(0, "Luci Camera ", "img.jpg")
   
       elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

            
# def main_screen():

     
#       root = Tk()
#       root.title('Your assistant Luci is Here....')
#       root.geometry("655x744")
#       backimage = PhotoImage("C:\\Users\\Atul Prajapati\\Downloads\\v2.png")
#       bi = Label(image=backimage)
#       bi.pack()


#       name_label = Label(text = 'Luci',width = 300, bg = "black", fg="white", font = ("Calibri", 13))
#       name_label.pack()


#       microphone_photo = PhotoImage(file = "C:\\Users\\Atul Prajapati\\Downloads\\v3.png")
#       microphone_button = Button(image=microphone_photo, command = Processing_Audio)
#       microphone_button.pack(pady=10)


#       root.mainloop()

# main_screen()