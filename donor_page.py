from tkinter import *
from tkinter import messagebox as m
from datetime import date
import pymysql
d=pymysql.connect(host='localhost',user='root',password='rooot',db='blood')
c=d.cursor()
def submit(): #donor registration submit button actions
    list1=['A+','A-','B+','B-','O+','O-','AB+','AB-']
    listphone=[]
    z1=ename.get()
    z2=eage.get()
    z3=n3.get()
    z4=ephone.get()
    z5=eaddress.get()
    z6=eblood.get()
    z7=emessure.get()
    z8=edate.get()
    c.execute('select phone from donor')
    res=c.fetchall()
#conditions for donate ...like;
    ## Empty field warning, Age consider only numbers, AGE LIMIT 18-65,INVALID Blood_group,
    #blood donation messurement 350-450 ,PHONE NUMBER should be 10 digits
    for i in res:
        listphone.append(i[0])  
    if z3=='0' or len(z5)==0 or len(z6)==0 or int(z7)==0 or len(z1)==0 or len(z2)==0 or len(z4)==0 or len(z8)==0:
        m.showwarning('warning..','Some field is empty!!!')
    elif z1.isalpha()==0:
        m.showwarning('warning..','Name field only consider alphabets!!') 
    elif z2.isdigit()==0:
        m.showwarning('warning..','Age field only consider numbers!!!')
        elif z4.isdigit()==0:
        m.showwarning('warning..','Phone number field only consider numbers!!!')      
    elif int(z2)<18 or int(z2)>65:
        m.showwarning('warning..','Age limit 18 to 65')
    elif z6 not in list1:
        m.showwarning('warning..',f'INVALID Blood_group : {z6} : !!')    
    elif int(z7)>450 or int(z7)<350:
        m.showwarning('Limitation Warning','U can donate maximum 450ml and minimum 350ml at a time')
        emessure.delete(0,'end')
    elif len(z4)<10 or len(z4)>10:
        m.showwarning('warning..','Phone number length should be 10')
    elif z4 in listphone:
#Importend: blood_donation(qty-350 to 450) once in 3 month
        ## find number of days (90) from database if >90 allow to donate on same database
        ## and.. if they add diff blood_group then send Warning... and correct it (if press yes)else exit.
        
        c.execute('select date from donor where phone=%s',z4)
        reslt=c.fetchall()
        for i in reslt:
            
            d1=i[0]
            d2=date.today()
            odate=d2-d1

            
            if (odate.days)<90:
                m.showwarning(f'LIMTATION',f'ur already donated..u can donate only after 90 days (till today- {odate}) from donated date({i[0]})')
            else:
                ans=m.askyesnocancel('Blood',f'CHECK YOUR MOBILE NUMBER\nELSE...{z1},You\'re already donated once...\nYes : It\'s MY OWN NUMBER continue donation\nNo : EDIT MY NUMBER \n Cancel: exit')
                c.execute('select * from donor where phone=%s',z4)
                res1=c.fetchall()
                for i in res1:
                    if ans==1:
                        if i[5] != z6:
#if the entered bllod_group in database is diff from new then,send msg for change bllod_grp
                            w=m.askyesno('BLOOD GROUP',f'YOUR BLOOD GROUP IS: {i[5]}\nYes: to proceed with {i[5]}\n No: to exit the page')
                            if w==1:
                                x=c.execute('update donor set messurement=%s where phone=%s',(int(i[6])+int(z7),z4))
                                m.showinfo('DONATED SUCCESSFULLY...',f'{i[0]} , Blood: {i[5]} Messurement: {z7}')
                                d.commit()
                                ename.delete(0,'end')
                                eage.delete(0,'end')
                                n3.set(0)
                                ephone.delete(0,'end')
                                eaddress.delete(0,'end')
                                eblood.delete(0,'end')
                                emessure.delete(0,'end')
                        else:
##make those fields empty after commit for another entry...only if days>90

                            x=c.execute('update donor set messurement=%s where phone=%s',(int(i[6])+int(z7),z4))
                            m.showinfo('DONATED SUCCESSFULLY...',f'{i[0]} , Blood: {i[5]} Messurement: {z7}')
                            d.commit()
                            ename.delete(0,'end')
                            eage.delete(0,'end')
                            n3.set(0)
                            ephone.delete(0,'end')
                            eaddress.delete(0,'end')
                            eblood.delete(0,'end')
                            emessure.delete(0,'end')
#if the donor entering wrong number then ask for re-entry
                    elif ans==0:
                        ephone.delete(0,'end')
                    else:
                        t4.destroy()
    else:           
        x='''insert into donor values(%s,%s,%s,%s,%s,%s,%s,%s)'''
        c.execute(x,(z1,z2,z3,z4,z5,z6,z7,z8))
        d.commit()   
##make those fields empty after commit for another entry

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
def donor(): #UI for donor registration...
#imortent : weight >45 and hemogoblin >12.5 is good_helth status for donation    
    q=m.askyesno('IMPORTENT QUESTION','Your body weight more than 45 kg AND HEMOGOBLIN Content More than 12.5gms/100ml')
    if q==0:
        m.showerror('<<SORRY>>','You can\'t DONATE Blood')
#till here 
    elif q==1:
        global ename,eage,n3,ephone,eaddress,eblood,emessure,t4,edate,nday,nmonth,nyear
        t4=Toplevel(bd=10,relief=SOLID)
        t4.title('Donor page')
        t4.geometry('600x500+720+100')
        t4.resizable(0,0)
        t4.wm_iconbitmap('life.ico')
        t4['bg']='teal'
        
        n1=StringVar()
        n2=StringVar()
        n3=StringVar()
        n4=StringVar()
        n5=StringVar()
        n6=StringVar()
        n7=StringVar()
        n8=StringVar()
        n3.set(0)
        
        now=date.today()
        
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
        edate.insert(0,now)
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

