import mysql.connector as a
con=a.connect(host="localhost", user="root",password="")
c=con.cursor()
sql1="create database rms"
c.execute(sql1)
sql2="use rms"
c.execute(sql2)
sql3="create table checkin (days varchar(50),names varchar(20), aadhar varchar(20), date varchar(20), typenumber varchar(20))"
c.execute(sql3)
sql4="create table checkout (typenumber varchar(20), guests integer, fare integer, days integer, tbill integer, date varchar(20))"
c.execute(sql4)
con.commit()