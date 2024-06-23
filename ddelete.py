#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
f=cgi.FieldStorage()
id=int(f.getvalue('id'))
cur.execute("delete from dregister where id=%d"%(id))
db.commit()
print("location:adminprofile.py?msg=done\r\n\r\n")
