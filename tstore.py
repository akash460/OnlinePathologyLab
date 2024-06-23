#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
f =cgi.FieldStorage()
a =f.getvalue('a1')
b =f.getvalue('a2')
c =f.getvalue('a3')
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
cur.execute("insert into test(testname,description,price)values('%s','%s','%s')"%(a,b,c))
db.commit()
print("location:adminprofile.py?msg=done\r\n\r\n")


