from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hi I am your chatbot. I will open a new window you can ask anything. If possible I will answer your queries")   


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open("C:/Users/pcmwa/Downloads/project mca/ChatGPT-preview.jpg")
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,image=self.photoimg,text="Chat Gpt",font=('areal',30,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=20,relief=RAISED,font=('areal',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=("areal",14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=1,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('areal',15,'bold'),width=8,bg='green',)
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clare=Button(btn_frame,text="Clear Data",command=self.clear,font=('areal',15,'bold'),width=8,bg='red',fg='white')
        self.clare.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('areal',14,'bold'),fg='red',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)

#function for chatgpt

#enter wala function
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
 
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')
    

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END) #scroll automatically

        if (self.entry.get()==''):
            speak("please enter some input")
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')

        if (self.entry.get()=='hello'):
            speak("hi")
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif (self.entry.get()=='hi'):
            speak("hello")
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif (self.entry.get()=='how are you'):
            speak("i am good and what about you")
            self.text.insert(END,'\n\n'+'Bot: i am good and what about you')
            

        elif (self.entry.get()=='fine'):
            speak("Nice to hear that")
            self.text.insert(END,'\n\n'+'Bot: Nice to hear that')
        
        elif (self.entry.get()=='who created you'):
            speak("Ayuhs yadav Systummm")
            self.text.insert(END,'\n\n'+'Bot: Ayush yadav')

        elif (self.entry.get()=='What is your name'):
            speak("my name is chandu chatgpt ka londa")
            self.text.insert(END,'\n\n'+'Bot: my name is chandu chatgpt ka londa')

        elif (self.entry.get()=='open google'):
            speak("opening")
            webbrowser.open("google.com")
        
        elif (self.entry.get()=='open youtube'):
            speak("opening")
            webbrowser.open("youtube.com")
        
        else:
            speak("I dont understand that but I can learn just change my queries. I am still in learning phase")
            self.text.insert(END,'\n\n'+'Bot: I dont understand that but I can learn just change my queries. I am still in learning phase')

        


        

        


if __name__ == '__main__':
    wishMe()
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()

