import mysql.connector as a
con=a.connect(host="localhost", user="root", password="", database="rms")

def checkin():
    d=input("Days:")
    g=input("Names:")
    a=input("Aadhar:")
    dt=input("Date:")
    b=input("Type & Number:")
    data=(d,g,a,dt,b)
    sql='insert into checkin values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Scessfully")
    main()

def checkout():
    b=input("Type & Number :")
    tg=int(input("Guest"))
    f=int(input("Fare:"))
    d=int(input("Days:"))
    bl=f*d*tg
    cod=input("Date:")
    data=(b,tg,f,d,bl,cod)
    sql="insert into checkout values(%s,%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    main()

def rooms():
    pass

def main():
    print("Enter 1 for room ")
    print("Enter 2 for checkin")
    print("Enter 3 for checkout")
    x=int(input())
    if x==1:
        rooms()
    elif x==2:
        checkin()
    elif x==3:
        checkout()
    else:
        print("Abe Jahil Sahi se Number Daal")

main()
