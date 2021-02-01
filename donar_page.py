from tkinter import *
from tkinter import messagebox as m
##from datetime import *
import pymysql
d=pymysql.connect(host='localhost',user='root',password='rooot',db='blood')
c=d.cursor()
def submit():
    list1=['A+','A-','B+','B-','O+','O-','AB+','AB-']
    z1=ename.get()
    z2=eage.get()
    z3=n3.get()
    z4=ephone.get()
    z5=eaddress.get()
    z6=eblood.get()
    z7=emessure.get()
##    z8=edate.get()
    if len(z3)==0 or len(z5)==0 or len(z6)==0 or int(z7)==0:
        m.showwarning('warning..','Some field is empty!!!')
    elif z1.isalpha()==0:
        m.showwarning('warning..','Name field only consider alphabets!!!') 
    elif z2.isdigit()==0:
        m.showwarning('warning..','Age field only consider numbers!!!')
    elif z4.isdigit()==0:
        m.showwarning('warning..','Phone number field only consider numbers!!!')      
    elif int(z2)<18 or int(z2)>65:
        m.showwarning('warning..','Age limit 18 to 65')
    elif z6 not in list1:
        m.showwarning('warning..',f'INVALID Blood_group : {z6} : !!')    
    elif int(z7)>350 and int(z7)<30:
        m.showwarning('Limitation Warning','U can donate maximum 350ml and minimum 30ml at a time')
        emessure.delete(0,'end')
    elif len(z4)<10 or len(z4)>10:
        m.showwarning('warning..','Phone number length should be 10')
    else:
        x='''insert into donar values(%s,%s,%s,%s,%s,%s,%s,%s)'''
        c.execute(x,(z1,z2,z3,z4,z5,z6,z7))#z8
        d.commit()
        ename.delete(0,'end')
        eage.delete(0,'end')
        n3.set(0)
        ephone.delete(0,'end')
        eaddress.delete(0,'end')
        eblood.delete(0,'end')
        emessure.delete(0,'end')
        m.showinfo('Notification',f'{z1}, Data added successfuly')
        z=m.askyesno('close donar page','Are you sure to CLOSE DONAR PAGE...')
        if z==1:
            t.destroy()

def donar():
    q=m.askyesno('IMPORTENT QUESTION','Your body weight more than 45 kg AND HEMOGOBLIN Content More than 12.5gms/100ml')
    if q==0:
        m.showerror('<<SORRY>>','You can\'t DONATE Blood')
    elif q==1:    
        global ename,eage,n3,ephone,eaddress,eblood,emessure,t,edate
        t=Toplevel(bd=10,relief=SOLID)
        t.title('Donar page')
        t.geometry('600x500+720+100')
        t.resizable(0,0)
        t['bg']='light blue'
##        now=datetime.now()
##        mnow=now.strftime('%m')
##        ynow=now.strftime('%Y')
        n1=StringVar()
        n2=StringVar()
        n3=StringVar()
        n4=StringVar()
        n5=StringVar()
        n6=StringVar()
        n7=StringVar()
##        n8=StringVar()
        n3.set(0)
##        fdate=Frame(t,relief=SUNKEN,bd=10,width=30)
##        fdate.place(x=165,y=430)
##        edate=Entry(fdate,text=f"Month: {mnow} Year:{ynow}",width=30,textvariable=n8)
##        edate.pack()
        lhead=Label(t,text='Donar Registration Form',relief=SOLID,font=('times new roman',30),fg='black')
        lhead.pack(padx=5,pady=20)
        lname=Label(t,text='Name',fg='white',bg='black',width=20)
        lname.place(x=130,y=100)
        lage=Label(t,text='Age',fg='white',bg='black',width=20)
        lage.place(x=130,y=140)
        lgen=Label(t,text='Gender',fg='white',bg='black',width=20)
        lgen.place(x=130,y=180)
        lphone=Label(t,text='Phone_no +91',fg='white',bg='black',width=20)
        lphone.place(x=130,y=220)
        laddress=Label(t,text='Address',fg='white',bg='black',width=20)
        laddress.place(x=130,y=260)
        lblood=Label(t,text='Blood_Group in CAPITAL',fg='white',bg='black',width=20)
        lblood.place(x=130,y=300)
        lmessure=Label(t,text='Messurement in ml',fg='white',bg='black',width=20)
        lmessure.place(x=130,y=340)

        ename=Entry(t,width=20,font=('times new roman',12),textvariable=n1,bg='cyan')
        ename.place(x=310,y=100)
        eage=Entry(t,width=20,font=('times new roman',12),textvariable=n2,bg='cyan')
        eage.place(x=310,y=140)
        
        r1=Radiobutton(t,text='Male',variable=n3,value='Male')
        r1.place(x=310,y=180)
        r2=Radiobutton(t,text='Female',variable=n3,value='Female')
        r2.place(x=390,y=180)
        
        ephone=Entry(t,width=20,font=('times new roman',12),textvariable=n4,bg='cyan')
        ephone.place(x=310,y=220)
        eaddress=Entry(t,width=20,font=('times new roman',12),textvariable=n5,bg='cyan')
        eaddress.place(x=310,y=260)
        eblood=Entry(t,width=20,font=('times new roman',12),textvariable=n6,bg='cyan')
        eblood.place(x=310,y=300)
        emessure=Entry(t,width=20,font=('times new roman',12),textvariable=n7,bg='cyan')
        emessure.place(x=310,y=340)

        b=Button(t,text='SUBMIT',font=('times new roman',12,'bold'),bg='light green',width=30,command=submit)
        b.place(x=165,y=390)   
        t.mainloop()

