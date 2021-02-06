from tkinter import *
from tkinter import messagebox  as m
import pymysql
from view_update import *

d=pymysql.connect(host='localhost',user='root',password='rooot',db='blood')
c=d.cursor()
def sub(): #subit button actions
    z1=euser.get()
    z2=epass.get()
    c.execute('select * from login ')
    result=c.fetchall()
    for i in result:
        if i[0]==z1:
            if i[1]==z2:
                op=m.askokcancel('info','USER_NAME and PASSWORD are CORRECT\nDo you like to continue')
                if op==0:
                    t1.withdraw()
                elif op==1:
                    t1.iconify()
                    view()   
            else:
                m.showerror('password','Wrong PASSWORD')
        else:
            m.showerror('user_name','Wrong USER_NAME')
def admin(): # for ui for admin sign_up
    global euser,epass,t1
    t1=Toplevel(bd=10,relief=SOLID)
    t1.title('Admin Login Page')
    t1.geometry('600x500+730+100')
    t1.resizable(0,0)
    t1['bg']='saddlebrown'

    n1=StringVar()
    n2=StringVar()

    lhead=Label(t1,text='Admin Log_in Form',font=('times new roman',30),fg='Black',relief=SOLID)
    lhead.pack(padx=30,pady=20)
    luser=Label(t1,text='User Name',font=('times new roman',10),bg='black',fg='white',width=20)
    luser.place(x=130,y=100)
    lpass=Label(t1,text='Password',font=('times new roman',10),bg='black',fg='white',width=20)
    lpass.place(x=130,y=140)

    euser=Entry(t1,width=20,font=('times new roman',12),bg='cyan',textvariable=n1)
    epass=Entry(t1,show='*',width=20,font=('times new roman',12),bg='cyan',textvariable=n2)
    euser.place(x=285,y=100)
    epass.place(x=285,y=140)

    button=Button(t1,text='SUBMIT',font=('times new roman',10),relief=SUNKEN,bd=5,bg='black',fg='white',width=30,command=sub)
    button.place(x=180,y=200)
    
