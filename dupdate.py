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
h=f.getvalue("a6")
i=f.getvalue("a7")


e=int(f.getvalue("id"))
cur.execute("update dregister set name='%s',gender='%s',email='%s',password='%s',phone='%s',qualification='%s',specialisation='%s' where id=%d" %(a,b,c,d,g,h,i,e))
db.commit()
db.close()

print("location:dprofile.py?id=%s\r\n\r\n"%(c))