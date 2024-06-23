#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
f =cgi.FieldStorage()
a=f.getvalue('a1')
b=f.getvalue('a2')
cur.execute("select * from dregister")
q=cur.fetchall()
y=0
for i in q:
    if i[3]==a and i[4]==b:
        y=1
        break
    else:
        y=0


if y==1:
    print("location:dprofile.py?id=%s\r\n\r\n"%(a))   
else:
    print("location:dlogin.html\r\n\r\n")