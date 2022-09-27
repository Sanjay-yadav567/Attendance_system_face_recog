from tkinter import*
from tkinter import ttk
from winsound import MessageBeep
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognization System")

    # ++++========Top img =====++++++
        img_top=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\helpd.jpg")
        img_top=img_top.resize((1366,130),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1366,height=130)

    # ++++++++=======Down Img======+++++
        img_bottom=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\helpbg.png")
        img_bottom=img_bottom.resize((1366,600),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=132,width=1366,height=600)

        dev_label=Label(f_lbl,text="Email: ysanjay567@gmail.com",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=500,y=100)



if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()