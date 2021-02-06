from tkinter import *
from donor_page import *
from patient_page import *
from admin_page import *
import pymysql
d=pymysql.connect(host='localhost',user='root',password='rooot',database='blood')
t=Tk()
t.title('Blood Donation Management System')
t.geometry('600x500+100+100')
t.resizable(0,0)
t['bg']='steelblue4'
l=Label(text='Blood Bank Management System',relief=SOLID,font=('times new roman',30),fg='black')
l.pack(padx=5,pady=30)
b1=Button(t,text='ADMIN',command=admin,width=20,font=('ariel',15,'bold'),relief=SUNKEN,bd=10,fg='white',bg='black')
b1.pack(padx=10,pady=20)
b2=Button(t,text=' Donor Reg.Form ',command=donor,width=20,font=('ariel',15,'bold'),relief=SUNKEN,bd=10,fg='white',bg='black')
b2.pack(padx=10,pady=20)
b3=Button(t,text='Patient Reg.Form',command=patient,width=20,font=('ariel',15,'bold'),relief=SUNKEN,bd=10,fg='white',bg='black')
b3.pack(padx=10,pady=20)
t.mainloop()
