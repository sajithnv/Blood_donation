from tkinter import *
from tkinter import messagebox as m
import pymysql
d=pymysql.connect(host='localhost',user='root',password='rooot',db='blood')
c=d.cursor()
def submit():
    z1=e1.get()
    z2=e2.get()
    z3=n3.get()
    z4=e3.get()
    z5=e4.get()
    z6=e5.get()
    z7=e6.get()
    x='''insert into donar values(%s,%s,%s,%s,%s,%s,%s)'''
    c.execute(x,(z1,z2,z3,z4,z5,z6,z7))
    d.commit()
    e1.delete(0,'end')
    e2.delete(0,'end')
    n3.set(0)
    e3.delete(0,'end')
    e4.delete(0,'end')
    e5.delete(0,'end')
    e6.delete(0,'end')
    m.showinfo('Notification',f'{z1}, Data added successfuly')
##    z=m.askyesno('close window','Are you sure...')
##    if z== 'yes':
##        t.destroy()

def donar():
    global e1,e2,e3,e4,e5,e6,n3
    t=Toplevel(bd=10,relief=SOLID)
    t.title('Donar page')
    t.geometry('600x500+720+100')
    t.resizable(0,0)
    t['bg']='light blue'
    
    n1=StringVar()
    n2=StringVar()
    n3=StringVar()
    n4=StringVar()
    n5=StringVar()
    n6=StringVar()
    n7=StringVar()
    
    l1=Label(t,text='Donar Registration Form',relief=SOLID,font=('times new roman',30),fg='black')
    l1.pack(padx=5,pady=20)
    l2=Label(t,text='Name',fg='white',bg='black',width=20)
    l2.place(x=130,y=100)
    l3=Label(t,text='Age',fg='white',bg='black',width=20)
    l3.place(x=130,y=140)
    l4=Label(t,text='Gender',fg='white',bg='black',width=20)
    l4.place(x=130,y=180)
    l5=Label(t,text='Phone_no',fg='white',bg='black',width=20)
    l5.place(x=130,y=220)
    l6=Label(t,text='Address',fg='white',bg='black',width=20)
    l6.place(x=130,y=260)
    l7=Label(t,text='Blood_Group',fg='white',bg='black',width=20)
    l7.place(x=130,y=300)
    l8=Label(t,text='Messurement',fg='white',bg='black',width=20)
    l8.place(x=130,y=340)

    e1=Entry(t,width=20,font=('times new roman',12),textvariable=n1,bg='cyan')
    e1.place(x=310,y=100)
    e2=Entry(t,width=20,font=('times new roman',12),textvariable=n2,bg='cyan')
    e2.place(x=310,y=140)
    
    r1=Radiobutton(t,text='Male',variable=n3,value='Male')
    r1.place(x=310,y=180)
    r2=Radiobutton(t,text='Female',variable=n3,value='Female')
    r2.place(x=390,y=180)
    
    e3=Entry(t,width=20,font=('times new roman',12),textvariable=n4,bg='cyan')
    e3.place(x=310,y=220)
    e4=Entry(t,width=20,font=('times new roman',12),textvariable=n5,bg='cyan')
    e4.place(x=310,y=260)
    e5=Entry(t,width=20,font=('times new roman',12),textvariable=n6,bg='cyan')
    e5.place(x=310,y=300)
    e6=Entry(t,width=20,font=('times new roman',12),textvariable=n7,bg='cyan')
    e6.place(x=310,y=340)
    b=Button(t,text='SUBMIT',font=('times new roman',12,'bold'),bg='light green',width=30,command=submit)
    b.place(x=165,y=390)   
    t.mainloop()

