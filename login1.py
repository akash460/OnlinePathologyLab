#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
f =cgi.FieldStorage()
a=f.getvalue('a1')
b=f.getvalue('a2')
cur.execute("select * from pregister")
q=cur.fetchall()
y=0
for i in q:
    if i[2]==a and i[5]==b:
        y=1
        c=i[0]
        break
    else:
        y=0


if y==1:
    print("location:pprofile.py?id=%s\r\n\r\n"%(a))   
else:
    print("location:plogin.html\r\n\r\n")
    