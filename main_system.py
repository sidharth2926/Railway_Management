# Railway reservation management system
#Connecting MYSQL to IDLE
import random 
import mysql.connector as a
pwd=input("Enter Database password:")
con=a.connect(host="localhost",
              user="root",
              password=pwd)
#Checking Connection
'''if con.is_connected:
    print("Connection Successful")'''
#Creating cursor
c=con.cursor()
#Creating database if exists
sql="create database if not exists Railway"
#Using database
c.execute(sql)
sql1="use Railway"
c.execute(sql1)
#Creating basic tables
sql2="create table if not exists train(Name varchar(100),Fair Decimal(20,2),Distance integer,A_date date,Route varchar(100))"
c.execute(sql2)
sql3="create table if not exists passenger(Name varchar(100),Train varchar(100),Fair Decimal(20,2),R_date date,Phoneno varchar(15),PNRno integer(10))"
c.execute(sql3)
sql4="create table if not exists Bills(BILLno integer(10),Btype varchar(100),SubDate date,T_cost decimal(20,2),B_Status varchar(20))" 
c.execute(sql4)
sql5="create table if not exists worker(Name varchar(100),Post varchar(100),Salary Decimal(20,2),gender char(1),W_id varchar(20))"
c.execute(sql5)
con.commit()

#System password login
def signin():
    print("\n")
    print("              ---------->>>>>WELCOME TO INDIAN RAILWAYS<<<<<----------")
    print("\n")
    print("For management login press M")
    print("For user login press U")
    #Adding trains to table
    def Addtrains():
        n=input("Enter train name:")
        ct=int(input("Enter ticket fare:"))
        d=int(input("Enter distance in kilometers:"))
        dat=input("Enter date in format YYYY-MM-DD:")
        r=input("Enter train route")
        s="insert into train values('{}',{},{},'{}','{}')".format(n,ct,d,dat,r)
        c.execute(s)
        con.commit()
        print("Train added successfully")
    def Dtrain():
        sql="select * from train"
        c.execute(sql)
        s=c.fetchall()
        for i in s:
            try:
                print("         ----------<<<<<<<<<<*****>>>>>>>>>>----------")
                print("Name:",i[0])
                print("Fare:",i[1])
                print("Distance:",i[2])
                print("Date:",i[3])
                print("Route:",i[4])
                print("......................................................")
            except:
                pass
        optionm()
    def Addbills():
        n=int(input("Enter bill number:"))
        t=input("Enter bill type:")
        v=input("Enter date of subbmission in foramt YYYY-MM-DD:")
        y=int(input("Enter total cost:"))
        x=input("Enter bill status")
        s="insert into bills values({},'{}','{}',{},'{}')".format(n,t,v,y,x)
        c.execute(s)
        con.commit()
        print("Bill added successfully")
    def Dbills():
        n=int(input("Enter bill number:"))
        f="select * from bills"
        c.execute(f)
        x=c.fetchall()
        for i in x:
            try:
                print("         ----------<<<<<<<<<<*****>>>>>>>>>>----------")
                print("This is",i[1])
                print("Submission date:",i[2])
                print("Total cost is:",i[3])
                print("Bill status:",i[4])
                print("......................................................")
            except:
                pass
    def Addworkers():
        n=input("Enter name of worker:")
        p=input("Enter post of worker:")
        s=int(input("Enter salary of worker:"))
        g=input("Enter gender of worker:")
        b="insert into worker (name,post,salary,gender) values('{}','{}',{},'{}')".format(n,p,s,g)
        c.execute(b)
        con.commit()
        x=random.randrange(1000000000,9999999999)
        z=str(x)
        print("Worker id:",z)
        j="update worker set W_id='{}' where Name='{}'".format(z,n)
        c.execute(j)
        con.commit()
        print("Worker Details added successfully")
    def Dworkers():
        a=input("Enter worker id:")
        b="select * from worker where W_id='{}'".format(a)
        c.execute(b)
        x=c.fetchall()
        for i in x:
            try:
                print("         ----------<<<<<<<<<<*****>>>>>>>>>>----------")
                print("Name of worker is:",i[0])
                print("Post of worker is:",i[1])
                print("Salary of worker is:",i[2])
                print("Gender:",i[3])
                print("......................................................")
            except:
                pass
    def Dpayments():
        n=input("Enter PNR number of passenger:")
        Sql="select * from passenger where pnrno='{}'".format(n)
        c.execute(Sql)
        d=c.fetchall()
        for i in d:
            print("Name of passenger",i[0])
            print("Reserved train:",i[1])
            print("Reservation Date:",i[3])
            print("Phone number:",i[4])
            print("Total bil inc GST:",i[2])
            print(".............................................")
    ch=input("Enter your choice")
    if ch=="M" or ch=="m":
        pwd=input("Enter management password")
        if pwd=="localtrain":
            print("Login successful")
            optionm()
        while True:
            choice=int(input("Select your choice"))
            if choice==1:
                Addtrains()
            if choice==2:
                Addbills()
            if choice==3:
                Addworkers()
            if choice==4:
                Dtrain()
            if choice==5:
                Dpayments()
            if choice==6:
                Dbills()
            if choice==7:
                Dworkers()
            if choice==8:
                print("Thank you ----INDIAN RAILWAYS---")
                break
    elif ch=="U" or ch=="u":
        pwd=input("Enter user password")
        if pwd=="user123":
            print("Login successful")
        optionp()
        #Checking availability status
        def chkavb():
            a=input("Enter source place")
            b=input("Enter destination")
            c=input("Enter date in fromat YYYY-MM-DD")
            print("Checking for availability...............")
            print("Availability status sent on your email by management")
        #Booking train
        def Booktrain():
            n=input("Enter name of passenger:")
            t=input("Enter journey train name:")
            f=int(input("Enter ticket fare:"))
            r=input("Enter reservation date in format YYYY-MM-DD:")
            ph=int(input("Enter phone number:"))
            g=input("Gender of passenger")
            Sq="insert into passenger (Name,train,fair,R_date,phoneno,gender)values('{}','{}',{},'{}',{},'{}')".format(n,t,f,r,ph,g)
            c.execute(Sq)
            con.commit()
            x=random.randrange(1000000000,9999999999)
            z=str(x)
            print("Your PNR number is:",z)
            j="update passenger set PNRno='{}' where Name='{}'".format(z,n)
            c.execute(j)
            con.commit()
            print("Ticket booked successfully")
        def chkconf():
            print("Checking for conformation..........")
            print("Confirmation status sent on your email by management")
        def chkpay():
            n=input("Enter PNR number of passenger:")
            s="select * from passenger where PNRno='{}'".format(n)
            c.execute(s)
            d=c.fetchall()
            for i in d:
                try:
                    print("Train name:",i[1])
                    print("Reservation date:",i[3])
                    print("Payment done including all taxes:",i[2])
                except:
                    pass
            optionp()
        def cancell():
            a=int(input("Enter PNR number of passenger:"))
            b=int(input("Enter phone number"))
            s="delete from passenger where PNRno={} and phoneno={}".format(a,b)
            c.execute(s)
            con.commit()
            print("Ticket cancelled successfully")
        while True:
            choice=int(input("Select your choice"))
            if choice==1:
                chkavb()
            if choice==2:
                Booktrain()
            if choice==3:
                chkconf()
            if choice==4:
                chkpay()
            if choice==5:
                cancell()
            if choice==6:
                print("Thank you ----INDIAN RAILWAYS---")
                break
    else:
        print("Access Denied")
        print("Signin again")
        signin()
#Project working options
def optionm():
    print("""
                      HOME PAGE
                      1.     Add Trains
                      2.     Add Bill
                      3.     Add Worker
                      4.     Display Trains
                      5.     Display Payments
                      6.     Display Bills
                      7.     Display Workers
                      8.     Exit 
        """)
def optionp():
    print("""
                      HOME PAGE
                      1.Check availability
                      2.Book train
                      3.Check conformation
                      4.Check payments
                      5.Ticket cancelling
                      6.EXIT
        """)
signin()
