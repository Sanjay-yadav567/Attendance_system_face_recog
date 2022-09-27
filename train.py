from tkinter import*
from tkinter import ttk
# from winsound import MessageBeep
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognization System")

    # ++++========Top img =====++++++
        img_top=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\train_data.png")
        img_top=img_top.resize((1366,130),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1366,height=130)


    # +++++++++====Button========+++++++
        b1=Button(self.root,text="CLICK TO TRAIN DATA",command=self.train_classifier,cursor='hand2',font=("Arial Black",20,"bold"),bg="white",fg="GREEN",borderwidth=5)
        b1.place(x=0,y=131,width=1366,height=45)
   
    # ++++++++=======Down Img======+++++
        img_bottom=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\trainbot.jpg")
        img_bottom=img_bottom.resize((1366,600),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=177,width=1366,height=548)

    def train_classifier(self):
        data_dir=("data")#Data Directry
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')# Gray scale image converting
            imageNp=np.array(img,'uint8')#uint8 is an array data type
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # =======Train the  classifier and save===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed!")



if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()