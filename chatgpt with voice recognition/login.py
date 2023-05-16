from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from chatgpt import speak
from register import Register
import mysql.connector
import os
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

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file="C:/Users/pcmwa/OneDrive/Desktop/facee/Python-FYP-Face-Recognition-Attendence-System/Images_GUI/log.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=560,y=170,width=340,height=450)

        img1=Image.open("C:/Users/pcmwa/OneDrive/Desktop/facee/Python-FYP-Face-Recognition-Attendence-System/Images_GUI/log.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=140,y=100)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=90,y=370,width=50,height=20)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcoem to chatbot")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='ayush',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=ChatBot(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='ayush',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='ayush',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# =====================main program Face detection system====================

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("ChatBot")


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

    
    speak("Hi I am your chatbot. I will open a login window you can login and start asking anything. If possible I will answer your queries") 
   
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)

        main_frame=Frame(self.root,bd=4,bg='black',width=610)
        main_frame.pack()

        img_chat=Image.open("C:/Users/pcmwa/Downloads/project mca/image-of-hand-holding-an-ai-face-looking-at-the-words-chatgpt-openai.webp")
        img_chat=img_chat.resize((800,100),Image.ANTIALIAS)
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

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('areal',15,'bold'),width=8,bg='black',fg='white')
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
    
    
    
  




if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()