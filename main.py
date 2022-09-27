import string
from time import strftime, time
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
 

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognization System")

# first image
        img=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\sas2.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=130)


#Background image
        img3=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\BGIMG.jpg")
        img3=img3.resize((1366,768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0 ,y=130,width=1366,height=600)

#========  Time  ===========
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(bg_img,font=("Arial Black",15,"bold"),bg="medium blue",fg="lawn green")  
        lbl.place(x=5,y=0,width=130,height=50)
        time()


#Student button
        img4=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\Student.jpg")
        img4=img4.resize((160,160),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)  

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor='hand2',bg="green",borderwidth=5)
        b1.place(x=300,y=100,width=150,height=150) 

        b1=Button(bg_img,text="Students Details",command=self.student_details,cursor='hand2',font=("Arial Black",11,"bold"),bg="white",fg="red",borderwidth=5)
        b1.place(x=300,y=220,width=150,height=40)


#Detect face button
        img5=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\facedet.jpg")
        img5=img5.resize((160,160),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor='hand2',command=self.face_data,bg="chocolate1",borderwidth=5)
        b1.place(x=600,y=100,width=150,height=150) 

        b1=Button(bg_img,text="Face Detector",cursor='hand2',command=self.face_data,font=("Arial Black",11,"bold"),bg="white",fg="green3",borderwidth=5)
        b1.place(x=600,y=220,width=150,height=40)


#Attendance button
        img6=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\Attendance.jpg")
        img6=img6.resize((160,160),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor='hand2',command=self.attendance_data,bg="brown1",borderwidth=5)
        b1.place(x=900,y=100,width=150,height=150) 
 
        b1=Button(bg_img,text="Attendance",cursor='hand2',command=self.attendance_data,font=("Arial Black",11,"bold"),bg="white",fg="purple3",borderwidth=5)
        b1.place(x=900,y=220,width=150,height=40)

#down area----------------------

#Train Face button
        img8=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\traindata.png")
        img8=img8.resize((160,160),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor='hand2',command=self.train_data,bg="deep pink",borderwidth=5)
        b1.place(x=300,y=300,width=150,height=150) 

        b1=Button(bg_img,text="Train Data",cursor='hand2',command=self.train_data,font=("Arial Black",11,"bold"),bg="white",fg="sienna2",borderwidth=5)
        b1.place(x=300,y=420,width=150,height=40)


#Photos Face button
        img9=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\photos.jpg")
        img9=img9.resize((160,160),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor='hand2',command=self.open_img,bg="gold2",borderwidth=5)
        b1.place(x=600,y=300,width=150,height=150) 

        b1=Button(bg_img,text="Photos",cursor='hand2',command=self.open_img,font=("Arial Black",11,"bold"),bg="white",fg="SteelBlue3",borderwidth=5)
        b1.place(x=600,y=420,width=150,height=40)



#Exit button
        img11=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\exit.jpg")
        img11=img11.resize((160,160),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor='hand2',command=self.iExit,bg="red",borderwidth=5)
        b1.place(x=900,y=300,width=150,height=150) 

        b1=Button(bg_img,text="Exit",cursor='hand2',command=self.iExit,font=("Arial Black",11,"bold"),bg="white",fg="cyan4",borderwidth=5)
        b1.place(x=900,y=420,width=150,height=40)


# ++++++++======Open Photos button +++++++==========

    def open_img(self):
        os.startfile("data")


#+++=====Function Butons+++====

    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)


# ========Train function button=========
    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)


#+==========face Recognizition ============ 
    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

#+==========Attendance ============ 
    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

#==========Exit button==========
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit > 0:
           self.root.destroy()
        else:
             return
        



if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()