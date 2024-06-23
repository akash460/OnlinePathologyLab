#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
f=cgi.FieldStorage()
a=f.getvalue("a1")
b=f.getvalue("a2")
c=f.getvalue("a3")
d=f.getvalue("a4")
g=f.getvalue("a5")
e=int(f.getvalue("id"))
cur.execute("update pregister set name='%s',email='%s',gender='%s',phone='%s',password='%s' where id=%d" %(a,b,c,d,g,e))
db.commit()
db.close()

print("location:pprofile.py?id=%s\r\n\r\n"%(b))