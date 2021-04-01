from tkinter import *
from tkinter import messagebox  as m
from view_update1 import *
from tkinter import ttk
import pymysql

d=pymysql.connect(host='localhost',user='root',password='rooot',db='blood')
c=d.cursor()
def view():#view admin page
    global t2
    
    t2=Toplevel(bd=10,relief=SOLID)
    t2.title('Admin page')
    t2.geometry('600x500+730+100')
    t2.resizable(0,0)
    t2.wm_iconbitmap('life.ico')
    t2['bg']='brown'
    z=Label(t2,text='Admin Home',font=('times new roman',30),relief=SOLID,width=25)
    z.pack(padx=5,pady=20)
    b1=Button(t2,text='Donor Details',command=donor_details,width=20,font=('ariel',15,'bold'),relief=SUNKEN,bd=10,fg='white',bg='black')
    b1.pack(padx=10,pady=17)
    b2=Button(t2,text='Receiver Details',command=receiver_details,width=20,font=('ariel',15,'bold'),relief=SUNKEN,bd=10,fg='white',bg='black')
    b2.pack(padx=10,pady=17)
    b3=Button(t2,text='Update Donor',command=update_donor,width=20,font=('ariel',15,'bold'),relief=SUNKEN,bd=10,fg='white',bg='black')
    b3.pack(padx=10,pady=17)
    b4=Button(t2,text='Update Receiver',command=update_receiver,width=20,font=('ariel',15,'bold'),relief=SUNKEN,bd=10,fg='white',bg='black')
    b4.pack(padx=10,pady=17)
    c.execute('select messurement from donor')
    res=c.fetchall()
    x=0
#its like status..if updation is required then show some message,when enter to this [page    
    for r in res:
        x=x+int(r[0])
    if x>0:
        m.showinfo('On branch ADMIN','DONOR UPDATION IS REQUIRED...')
    c.execute('select messurement from receiver')
    res=c.fetchall()
    x1=0
    for r in res:
        x1=x1+int(r[0])
    if x1>0:
        m.showinfo('On branch ADMIN','RECEIVER UPDATE IS REQUIRED...')    
    t2.mainloop()
#till here    
def donor_details(): # all donor details
    t3=Toplevel(bd=10,relief=SOLID)
    t3.title('donor details')
    t3.geometry('1300x2500+30+20')
    t3.resizable(0,0)
    t3.wm_iconbitmap('life.ico')
    t3['bg']='light blue'

##    t3.columnconfigure(0,weight=1)
##    t3.rowconfigure(0,weight=1)
    
    lhead=Label(t3,text='Donor Details',font=('times new roman',30),relief=SOLID,width=53)
    lhead.place(x=50,y=30)
    lname=Label(t3,width=12,text=' Name ',font=('times new roman',15),bg='black',fg='white',)
    lname.place(x=80,y=100)
    lage=Label(t3,width=12,text=' Age ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lage.place(x=220,y=100)
    lgender=Label(t3,width=12,text=' Gender ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lgender.place(x=360,y=100)
    lphone=Label(t3,width=12,text=' phone ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lphone.place(x=500,y=100)
    laddress=Label(t3,width=12,text=' address ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    laddress.place(x=640,y=100)
    lblood=Label(t3,width=12,text=' Blood_group ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lblood.place(x=780,y=100)
    lmessure=Label(t3,width=12,text=' Messurement ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lmessure.place(x=920,y=100)
    ldate=Label(t3,width=12,text=' Date ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    ldate.place(x=1060,y=100)

    c.execute('select * from donor')
    result=c.fetchall()
    num=130
    t=0
    for i in result:
        lbname=Label(t3,text=i[0],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lbname.place(x=80,y=num)
        lbage=Label(t3,text=i[1],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lbage.place(x=220,y=num)       
        lbgender=Label(t3,text=i[2],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lbgender.place(x=360,y=num)
        lbphone=Label(t3,text=i[3],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lbphone.place(x=500,y=num)
        lbaddress=Label(t3,text=i[4],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lbaddress.place(x=640,y=num)
        lbblood=Label(t3,text=i[5],font=('times new roman',15),relief=SOLID,width=12,fg='red')
        lbblood.place(x=780,y=num)
        lbmessure=Label(t3,text=i[6],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lbmessure.place(x=920,y=num)
        lbdate=Label(t3,text=i[7],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lbdate.place(x=1060,y=num)
        num+=30
        t+=int(i[6])
    if t==0:
        indi=Label(t3,text='STATUS: EMPTY',font=('times new roman',30),relief=SUNKEN,bd=5,width=30,bg='green',fg='white')
        indi.place(x=300,y=600)
    elif t>0 and t<=3000:
        indi=Label(t3,text=f'STATUS: UPDATE(QTY : {t})',font=('times new roman',30),relief=SUNKEN,bd=5,width=30,bg='red',fg='white')
        indi.place(x=300,y=600)
    else:
        indi=Label(t3,text=f'STATUS: UPDATE(QTY : {t})',font=('times new roman',30),relief=SUNKEN,bd=5,width=30,bg='black',fg='white')
        indi.place(x=300,y=600)  
    t3.mainloop()    
def receiver_details(): # all reciever details
    t5=Toplevel(bd=10,relief=SOLID)
    t5.title('receiver details')
    t5.geometry('1300x700+30+20')
    t5.resizable(0,0)
    t5.wm_iconbitmap('life.ico')
    t5['bg']='light blue'
    lb1head=Label(t5,text='Receiver Details',font=('times new roman',30),relief=SOLID,width=53)
    lb1head.place(x=50,y=30)
    lb1name=Label(t5,width=12,text=' Name ',font=('times new roman',15),bg='black',fg='white',)
    lb1name.place(x=80,y=100)
    lb1age=Label(t5,width=12,text=' Age ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1age.place(x=220,y=100)
    lb1gender=Label(t5,width=12,text=' Gender ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1gender.place(x=360,y=100)
    lb1phone=Label(t5,width=12,text=' phone ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1phone.place(x=500,y=100)
    lb1address=Label(t5,width=12,text=' address ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1address.place(x=640,y=100)
    lb1blood=Label(t5,width=12,text=' Blood_group ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1blood.place(x=780,y=100)
    lb1messure=Label(t5,width=12,text=' Messurement ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1messure.place(x=920,y=100)
    lb1date=Label(t5,width=12,text=' Date ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1date.place(x=1060,y=100)

    c.execute('select * from receiver')
    result=c.fetchall()
    num=130
    t=0
    for i in result:
        lb2name=Label(t5,text=i[0],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lb2name.place(x=80,y=num)
        lb2age=Label(t5,text=i[1],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lb2age.place(x=220,y=num)       
        lb2gender=Label(t5,text=i[2],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lb2gender.place(x=360,y=num)
        lb2phone=Label(t5,text=i[3],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lb2phone.place(x=500,y=num)
        lb2address=Label(t5,text=i[4],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lb2address.place(x=640,y=num)
        lb2blood=Label(t5,text=i[5],font=('times new roman',15),relief=SOLID,width=12,fg='red')
        lb2blood.place(x=780,y=num)
        lb2messure=Label(t5,text=i[6],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lb2messure.place(x=920,y=num)
        lb2date=Label(t5,text=i[7],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lb2date.place(x=1060,y=num)
        num+=30
        t+=int(i[6])
    if t==0:
        indi=Label(t5,text='STATUS: EMPTY',font=('times new roman',30),relief=SUNKEN,bd=5,width=30,bg='green',fg='white')
        indi.place(x=300,y=600)
    elif t>0 and t<=3000:
        indi=Label(t5,text=f'STATUS: UPDATE(QTY : {t})',font=('times new roman',30),relief=SUNKEN,bd=5,width=30,bg='red',fg='white')
        indi.place(x=300,y=600)
    else:
        indi=Label(t5,text=f'STATUS: UPDATE(QTY : {t})',font=('times new roman',30),relief=SUNKEN,bd=5,width=30,bg='black',fg='white')
        indi.place(x=300,y=600)     
    t5.mainloop()    

