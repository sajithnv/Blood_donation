from tkinter import messagebox as m
from tkinter import *
import pymysql
d=pymysql.connect(host='localhost',user='root',password='rooot',db='blood')
c=d.cursor()
def donorblood():#for add the donar blood to stock and clear the donar stock empty
    t=0
    for i in bg:
        if i=='A+':
            c.execute('select messurement from donor where blood_group="A+"')
            mres=c.fetchall()
            for j in mres:
                t=t+int(j[0])
            c.execute('select ap from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0]) 
            c.execute('update update_blood set ap=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="A+"')
            d.commit()
        elif i=='A-':
            c.execute('select messurement from donor where blood_group="A-"')
            mres=c.fetchall()
            for j in mres:
                t=t+int(j[0])
            c.execute('select am from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0]) 
            c.execute('update update_blood set am=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="A-"')
            d.commit()
        elif i=='B+':
            c.execute('select messurement from donor where blood_group="B+"')
            mres=c.fetchall()
            for j in mres:
                t=t+int(j[0])
            c.execute('select bp from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0]) 
            c.execute('update update_blood set bp=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="B+"')
            d.commit()
        elif i=='B-':
            c.execute('select messurement from donor where blood_group="B-"')
            mres=c.fetchall()
            for j in mres:
                t=t+int(j[0])
            c.execute('select bm from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0]) 
            c.execute('update update_blood set bm=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="B-"')
            d.commit()
        elif i=='AB+':
            c.execute('select messurement from donor where blood_group="AB+"')
            mres=c.fetchall()
            for j in mres:
                t=t+int(j[0])
            c.execute('select abp from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0]) 
            c.execute('update update_blood set abp=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="AB+"')
            d.commit()
        elif i=='AB-':
            c.execute('select messurement from donor where blood_group="AB-"')
            mres=c.fetchall()
            for j in mres:
                t=t+int(j[0])
            c.execute('select abm from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0]) 
            c.execute('update update_blood set abm=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="AB-"')
            d.commit()
        elif i=='O+':
            c.execute('select messurement from donor where blood_group="O+"')
            mres=c.fetchall()
            for j in mres:
                t=t+int(j[0])
            c.execute('select op from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0]) 
            c.execute('update update_blood set op=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="O+"')
            d.commit()
        elif i=='O-':
            c.execute('select messurement from donor where blood_group="O-"')
            mres=c.fetchall()
            for j in mres:
                t=t+int(j[0])
            c.execute('select om from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0]) 
            c.execute('update update_blood set om=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="O-"')
            d.commit()     
def update_donor():#UI
    global eblood,emessure,bg,m
    t3=Toplevel(bd=10,relief=SOLID)
    t3.title('Update_donor_details')
    t3.geometry('900x700+200+20')
    t3.resizable(0,0)
    t3['bg']='light blue'
    
    lhead=Label(t3,text='Update Donor Details',font=('times new roman',30),relief=SOLID,width=35)
    lhead.place(x=50,y=30)
    lname=Label(t3,width=12,text=' Name ',font=('times new roman',15),bg='black',fg='white',)
    lname.place(x=150,y=100)
    lphone=Label(t3,width=12,text=' phone ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lphone.place(x=290,y=100)
    lblood=Label(t3,width=12,text=' Blood_group ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lblood.place(x=430,y=100)
    lmessure=Label(t3,width=12,text=' Messurement ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lmessure.place(x=570,y=100)
    c.execute('select * from donor')
    result=c.fetchall()
    num=130
    bg=set()
    m=[]
    for i in result:
        lbname=Label(t3,text=i[0],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lbname.place(x=150,y=num)
        lbphone=Label(t3,text=i[3],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lbphone.place(x=290,y=num)
        eblood=Label(t3,text=i[5],font=('times new roman',15),relief=SOLID,width=12,fg='red')
        eblood.place(x=430,y=num)
        emessure=Label(t3,text=i[6],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        emessure.place(x=570,y=num)
        bg.add(eblood.cget('text'))
        m.append(int(emessure.cget('text')))
        num+=30
    lbbutton=Button(t3,text='Update',font=('times new roman',20),relief=SUNKEN,bd=5,width=15,bg='red',fg='white',command=donorblood)
    lbbutton.place(x=300,y=450)      
    t3.mainloop()    
def update_receiver():
    t5=Toplevel(bd=10,relief=SOLID)
    t5.title('Update_receiver_details')
    t5.geometry('900x700+200+20')
    t5.resizable(0,0)
    t5['bg']='light blue'
    lb1head=Label(t5,text='Update Receiver Details',font=('times new roman',30),relief=SOLID,width=35)
    lb1head.place(x=50,y=30)
    lb1name=Label(t5,width=12,text=' Name ',font=('times new roman',15),bg='black',fg='white',)
    lb1name.place(x=80,y=100)
    lb1phone=Label(t5,width=12,text=' phone ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1phone.place(x=220,y=100)
    lb1blood=Label(t5,width=12,text=' Blood_group ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1blood.place(x=360,y=100)
    lb1messure=Label(t5,width=12,text=' Messurement ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1messure.place(x=500,y=100)
    lb1update=Label(t5,width=12,text=' Modify ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1update.place(x=660,y=100)

    c.execute('select * from receiver')
    result=c.fetchall()
    num=130
    bg=set()
    m=[]
    for i in result:
        lb2name=Label(t5,text=i[0],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lb2name.place(x=80,y=num)
        lb2phone=Label(t5,text=i[3],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lb2phone.place(x=220,y=num)
        lb2blood=Label(t5,text=i[5],font=('times new roman',15),relief=SOLID,width=12,fg='red')
        lb2blood.place(x=360,y=num)
        lb2messure=Label(t5,text=i[6],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
        lb2messure.place(x=500,y=num)
        
        num+=30
    lbbutton=Button(t3,text='Update',font=('times new roman',20),relief=SUNKEN,bd=5,width=15,bg='red',fg='white')#,command=receiverblood)
    lbbutton.place(x=300,y=450)    
    t5.mainloop()    


