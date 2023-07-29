from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from dotenv import load_dotenv

load_dotenv()

import mysql.connector as sql
mycon=sql.connect(host='localhost',user=os.getenv('user'),passwd=os.getenv('password'),charset='utf8',database='Drivers')
cursor=mycon.cursor()

class Drivers:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Driver Management System")

        self.var_name=StringVar()
        self.var_phone=StringVar()
        self.var_id_type=StringVar()
        self.var_id_proof=StringVar()
        self.var_salary=StringVar()
        self.var_type=StringVar()
        self.var_vname=StringVar()
        self.var_vno=StringVar()
        self.var_dl=StringVar()

        lbl_title=Label(self.root, text="DRIVER MANAGEMENT SYSTEM", font=("Times New Roman",37,"bold"),fg="darkblue",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)

        img_logo=Image.open('logo.png')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        img_frame=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        img_frame.place(x=0,y=60,width=1530,height=250)

        auto_img=Image.open('auto.jpg')
        auto_img=auto_img.resize((500,250),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(auto_img)
        self.img1=Label(img_frame,image=self.photo1)
        self.img1.place(x=0,y=0,width=540,height=250)

        bike_img=Image.open('bike.jpg')
        bike_img=bike_img.resize((500,250),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(bike_img)
        self.img2=Label(img_frame,image=self.photo2)
        self.img2.place(x=510,y=0,width=540,height=250)

        taxi_img=Image.open('taxi.png')
        taxi_img=taxi_img.resize((500,250),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(taxi_img)
        self.img3=Label(img_frame,image=self.photo3)
        self.img3.place(x=1020,y=0,width=540,height=250)

        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=10,y=310,width=1510,height=510)

        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Driver Information",font=("Times New Roman",11,"bold"),fg="Red")
        upper_frame.place(x=10,y=10,width=1480,height=200)

        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Driver Information Table",font=("Times New Roman",11,"bold"),fg="Red")
        down_frame.place(x=10,y=210,width=1480,height=260)

        # name:
        lbl_name=Label(upper_frame,text="Name",font=("Times New Roman",11,"bold"),bg="white")
        lbl_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("Arial",11))
        txt_name.grid(row=0,column=3,padx=5,pady=7)
        # phone-no:
        lbl_phone=Label(upper_frame,text="Contact",font=("Times New Roman",11,"bold"),bg="white")
        lbl_phone.grid(row=1,column=2,padx=5,pady=7,sticky=W)
        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("Arial",11))
        txt_phone.grid(row=1,column=3,padx=5,pady=7)
        # id-proof:
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_id_type,state="readonly",font=("Times New Roman",11,"bold"),width=18)
        com_txt_proof['value']=("Select ID-Proof","PAN Card","Aadhar Card")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=2,column=2,padx=5,pady=7)
        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_id_proof,width=22,font=("Arial",11))
        txt_phone.grid(row=2,column=3,padx=5,pady=7)
        # salary:
        lbl_salary=Label(upper_frame,text="Salary",font=("Times New Roman",11,"bold"),bg="white")
        lbl_salary.grid(row=3,column=2,padx=5,pady=7,sticky=W)
        txt_salary=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("Arial",11))
        txt_salary.grid(row=3,column=3,padx=5,pady=7)
        # type:
        com_txt_type=ttk.Combobox(upper_frame,textvariable=self.var_type,state="readonly",font=("Times New Roman",11,"bold"),width=18)
        com_txt_type['value']=("Vehicle Type","Bike","Auto","Mini Car","SUV","Sedan")
        com_txt_type.current(0)
        com_txt_type.grid(row=0,column=5,padx=50,pady=7)
        # vehicle name:
        lbl_vname=Label(upper_frame,text="Vehicle Name",font=("Times New Roman",11,"bold"),bg="white")
        lbl_vname.grid(row=1,column=5,padx=50,pady=7,sticky=W)
        txt_vname=ttk.Entry(upper_frame,textvariable=self.var_vname,width=22,font=("Arial",11))
        txt_vname.grid(row=1,column=6,padx=5,pady=7)
        # vehicle number:
        lbl_vno=Label(upper_frame,text="Vehicle No.",font=("Times New Roman",11,"bold"),bg="white")
        lbl_vno.grid(row=2,column=5,padx=50,pady=7,sticky=W)
        txt_vno=ttk.Entry(upper_frame,textvariable=self.var_vno,width=22,font=("Arial",11))
        txt_vno.grid(row=2,column=6,padx=5,pady=7)
        # driving licence:
        lbl_dl=Label(upper_frame,text="Driving Licence No.",font=("Times New Roman",11,"bold"),bg="white")
        lbl_dl.grid(row=3,column=5,padx=50,pady=7,sticky=W)
        txt_dl=ttk.Entry(upper_frame,textvariable=self.var_dl,width=22,font=("Arial",11))
        txt_dl.grid(row=3,column=6,padx=5,pady=7)

        btn_frame=Frame(upper_frame,relief=RIDGE,bg="white")
        btn_frame.place(x=1250,y=-5,width=170,height=180)

        btn_add=Button(btn_frame,text="Save",command=self.add_data,font=("Arial",15,"bold"),width=13,bg="light blue")
        btn_add.grid(row=0,column=0,padx=1)
        btn_upd=Button(btn_frame,text="Update",command=self.update_data,font=("Arial",15,"bold"),width=13,bg="light blue")
        btn_upd.grid(row=1,column=0,padx=1)
        btn_del=Button(btn_frame,text="Delete",command=self.delete_data,font=("Arial",15,"bold"),width=13,bg="light blue")
        btn_del.grid(row=2,column=0,padx=1)
        btn_clr=Button(btn_frame,text="Clear",command=self.reset_data,font=("Arial",15,"bold"),width=13,bg="light blue")
        btn_clr.grid(row=3,column=0,padx=1)

        search_frame=LabelFrame(down_frame,relief=RIDGE,bg="white",bd=0)
        search_frame.place(x=0,y=5,width=1475,height=60)
        search_by=Label(search_frame,font=("Arial",11,"bold"),text="Search by",fg="black",bg="light blue")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        self.var_com_search=StringVar()
        com_text_search=ttk.Combobox(search_frame,state="readonly",textvariable=self.var_com_search,font=("Times New Roman",11,"bold"),width=14)
        com_text_search['value']=("Select option","ID_No","Name")
        com_text_search.current(0)
        com_text_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("Arial",11))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,command=self.search_data,text="search",font=("Arial",11,"bold"),width=14,bg="light blue")
        btn_search.grid(row=0,column=3,padx=5)

        btn_show=Button(search_frame,command=self.fetch_data,text="show all",font=("Arial",11,"bold"),width=14,bg="light blue")
        btn_show.grid(row=0,column=4,padx=5)

        tabel_frame=Frame(down_frame,bd=2,relief=RIDGE,bg="white")
        tabel_frame.place(x=10,y=50,width=1460,height=185)

        scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        self.driver_table=ttk.Treeview(tabel_frame,column=("name","phone","id-type","id-proof","salary","v-type","v-name","vno","dl"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.driver_table.xview)       
        scroll_y.config(command=self.driver_table.yview)

        self.driver_table.heading("name",text="NAME")
        self.driver_table.heading("phone",text="PHONE")
        self.driver_table.heading("id-type",text="ID-TYPE")
        self.driver_table.heading("id-proof",text="ID-PROOF")
        self.driver_table.heading("salary",text="SALARY")
        self.driver_table.heading("v-type",text="V-TYPE")
        self.driver_table.heading("v-name",text="V-NAME")
        self.driver_table.heading("vno",text="V-NO.")
        self.driver_table.heading("dl",text="DRIVING LICENCE")
        self.driver_table['show']='headings'
        self.driver_table.column("name",width=100)
        self.driver_table.column("phone",width=100)
        self.driver_table.column("id-type",width=100)
        self.driver_table.column("id-proof",width=100)
        self.driver_table.column("salary",width=100)
        self.driver_table.column("v-type",width=100)
        self.driver_table.column("v-name",width=100)
        self.driver_table.column("vno",width=100)
        self.driver_table.column("dl",width=100)

        self.driver_table.pack(fill=BOTH,expand=1)

        self.driver_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    def add_data(self):
        if self.var_name.get()=="" or self.var_phone.get()=="" or self.var_dl.get()=="":
            messagebox.showerror("Error","Please enter all the required fields!!!")
        else:
            try:
                cursor.execute("insert into drivers_details values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(self.var_name.get(),self.var_phone.get(),self.var_id_type.get(),self.var_id_proof.get(),self.var_salary.get(),self.var_type.get(),self.var_vname.get(),self.var_vno.get(),self.var_dl.get()))
                mycon.commit()
                self.fetch_data()
                messagebox.showinfo("Success","Driver details added successfully!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f'Due to: {str(es)}',parent=self.root)

    def fetch_data(self):
        cursor.execute("select * from drivers_details")
        data=cursor.fetchall()
        if data!=[]:
            self.driver_table.delete(*self.driver_table.get_children())
            for i in data:
                self.driver_table.insert("",END,values=i)
            mycon.commit()
    
    def get_cursor(self, event=""):
        cursor_row=self.driver_table.focus()
        content=self.driver_table.item(cursor_row)
        data=content['values']

        self.var_name.set(data[0])
        self.var_phone.set(data[1])
        self.var_id_type.set(data[2])
        self.var_id_proof.set(data[3])
        self.var_salary.set(data[4])
        self.var_type.set(data[5])
        self.var_vname.set(data[6])
        self.var_vno.set(data[7])
        self.var_dl.set(data[8])

    def update_data(self):
        if self.var_name=="" or self.var_phone=="" or self.var_dl=="":
            messagebox.showerror("Errot","All fields are required!!!")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure for updation?")
                if update:
                    cursor.execute("update drivers_details set Name='{}',Phone='{}',ID_Type='{}',ID_No='{}',Salary='{}',V_Type='{}',V_Name='{}',V_No='{}',DL='{}' where ID_No='{}'".format(self.var_name.get(),self.var_phone.get(),self.var_id_type.get(),self.var_id_proof.get(),self.var_salary.get(),self.var_type.get(),self.var_vname.get(),self.var_vno.get(),self.var_dl.get(),self.var_id_proof.get()))
                else:
                    if not update:
                        return
                mycon.commit()
                self.fetch_data()
            except Exception as es:
                messagebox.showerror("Error",f'Due to: {str(es)}',parent=self.root)

    def delete_data(self):
        if self.var_id_proof=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure you want to delete selected data?")
                if delete:
                    q="delete from drivers_details where ID_No='{}'".format(self.var_id_proof.get())
                    cursor.execute(q)
                else:
                    if not delete:
                        return
                mycon.commit()
                self.fetch_data()
                messagebox.showinfo("Delete","Driver details deleted successfully!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f'Due to: {str(es)}',parent=self.root)
    
    def reset_data(self):
        self.var_name.set("")
        self.var_phone.set("")
        self.var_id_type.set("Select ID-Proof")
        self.var_id_proof.set("")
        self.var_salary.set("")
        self.var_type.set("Vehicle Type")
        self.var_vname.set("")
        self.var_vno.set("")
        self.var_dl.set("")

    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Error please select option")
        else:
            try:
                cursor.execute("select * from drivers_details where "+str(self.var_com_search.get())+" like '%"+str(self.var_search.get())+"%'")
                rows=cursor.fetchall()
                if rows!=[]:
                    self.driver_table.delete(*self.driver_table.get_children())
                    for i in rows:
                        self.driver_table.insert("",END,values=i)
                    mycon.commit()
            except Exception as es:
                messagebox.showerror("Error",f'Due to: {str(es)}',parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Drivers(root)
    root.mainloop()