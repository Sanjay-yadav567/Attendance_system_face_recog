from tkinter import*
from tkinter import ttk
from winsound import MessageBeep
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognization System")

    # ++++========Top img =====++++++
        img_top=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\devlop.jpg")
        img_top=img_top.resize((1366,130),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1366,height=130)

    # ++++++++=======Down Img======+++++
        img_bottom=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\dev.jpg")
        img_bottom=img_bottom.resize((1366,600),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=132,width=1366,height=600)

    #Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=500,y=0,width=400,height=500)

        img_frame=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\logodev.png")
        img_frame=img_frame.resize((200,200),Image.ANTIALIAS)
        self.photoimg_frame=ImageTk.PhotoImage(img_frame)

        f_lbl=Label(main_frame,image=self.photoimg_frame)
        f_lbl.place(x=300,y=0,width=200,height=200)

    #Devloper info
        dev_label=Label(main_frame,text="Hello I AM SANJAY",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I AM DEVELOPER",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        img_bottom=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\dev.jpg")
        img_bottom=img_bottom.resize((1366,600),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=132,width=1366,height=600)






if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()