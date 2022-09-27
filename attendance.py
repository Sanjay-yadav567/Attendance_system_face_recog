from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognization System")

        #==========TExt Variables======================
        self.var_Atten_id=StringVar()
        self.var_Atten_roll=StringVar()
        self.var_Atten_name=StringVar()
        self.var_Atten_dep=StringVar()
        self.var_Atten_time=StringVar()
        self.var_Atten_date=StringVar()
        self.var_Atten_attendance=StringVar()

    # first image
        img=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\Attenddetail.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1366,height=130)

    #Background image
        img2=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\bhimg2.jpg")
        img2=img2.resize((1366,768),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img=Label(self.root,image=self.photoimg2)
        bg_img.place(x=0 ,y=130,width=1366,height=600)

        main_frame=Frame(bg_img,bd=2,bg="DarkSeaGreen1")
        main_frame.place(x=6,y=10,width=1349,height=560)

    #left side label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance",font=("times new roman",12,"bold"))
        Left_frame.place(x=8,y=10,width=660,height=540)

        img_left=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\stdatt.jpg")
        img_left=img_left.resize((650,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=4,y=0,width=650,height=100)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=4,y=105,width=650,height=410)

    #label Entry
        #Attendance ID
        attendanceID_label=Label(left_inside_frame,text="AttendanceID :",bg="white",font=("times new roman",12,"bold"))
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_id,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Roll
        rollLabel=Label(left_inside_frame,text="Roll :",bg="white",font=("times new roman",12,"bold"))
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)

        #Name
        nameLabel=Label(left_inside_frame,text="Name :",bg="white",font=("times new roman",12,"bold"))
        nameLabel.grid(row=1,column=0)
 
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,pady=8)

        #Department
        depLabel=Label(left_inside_frame,text="Department :",bg="white",font=("times new roman",12,"bold"))
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)

        #Time
        timeLabel=Label(left_inside_frame,text="Time :",bg="white",font=("times new roman",12,"bold"))
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,pady=8)

        #Date
        dateLabel=Label(left_inside_frame,text="Date :",bg="white",font=("times new roman",12,"bold"))
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_Atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,pady=8)

        #Attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status :",bg="white",font=("times new roman",12,"bold"))
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),width=18,textvariable=self.var_Atten_attendance,state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=645,height=37)#-----------Yahabn change karna hai----------

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


    #Right side label frame 
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance List",font=("times new roman",12,"bold"))
        Right_frame.place(x=675,y=10,width=660,height=540)

        img_right=Image.open(r"C:\Users\HRYADAV\Desktop\attendence system\images\stdatt.jpg")
        img_right=img_right.resize((650,100),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=4,y=0,width=650,height=100)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=4,y=105,width=650,height=410)

        #===========scroll bar table================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


        # ====================Fetch data==============
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #Export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        
        except Exception as es:
            messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #======Get Curser +++++============
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_Atten_id.set(rows[0])
        self.var_Atten_roll.set(rows[1])
        self.var_Atten_name.set(rows[2])
        self.var_Atten_dep.set(rows[3])
        self.var_Atten_time.set(rows[4])
        self.var_Atten_date.set(rows[5])
        self.var_Atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_Atten_id.set("")
        self.var_Atten_roll.set("")
        self.var_Atten_name.set("")
        self.var_Atten_dep.set("")
        self.var_Atten_time.set("")
        self.var_Atten_date.set("")
        self.var_Atten_attendance.set("")




if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()