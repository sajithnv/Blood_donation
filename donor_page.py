from tkinter import *
from tkinter import messagebox as m
from datetime import *
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
    z8=edate.get()
##    result=c.fetchall()
##        for i in result:
##            if z4 in i[3]:
##                newblood=int(z7)+int(i[3])
##                y="update donor set messurement=f'{newblood}' where phone=f'{int(z4)}'"
##                c.execute(y)
##                d.commit()
##        else: 
    if len(z3)==0 or len(z5)==0 or len(z6)==0 or int(z7)==0:
        m.showwarning('warning..','Some field is empty!!!')
    elif z1.isalpha()==0 or z1.isspace==1 or z1.isspace==0:
        m.showwarning('warning..','Name field only consider alphabets and spaces!!!') 
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
##        c.execute('select phone from donor')
##        result=c.fetchall()
##        l=[]
##        for i in int(result):
##            l.append(i)
##        print(l)    
##        if z4 in l:
##            print('hii')
##            x=ephone.get()
##            c.execute("select messurement from donor where phone=f'{x}'")
##            result=c.fetchall()
##            print(result)
##            
##          for i in result:
##                    print(i)
##                    bld=int(i[6])+10
##                    m.message('',f'{bld}')
##                    newblood=f'{str(bld)}'
##                    z="select messsure from donor"
##                    c.execute(z)
##                    y="update donor set messurement='%s' where phone='%s'"
##                    c.execute(y,(newblood,z4))
##                    d.commit()
           
        x='''insert into donor values(%s,%s,%s,%s,%s,%s,%s,%s)'''
        c.execute(x,(z1,z2,z3,z4,z5,z6,z7,z8))
        d.commit()   
        ename.delete(0,'end')
        eage.delete(0,'end')
        n3.set(0)
        ephone.delete(0,'end')
        eaddress.delete(0,'end')
        eblood.delete(0,'end')
        emessure.delete(0,'end')
        m.showinfo('Notification',f'{z1}, Data added successfuly')
        z=m.askyesno('close donor page','Are you sure to CLOSE DONOR PAGE...')
        if z==1:
            t4.withdraw()

def donor():
    q=m.askyesno('IMPORTENT QUESTION','Your body weight more than 45 kg AND HEMOGOBLIN Content More than 12.5gms/100ml')
    if q==0:
        m.showerror('<<SORRY>>','You can\'t DONATE Blood')
    elif q==1:
        global ename,eage,n3,ephone,eaddress,eblood,emessure,t4,edate,nday,nmonth,nyear
        t4=Toplevel(bd=10,relief=SOLID)
        t4.title('Donor page')
        t4.geometry('600x500+720+100')
        t4.resizable(0,0)
        t4['bg']='light blue'
        
        n1=StringVar()
        n2=StringVar()
        n3=StringVar()
        n4=StringVar()
        n5=StringVar()
        n6=StringVar()
        n7=StringVar()
        n8=StringVar()
        n3.set(0)
        
        now=datetime.now()
        nday=now.strftime("%d")
        nmonth=now.strftime("%m")
        nyear=now.strftime("%Y")
        
        lhead=Label(t4,text='Donor Registration Form',relief=SOLID,font=('times new roman',30),fg='black')
        lhead.pack(padx=40,pady=20)
        ldate=Label(t4,text='Date',fg='white',bg='black',width=20)
        ldate.place(x=120,y=100)
        lname=Label(t4,text='Name',fg='white',bg='black',width=20)
        lname.place(x=120,y=140)
        lage=Label(t4,text='Age',fg='white',bg='black',width=20)
        lage.place(x=120,y=180)
        lgen=Label(t4,text='Gender',fg='white',bg='black',width=20)
        lgen.place(x=120,y=220)
        lphone=Label(t4,text='Phone_no +91',fg='white',bg='black',width=20)
        lphone.place(x=120,y=260)
        laddress=Label(t4,text='Address',fg='white',bg='black',width=20)
        laddress.place(x=120,y=300)
        lblood=Label(t4,text='Blood_Group in CAPITAL',fg='white',bg='black',width=20)
        lblood.place(x=120,y=340)
        lmessure=Label(t4,text='Messurement in ml',fg='white',bg='black',width=20)
        lmessure.place(x=120,y=380)

        edate=Entry(t4,width=20,font=('times new roman',12),textvariable=n8,bg='cyan')
        edate.insert(0,f'{nday}/{nmonth}/{nyear}')
        edate.place(x=300,y=100)
        ename=Entry(t4,width=20,font=('times new roman',12),textvariable=n1,bg='cyan')
        ename.place(x=300,y=140)
        eage=Entry(t4,width=20,font=('times new roman',12),textvariable=n2,bg='cyan')
        eage.place(x=300,y=180)
        
        r1=Radiobutton(t4,text='Male',variable=n3,value='Male')
        r1.place(x=310,y=220)
        r2=Radiobutton(t4,text='Female',variable=n3,value='Female')
        r2.place(x=390,y=220)
        
        ephone=Entry(t4,width=20,font=('times new roman',12),textvariable=n4,bg='cyan')
        ephone.place(x=300,y=260)
        eaddress=Entry(t4,width=20,font=('times new roman',12),textvariable=n5,bg='cyan')
        eaddress.place(x=300,y=300)
        eblood=Entry(t4,width=20,font=('times new roman',12),textvariable=n6,bg='cyan')
        eblood.place(x=300,y=340)
        emessure=Entry(t4,width=20,font=('times new roman',12),textvariable=n7,bg='cyan')
        emessure.place(x=300,y=380)

        b=Button(t4,text='SUBMIT',font=('times new roman',12,'bold'),bg='light green',width=30,command=submit)
        b.place(x=155,y=420)   
        t4.mainloop()

