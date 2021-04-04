#db : blood
#tables: donor ,receiver ,update_blood,login
from tkinter import *
from donor_page import *
from patient_page import *
from admin_page import *
import pymysql
d=pymysql.connect(host='localhost',user='root',password='rooot',database='blood')
##c=d.cursor()
##table1='create table donor(name varchar(20),age varchar(2),gender varchar(10),phone varchar(20),address varchar(80),blood_group varchar(10),messurement varchar(3),date date)'
##c.execute(table1)
##table2='create table login(uname varchar(20),password varchar(20))'
##c.execute(table2)
##table3='create table receiver(name varchar(20),age varchar(2),gender varchar(10),phone varchar(20),address varchar(80),blood_group varchar(10),messurement varchar(3),date date)'
##c.execute(table3)
##table4='create table update_blood(ap int,am int,bp int,bm int,op int,om int,abp int,abm int)'
##c.execute(table4)
t=Tk()
t.title('Blood Donation Management System')
t.geometry('600x500+100+100')
t.resizable(0,0)
t.wm_iconbitmap('life.ico')
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
