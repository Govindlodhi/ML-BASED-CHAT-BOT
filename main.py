from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine=pp.init()   #install pyttsx3 for Text to Speech
voices=engine.getProperty('voices')
print(voices)

engine.setProperty('voice',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot=ChatBot("mybot")
convo = [
    "Hello",
    "Hi there!",
    "your name",
    "my name is AI bot",
    "who devloped you",
    "i have devloped govind lodhi",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "mobile no",'mo no','phone no',
    "89 59 39 96 95",
    "where are you from",
    "i am from bhopal",
    "your address",
    "i did not show our adderess",
    "your collage name ",
    "lnct collage of bhopal",
    "collage mo no.",
    "977774455",
    "home mobile no",
    "56782314223"

]
trainer = ListTrainer(bot)
trainer.train(convo)
"""
print("talk to bot")
while True:
    query=input()
    if query=='exit':
        break
    answer=bot.get_response(query)
    print("bot= ",answer)
"""
main=Tk()
main.geometry("400x550")
main.title("MY Chatbot")
img=PhotoImage(file="chatimg.png")
photola=Label(main,image=img)
photola.pack(pady=5)


#import chatter vot


#take query : it take audio as input from user and convert it to string
def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
       try:
           audio = sr.listen(m)
           query = sr.recognize_google(audio, language='eng-in')
           print(query)
           textF.delete(0, END)
           textF.insert(0, END)
           ask_from_bot()
       except Exception as e:
           print(e)
           print("not recognized")

#ask from bot
def ask_from_bot():
    query=textF.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,"you:  "+query)
    msgs.insert(END,"bot: "+ str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)


main.configure(background="light green")
#frameobject
frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set,bg="pink")
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

#/creating text field
textF=Entry(main,font=("vardana",20),bg='light blue',justify='center')
textF.pack(fill=X,pady=10,padx=10)

#butten
btn=Button(main,text="ask from bot",font='vardana 10 bold italic underline', \
           bg='sky blue',borderwidth=3,relief=GROOVE, activebackground='gray',\
           activeforeground='silver',command=ask_from_bot,pady=10)
btn.pack()

#creating a function;
def enter_function(event):
    btn.invoke()

#going to bind main window with enter key
main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()

t=threading.Thread(target=repeatL)
t.start()

main.mainloop()