from tkinter import *
from donar_page import *
import pymysql
d=pymysql.connect(host='localhost',user='root',password='rooot',database='blood')
t=Tk()
t.title('Blood Donation Management System')
t.geometry('600x500+100+100')
t.resizable(0,0)
t['bg']='light blue'
l=Label(text='Blood Bank Management System',relief=SOLID,font=('times new roman',30),fg='black')
l.pack(padx=5,pady=30)
b1=Button(t,text=' Donor Reg.Form ',command=donar,width=20,font=('ariel',15,'bold'),fg='white',bg='black')
b1.pack(padx=10,pady=20)
b2=Button(t,text='ADMIN',width=20,font=('ariel',15,'bold'),fg='white',bg='black')
b2.pack(padx=10,pady=20)
b3=Button(t,text='Patient Reg.Form',width=20,font=('ariel',15,'bold'),fg='white',bg='black')
b3.pack(padx=10,pady=20)

t.mainloop()
