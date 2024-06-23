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
e=int(f.getvalue("id"))
cur.execute("update test set testname='%s',description='%s',price='%s' where tid=%d" %(a,b,c,e))
db.commit()
db.close()

print("location:adminprofile.py?\r\n\r\n"%(c))