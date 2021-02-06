from tkinter import messagebox as m
from tkinter import *
import pymysql
d=pymysql.connect(host='localhost',user='root',password='rooot',db='blood')
c=d.cursor()
#for add the donar blood to stock and clear the donar stock empty
def donorblood():#admin_page update_button of donate
    t=0
#1)Nothing to update msg for admin     
    c.execute('select messurement from donor')
    res=c.fetchall()
    x=0
    for r in res:
        x=x+int(r[0])
    if x==0:
        m.showinfo('On branch ADMIN','Nothing to update total amount of blood= 0')
    c.execute('select blood_group,messurement from donor')
    bg=c.fetchall()
#1)till here
    for i in bg:
        if i[0]=='A+':
            t=int(i[1])
            c.execute('select ap from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0])
            if t<=0:
                continue
            c.execute('update update_blood set ap=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="A+"')
            m.showinfo('STATEMENT',f'Blood A+ Stored successfully..crnt_bld: {t1} new_bld: {t} total= {t1+t}')
            d.commit()
        elif i[0]=='A-':
            t=int(i[1])
            c.execute('select am from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0])
            if t<=0:
                continue    
            c.execute('update update_blood set am=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="A-"')
            m.showinfo('STATEMENT',f'Blood A- Stored successfully..crnt_bld: {t1} new_bld: {t} total= {t1+t}')
            d.commit()
        elif i[0]=='B+':
            t=int(i[1])
            c.execute('select bp from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0])
            if t<=0:
                continue    
            c.execute('update update_blood set bp=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="B+"')
            m.showinfo('STATEMENT',f'Blood B+ Stored successfully..crnt_bld: {t1} new_bld: {t} total= {t1+t}')
            d.commit()
        elif i[0]=='B-':
            t=int(i[1])
            c.execute('select bm from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0])
            if t<=0:
                continue    
            c.execute('update update_blood set bm=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="B-"')
            m.showinfo('STATEMENT',f'Blood B- Stored successfully..crnt_bld: {t1} new_bld: {t} total= {t1+t}')            
            d.commit()
        elif i[0]=='AB+':
            t=int(i[1])
            c.execute('select abp from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0])
            if t<=0:
                continue    
            c.execute('update update_blood set abp=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="AB+"')
            m.showinfo('STATEMENT',f'Blood AB+ Stored successfully..crnt_bld: {t1} new_bld: {t} total= {t1+t}')            
            d.commit()
        elif i[0]=='AB-':
            t=int(i[1])
            c.execute('select abm from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0])
            if t<=0:
                continue    
            c.execute('update update_blood set abm=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="AB-"')
            m.showinfo('STATEMENT',f'Blood AB- Stored successfully..crnt_bld: {t1} new_bld: {t} total= {t1+t}')            
            d.commit()
        elif i[0]=='O+':
            t=int(i[1])
            c.execute('select op from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0])
            if t<=0:
                continue    
            c.execute('update update_blood set op=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="O+"')
            m.showinfo('STATEMENT',f'Blood O+ Stored successfully..crnt_bld: {t1} new_bld: {t} total= {t1+t}')            
            d.commit()
        elif i[0]=='O-':
            t=int(i[1])
            c.execute('select om from update_blood')
            apres=c.fetchall()
            for k in apres:
                t1=int(k[0])
            if t<=0:
                continue    
            c.execute('update update_blood set om=%s',(t1+t))
            c.execute('update donor set messurement="0" where blood_group="O-"')
            m.showinfo('STATEMENT',f'Blood O- Stored successfully..crnt_bld: {t1} new_bld: {t} total= {t1+t}')
            
            d.commit()
#till here           
def update_donor():#UI
    global bg
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
#notification.... "nothing to update in receiver" 
    c.execute('select messurement from donor')
    res=c.fetchall()
    x=0
    for r in res:
        x=x+int(r[0])
    if x==0:
        m.showinfo('On branch ADMIN','Nothing to update No one is requested yet!')
#till here
#print details of donor if anything is pending for update
    for i in result:
        if int(i[6])==0:
            continue    
        else:
            lbname=Label(t3,text=i[0],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
            lbname.place(x=150,y=num)
            lbphone=Label(t3,text=i[3],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
            lbphone.place(x=290,y=num)
            eblood=Label(t3,text=i[5],font=('times new roman',15),relief=SOLID,width=12,fg='red')
            eblood.place(x=430,y=num)
            emessure=Label(t3,text=i[6],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
            emessure.place(x=570,y=num)
            num+=30
    lbbutton=Button(t3,text='Update',font=('times new roman',20),relief=SUNKEN,bd=5,width=15,bg='red',fg='white',command=donorblood)
    lbbutton.place(x=300,y=450)
    c.execute('select messurement from donor')
    
    t3.mainloop()
#till here    
#for receive blood and clear the stock from donarstock
def receiverblood():#admin_page update_button of receiver
    t=0
#1)for 'nothing to update' notification for admin 
    c.execute('select messurement from receiver')
    res=c.fetchall()
    x=0
    for r in res:
        x=x+int(r[0])
    if x==0:
        m.showinfo('On branch ADMIN','Nothing to update No one is requested yet!')
#2) for direct donation from single blood group
    c.execute('select blood_group,messurement,phone from receiver')
    res=c.fetchall()
    for i in res:
        if i[0]=='O-':
            c.execute('select om from update_blood')
            mres1=c.fetchall()
            for j1 in mres1:
                t1=int(j1[0])
            t=int(i[1])
            if t<=0:
                continue
            if t<t1:
                m.showinfo('Blood','O- Blood is Received Successfully')
                c.execute('update update_blood set om=%s',(t1-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            else:
                m.showwarning('Blood','(total quantity of O-)is < Blood u want so,Blood is not AVAILABLE')
        elif i[0]=='O+':
            c.execute('select op from update_blood')
            mres1=c.fetchall()
            for j1 in mres1:
                t1=int(j1[0])
            c.execute('select om from update_blood')
            mres2=c.fetchall()
            for j2 in mres2:
                t2=int(j2[0])
            t=int(i[1])
#3)for block the messages if the messurement = 0            
            if t<=0:
                continue
#3 till here            
            total=t1+t2    
            if t<=t1:
                m.showinfo('Blood','O+ Blood is Received Successfully')
                c.execute('update update_blood set op=%s',(t1-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t2:
                m.showinfo('Blood','O+ is not available..so, O- is Received Successfully')
                c.execute('update update_blood set om=%s',(t2-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
#2 till here
#4)if the single blood_group amount < amnt of blood needed then A COMINATION of bloodgroups provide...                
            elif t<=total:
                zz=m.askyesno('Blood','Blood O+ is not AVAILABLE..so,proceed a combination of blood\n yes=Proceed or no=EXIT')
                if zz==1:
                    b1=t1-t
                    c.execute('update update_blood set op=%s',(t1-t1))
                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                    d.commit()
                    if b1<0:
                        b2=t2-abs(b1)
                        if b2<=0:
                            c.execute('update update_blood set om=%s',(t2-t2))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        else:
                            m.showinfo('Blood','Combination of O+ and O- are used..,Blood Received successfully')
                            c.execute('update update_blood set om=%s',(t2-abs(b1)))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                if zz==0:
                    break
#4 till here...
#main#####...continue same methods..
            else:
                m.showwarning('Blood','(total quantity of O+,O-)is < Blood u want so,Blood is not AVAILABLE')

        elif i[0]=='A-':
            c.execute('select am from update_blood')
            mres1=c.fetchall()
            for j1 in mres1:
                t1=int(j1[0])
            c.execute('select om from update_blood')
            mres2=c.fetchall()
            for j2 in mres2:
                t2=int(j2[0])
            t=int(i[1])
            if t<=0:
                continue    
            total=t1+t2    
            if t<=t1:
                m.showinfo('Blood','A- Blood is Received Successfully')
                c.execute('update update_blood set am=%s',(t1-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t2:
                m.showinfo('Blood','A- is not available..so, O- is Received Successfully')
                c.execute('update update_blood set om=%s',(t2-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=total:
                zz=m.askyesno('Blood','Blood A- is not AVAILABLE..so,proceed a combination of blood\n yes=Proceed or no=EXIT')
                if zz==1:
                    b1=t1-t
                    c.execute('update update_blood set am=%s',(t1-t1))
                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                    d.commit()
                    if b1<0:
                        b2=t2-abs(b1)
                        if b2<=0:
                            c.execute('update update_blood set om=%s',(t2-t2))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        else:
                            m.showinfo('Blood','Combination of A- and O- are used..,Blood Received successfully')
                            c.execute('update update_blood set om=%s',(t2-abs(b1)))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                if zz==0:
                    break
            else:
                m.showwarning('Blood','(total quantity of A-,O-)is < Blood u want so,Blood is not AVAILABLE')

        elif i[0]=='B-':
            c.execute('select bm from update_blood')
            mres1=c.fetchall()
            for j1 in mres1:
                t1=int(j1[0])
            c.execute('select om from update_blood')
            mres2=c.fetchall()
            for j2 in mres2:
                t2=int(j2[0])
            t=int(i[1])
            if t<=0:
                continue    
            total=t1+t2    
            if t<=t1:
                m.showinfo('Blood','B- Blood is Received Successfully')
                c.execute('update update_blood set bm=%s',(t1-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t2:
                m.showinfo('Blood','B- is not available..so, O- is Received Successfully')
                c.execute('update update_blood set om=%s',(t2-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=total:
                zz=m.askyesno('Blood','Blood B- is not AVAILABLE..so,proceed a combination of blood\n yes=Proceed or no=EXIT')
                if zz==1:
                    b1=t1-t
                    c.execute('update update_blood set bm=%s',(t1-t1))
                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                    d.commit()
                    if b1<0:
                        b2=t2-abs(b1)
                        if b2<=0:
                            c.execute('update update_blood set om=%s',(t2-t2))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        else:
                            m.showinfo('Blood','Combination of B- and O- are used..,Blood Received successfully')
                            c.execute('update update_blood set om=%s',(t2-abs(b1)))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                if zz==0:
                    break
            else:
                m.showwarning('Blood','(total quantity of B- and O-)is < Blood u want so,Blood is not AVAILABLE')


        elif i[0]=='A+':
            c.execute('select ap from update_blood')
            mres1=c.fetchall()
            for j1 in mres1:
                t1=int(j1[0])
            c.execute('select am from update_blood')
            mres2=c.fetchall()
            for j2 in mres2:
                t2=int(j2[0])
            c.execute('select op from update_blood')
            mres3=c.fetchall()
            for j3 in mres3:
                t3=int(j3[0])
            c.execute('select om from update_blood')
            mres4=c.fetchall()
            for j4 in mres4:
                t4=int(j4[0])
            t=int(i[1])
            if t<=0:
                continue
            total=t1+t2+t3+t4    
            if t<=t1:
                m.showinfo('Blood','A+ Blood is Received Successfully')
                c.execute('update update_blood set ap=%s',(t1-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t2:
                m.showinfo('Blood','A+ is not available..so, A- is Received Successfully')
                c.execute('update update_blood set am=%s',(t2-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t3:
                m.showinfo('Blood','A+ is not available..so,O+ is Received Successfully')
                c.execute('update update_blood set op=%s',(t3-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t4:
                m.showinfo('Blood','A+ is not available..so,O- is Received Successfully')
                c.execute('update update_blood set om=%s',(t4-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=total:
                zz=m.askyesno('Blood','Blood A+ is not AVAILABLE..so,proceed a combination of blood\n yes=Proceed or no=EXIT')
                if zz==1:
                    b1=t1-t
                    c.execute('update update_blood set ap=%s',(t1-t1))
                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                    d.commit()
                    if b1<0:
                        b2=t2-abs(b1)
                        if b2<=0:
                            c.execute('update update_blood set am=%s',(t2-t2))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        else:
                            m.showinfo('Blood','Combination of A+ and A- are used..,Blood Received successfully')                            
                            c.execute('update update_blood set am=%s',(t2-abs(b1)))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        if b2<0:
                            b3=t3-abs(b2)
                            if b3<=0:
                                c.execute('update update_blood set op=%s',(t3-t3))
                                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                d.commit()
                            else:
                                m.showinfo('Blood','Combination of A+,A-and O+ are used..,Blood Received successfully')
                                c.execute('update update_blood set op=%s',(t3-abs(b2)))
                                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                d.commit()
                            if b3<0:
                                b4=t4-abs(b3)
                                if b4<=0:
                                    m.showinfo('Blood','Combination of A+,A-,O+,O- are used...,Blood Received successfully')
                                    c.execute('update update_blood set om=%s',(t4-t4))
                                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                    d.commit()
    ##                    else:
    ##                        c.execute('update update_blood set op=%s',(t4-abs(b3))
    ##                        c.execute('update receiver set messurement="0" where blood_group="O+"')
                    #m.showinfo('Blood','A+ is not available..so, A combination of(total=A+,A-,O+,O-) is Received Successfully')
                if zz==0:
                    break
            else:
                m.showwarning('Blood','(total quantity of A+,A-,O+,O-)is < Blood u want so,Blood is not AVAILABLE')
        elif i[0]=='B+':
            c.execute('select bp from update_blood')
            mres1=c.fetchall()
            for j1 in mres1:
                t1=int(j1[0])
            c.execute('select bm from update_blood')
            mres2=c.fetchall()
            for j2 in mres2:
                t2=int(j2[0])
            c.execute('select op from update_blood')
            mres3=c.fetchall()
            for j3 in mres3:
                t3=int(j3[0])
            c.execute('select om from update_blood')
            mres4=c.fetchall()
            for j4 in mres4:
                t4=int(j4[0])
            t=int(i[1])
            if t<=0:
                continue    
            total=t1+t2+t3+t4    
            if t<=t1:
                m.showinfo('Blood','B+ Blood is Received Successfully')
                c.execute('update update_blood set bp=%s',(t1-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t2:
                m.showinfo('Blood','B+ is not available..so, B- is Received Successfully')
                c.execute('update update_blood set bm=%s',(t2-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t3:
                m.showinfo('Blood','B+ is not available..so,O+ is Received Successfully')
                c.execute('update update_blood set op=%s',(t3-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t4:
                m.showinfo('Blood','B+ is not available..so,O- is Received Successfully')
                c.execute('update update_blood set om=%s',(t4-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=total:
                zz=m.askyesno('Blood','Blood B+ is not AVAILABLE..so,proceed a combination of blood\n yes=Proceed or no=EXIT')
                if zz==1:
                    b1=t1-t
                    c.execute('update update_blood set bp=%s',(t1-t1))
                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                    d.commit()
                    if b1<0:
                        b2=t2-abs(b1)
                        if b2<=0:
                            c.execute('update update_blood set bm=%s',(t2-t2))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        else:    
                            m.showinfo('Blood','Combination of B+ and B- are used..,Blood Received successfully')
                            c.execute('update update_blood set bm=%s',(t2-abs(b1)))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        if b2<0:
                            b3=t3-abs(b2)
                            if b3<=0:
                                c.execute('update update_blood set op=%s',(t3-t3))
                                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                d.commit()
                            else:
                                m.showinfo('Blood','Combination of B+,B-and O+ are used..,Blood Received successfully')
                                c.execute('update update_blood set op=%s',(t3-abs(b2)))
                                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                d.commit()
                            if b3<0:
                                b4=t4-abs(b3)
                                if b4<=0:
                                    m.showinfo('Blood','Combination of B+,B-,O+,O- are used...,Blood Received successfully')
                                    c.execute('update update_blood set om=%s',(t4-t4))
                                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                    d.commit()
    ##                    else:
    ##                        c.execute('update update_blood set op=%s',(t4-abs(b3))
    ##                        c.execute('update receiver set messurement="0" where blood_group="O+"')
                   # m.showinfo('Blood','B+ is not available..so, A combination of(total=B+,B-,O+,O-) is Received Successfully')
                if zz==0:
                    break
            else:
                m.showwarning('Blood','(total quantity of B+,B-,O+,O-)is < Blood u want so,Blood is not AVAILABLE')
            
        elif i[0]=='AB-':
            c.execute('select abm from update_blood')
            mres1=c.fetchall()
            for j1 in mres1:
                t1=int(j1[0])
            c.execute('select am from update_blood')
            mres2=c.fetchall()
            for j2 in mres2:
                t2=int(j2[0])
            c.execute('select bm from update_blood')
            mres3=c.fetchall()
            for j3 in mres3:
                t3=int(j3[0])
            c.execute('select om from update_blood')
            mres4=c.fetchall()
            for j4 in mres4:
                t4=int(j4[0])
            t=int(i[1])
            if t<=0:
                continue    
            total=t1+t2+t3+t4    
            if t<=t1:
                m.showinfo('Blood','AB- Blood is Received Successfully')
                c.execute('update update_blood set abm=%s',(t1-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))        
                d.commit()
            elif t<=t2:
                m.showinfo('Blood','AB- is not available..so, A- is Received Successfully')
                c.execute('update update_blood set am=%s',(t2-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t3:
                m.showinfo('Blood','AB- is not available..so,B-is Received Successfully')
                c.execute('update update_blood set bm=%s',(t3-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t4:
                m.showinfo('Blood','AB- is not available..so,O- is Received Successfully')
                c.execute('update update_blood set om=%s',(t4-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=total:
                zz=m.askyesno('Blood','Blood AB- is not AVAILABLE..so,proceed a combination of blood\n yes=Proceed or no=EXIT')
                if zz==1:
                    b1=t1-t
                    c.execute('update update_blood set abm=%s',(t1-t1))
                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                    d.commit()
                    if b1<0:
                        b2=t2-abs(b1)
                        if b2<=0:
                            c.execute('update update_blood set am=%s',(t2-t2))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        else:    
                            m.showinfo('Blood','Combination of AB- and A- are used..,Blood Received successfully')
                            c.execute('update update_blood set am=%s',(t2-abs(b1)))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        if b2<0:
                            b3=t3-abs(b2)
                            if b3<=0:
                                c.execute('update update_blood set bm=%s',(t3-t3))
                                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                d.commit()
                            else:
                                m.showinfo('Blood','Combination of AB-,A-and B- are used..,Blood Received successfully')
                                c.execute('update update_blood set bm=%s',(t3-abs(b2)))
                                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                d.commit()
                            if b3<0:
                                b4=t4-abs(b3)
                                if b4<=0:
                                    m.showinfo('Blood','Combination of AB-,A-,B-,O- are used...,Blood Received successfully')
                                    c.execute('update update_blood set om=%s',(t4-t4))
                                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                    d.commit()
    ##                    else:
    ##                        c.execute('update update_blood set op=%s',(t4-abs(b3))
    ##                        c.execute('update receiver set messurement="0" where blood_group="O+"')
                    #m.showinfo('Blood','AB- is not available..so, A combination of(total=AB-,A-,B-,O-) is Received Successfully')
                if zz==0:
                    break
            else:
                m.showwarning('Blood','(total quantity of AB-,A-,B-,O-)is < Blood u want so,Blood is not AVAILABLE')
        elif i[0]=='AB+':
            c.execute('select abp from update_blood')
            mres1=c.fetchall()
            for j1 in mres1:
                t1=int(j1[0])
            c.execute('select abm from update_blood')
            mres2=c.fetchall()
            for j2 in mres2:
                t2=int(j2[0])
            c.execute('select op from update_blood')
            mres3=c.fetchall()
            for j3 in mres3:
                t3=int(j3[0])
            c.execute('select om from update_blood')
            mres4=c.fetchall()
            for j4 in mres4:
                t4=int(j4[0])
            c.execute('select ap from update_blood')
            mres5=c.fetchall()
            for j5 in mres5:
                t5=int(j5[0])
            c.execute('select am from update_blood')
            mres6=c.fetchall()
            for j6 in mres6:
                t6=int(j6[0])
            c.execute('select bp from update_blood')
            mres7=c.fetchall()
            for j7 in mres7:
                t7=int(j7[0])
            c.execute('select bm from update_blood')
            mres8=c.fetchall()
            for j8 in mres8:
                t8=int(j8[0])    
            t=int(i[1])
            if t<=0:
                continue    
            total=t1+t2+t3+t4+t5+t6+t7+t8    
            if t<=t1:
                m.showinfo('Blood','AB+ Blood is Received Successfully')
                c.execute('update update_blood set abp=%s',(t1-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t2:
                m.showinfo('Blood','AB+ is not available..so, AB- is Received Successfully')
                c.execute('update update_blood set abm=%s',(t2-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t3:
                m.showinfo('Blood','AB+ is not available..so,O+ is Received Successfully')
                c.execute('update update_blood set op=%s',(t3-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t4:
                m.showinfo('Blood','AB+ is not available..so,O- is Received Successfully')
                c.execute('update update_blood set om=%s',(t4-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t5:
                m.showinfo('Blood','AB+ is not available..so,A+ is Received Successfully')
                c.execute('update update_blood set ap=%s',(t5-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t6:
                m.showinfo('Blood','AB+ is not available..so,A- is Received Successfully')
                c.execute('update update_blood set am=%s',(t6-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t7:
                m.showinfo('Blood','AB+ is not available..so,B+ is Received Successfully')
                c.execute('update update_blood set bp=%s',(t7-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()
            elif t<=t8:
                m.showinfo('Blood','AB+ is not available..so,B- is Received Successfully')
                c.execute('update update_blood set bm=%s',(t8-t))
                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                d.commit()

            elif t<=total:
                zz=m.askyesno('Blood','Blood AB+ is not AVAILABLE..so,proceed a combination of blood\n yes=Proceed or no=EXIT')
                if zz==1:
                    b1=t1-t
                    c.execute('update update_blood set abp=%s',(t1-t1))
                    c.execute('update receiver set messurement="0" where blood_group="AB+"')
                    d.commit()
                    if b1<0:
                        b2=t2-abs(b1)
                        if b2<=0:
                            c.execute('update update_blood set abm=%s',(t2-t2))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        else:    
                            m.showinfo('Blood','Combination of AB+ and AB- are used..,Blood Received successfully')
                            c.execute('update update_blood set abm=%s',(t2-abs(b1)))
                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                            d.commit()
                        if b2<0:
                            b3=t3-abs(b2)
                            if b3<=0:
                                c.execute('update update_blood set op=%s',(t3-t3))
                                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                d.commit()
                            else:
                                m.showinfo('Blood','Combination of AB+,AB-and O+ are used..,Blood Received successfully')
                                c.execute('update update_blood set op=%s',(t3-abs(b2)))
                                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                d.commit()
                            if b3<0:
                                b4=t4-abs(b3)
                                if b4<=0:
                                    c.execute('update update_blood set om=%s',(t4-t4))
                                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                    d.commit()
                                else:
                                    m.showinfo('Blood','Combination of AB+,AB-,O+ and O- are used...,Blood Received successfully')
                                    c.execute('update update_blood set om=%s',(t4-abs(b3)))
                                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                    d.commit()          
                                if b4<0:
                                    b5=t5-abs(b4)
                                    if b5<=0:
                                        c.execute('update update_blood set ap=%s',(t5-t5))
                                        c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                        d.commit()
                                    else:
                                        m.showinfo('Blood','Combination of AB+,AB-,O+,O- and A+ are used...,Blood Received successfully')
                                        c.execute('update update_blood set ap=%s',(t5-abs(b4)))
                                        c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                        d.commit()          
                                    if b5<0:
                                        b6=t6-abs(b5)
                                        if b6<=0:
                                            c.execute('update update_blood set am=%s',(t6-t6))
                                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                            d.commit()
                                        else:
                                            m.showinfo('Blood','Combination of AB+,AB-,O+,O-,A+ and A- are used...,Blood Received successfully')
                                            c.execute('update update_blood set am=%s',(t6-abs(b5)))
                                            c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                            d.commit()
                                        if b6<0:
                                            b7=t7-abs(b6)
                                            if b7<=0:
                                                c.execute('update update_blood set bp=%s',(t7-t7))
                                                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                                d.commit()
                                            else:
                                                m.showinfo('Blood','Combination of AB+,AB-,O+,O-,A+,A- and B+ are used...,Blood Received successfully')
                                                c.execute('update update_blood set bp=%s',(t7-abs(b6)))
                                                c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                                d.commit()          
                                            if b7<0:
                                                b8=t8-abs(b7)
                                                if b8<=0:
                                                    m.showinfo('Blood','Combination of AB+,AB-,O+,O-,A+,A-,B+ and B- are used...,Blood Received successfully')
                                                    c.execute('update update_blood set bm=%s',(t8-t8))
                                                    c.execute('update receiver set messurement="0" where phone=%s',str(i[2]))
                                                    d.commit()
                if zz==0:
                    break
            else:
                m.showwarning('Blood','(total quantity of B+,B-,O+,O-)is < Blood u want so,Blood is not AVAILABLE')           
 ##### END OF BLOOD RECEIVING....
# 1)for search_bar..
def search():
    list1=['A+','A-','B+','B-','O+','O-','AB+','AB-','all']
    z=lb1entry.get()
    if z in list1:
        if z=='A+':
            c.execute('select ap from update_blood')
            result=c.fetchall()
            for i in result:
                m2=int(i[0])
            m.showinfo('Blood A+',f'Blood {z} ,Quantiy = {m2}')
        if z=='A-':
            c.execute('select am from update_blood')
            result=c.fetchall()
            for i in result:
                m2=int(i[0])
            m.showinfo('Blood A-',f'Blood {z} ,Quantiy = {m2}')
        if z=='B+':
            c.execute('select bp from update_blood')
            result=c.fetchall()
            for i in result:
                m2=int(i[0])
            m.showinfo('Blood B+',f'Blood {z} ,Quantiy = {m2}')
        if z=='B-':
            c.execute('select bm from update_blood')
            result=c.fetchall()
            for i in result:
                m2=int(i[0])
            m.showinfo('Blood B-',f'Blood {z} ,Quantiy = {m2}')
        if z=='O+':
            c.execute('select op from update_blood')
            result=c.fetchall()
            for i in result:
                m2=int(i[0])
            m.showinfo('Blood O+',f'Blood {z} ,Quantiy = {m2}')
        if z=='O-':
            c.execute('select om from update_blood')
            result=c.fetchall()
            for i in result:
                m2=int(i[0])
            m.showinfo('Blood O-',f'Blood {z} ,Quantiy = {m2}')
        if z=='AB+':
            c.execute('select abp from update_blood')
            result=c.fetchall()
            for i in result:
                m2=int(i[0])
            m.showinfo('Blood AB+',f'Blood {z} ,Quantiy = {m2}')
        if z=='AB-':
            c.execute('select abm from update_blood')
            result=c.fetchall()
            for i in result:
                m2=int(i[0])
            m.showinfo('Blood AB-',f'Blood {z} ,Quantiy = {m2}')
######2 for all blood_stock """""SEARCH 'all' """""""
        if z=='all':
            c.execute('select * from update_blood')
            result=c.fetchall()
            for i in result:
                ap=int(i[0])
                am=int(i[1])
                bp=int(i[2])
                bm=int(i[3])
                op=int(i[4])
                om=int(i[5])
                abp=int(i[6])
                abm=int(i[7])
            m.showinfo('Blood',f'_BLD_\t_QNTY_\n A+\t: {ap}\n A-\t: {am}\n B+\t: {bp}\n B-\t: {bm}\n O+\t: {op}\n O-\t: {om}\n AB+\t: {abp}\n AB-\t: {abm}')
# 2 till here
    else:
        m.showwarning('Blood',f'Blood {z} ,INVALID BLOOD GROUP')
        lb1entry.delete(0,'end')
# 1 till here
def update_receiver():#UI
    global bg1,lb1entry
    t5=Toplevel(bd=10,relief=SOLID)
    t5.title('Update_receiver_details')
    t5.geometry('900x700+200+20')
    t5.resizable(0,0)
    t5['bg']='light blue'
    n1=StringVar()
    lb1head=Label(t5,text='Update Receiver Details',font=('times new roman',30),relief=SOLID,width=35)
    lb1head.place(x=50,y=30)
    lb1label=Label(t5,width=12,text=' Blood_group :',font=('times new roman',12),relief=SOLID,bd=5)
    lb1label.place(x=170,y=120)
    lb1button=Button(t5,text='SEARCH',width=20,bg='red',relief=SUNKEN,bd=5,command=search)
    lb1button.place(x=470,y=120)
    lb1entry=Entry(t5,width=20,font=('times new roman',12),textvariable=n1,bg='cyan',relief=SOLID,bd=5)
    lb1entry.place(x=290,y=120)
    lb1name=Label(t5,width=12,text=' Name ',font=('times new roman',15),bg='black',fg='white',)
    lb1name.place(x=150,y=170)
    lb1phone=Label(t5,width=12,text=' phone ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1phone.place(x=290,y=170)
    lb1blood=Label(t5,width=12,text=' Blood_group ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1blood.place(x=430,y=170)
    lb1messure=Label(t5,width=12,text=' Messurement ',font=('times new roman',15),relief=SOLID,bg='black',fg='white')
    lb1messure.place(x=570,y=170)
    
    c.execute('select * from receiver')
    result=c.fetchall()
    num=200
# for nothing to update comment...
    c.execute('select messurement from receiver')
    res=c.fetchall()
    x=0
    for r in res:
        x=x+int(r[0])
    if x==0:
        m.showinfo('On branch ADMIN','Nothing to update No one is requested yet!')
#till here
#print details of receiver if anything is pending for update        
    for i in result:
        if int(i[6])==0:
            continue
        else:
            lb2name=Label(t5,text=i[0],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
            lb2name.place(x=150,y=num)
            lb2phone=Label(t5,text=i[3],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
            lb2phone.place(x=290,y=num)
            lb2blood=Label(t5,text=i[5],font=('times new roman',15),relief=SOLID,width=12,fg='red')
            lb2blood.place(x=430,y=num)
            lb2messure=Label(t5,text=i[6],font=('times new roman',15),relief=SOLID,width=12,fg='blue')
            lb2messure.place(x=570,y=num)
            num+=30
    lb2button=Button(t5,text='Update',font=('times new roman',20),relief=SUNKEN,bd=5,width=15,bg='red',fg='white',command=receiverblood)
    lb2button.place(x=300,y=450)    
    t5.mainloop()    


