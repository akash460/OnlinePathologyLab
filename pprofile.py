#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
f =cgi.FieldStorage()
email =f.getvalue('id')
cur.execute("select * from aregister where email='%s'" %(email))
s=cur.fetchall()
print("""
<html>
<head>
<link rel="stylesheet" type="text/css" href="table.css"></head>
<body>
<img src="logo1.png">
<table>
<tr>
<td> <a href="index.html">Home</a></td>
<td> <a href="plogin.html">Patient</a></td>
<td> <a href="dlogin.html">Doctors</a></td>
<td> <a href="aregister.py">Appoinment</a></td>
</tr>
</table>
<p align="right"><a href="index.html">Log_out</a></p>
<br>
<br>
<br>
<div style="width: 48%; float: right; float: up;">
<table border="2" bgcolor="aqua">
""")
for j in s:
        print(
            """<b><tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td> %s </td> <td> %s </td><td> %s </td><td> %s </td><td><a href =" adelete.py?id=%d">delete</a></td><td></tr><b>""" %(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[0],j[0]))
print("""
</table>
</div>
</body> 
""")
cur.execute("select * from pregister where email='%s'"%(email))
t=cur.fetchall()
print("""
<html>
<body>
<br>
<br>
<br>
<form>
<font size="8">
<body bgcolor="#006699">
""")
for i in t:
        print(
            """<b>ID:- %s <br>Name:- %s <br>Email:-  %s <br> <button><a href="pedit.py?id=%d">editprofile></a></button><br><br></b>""" %(i[0],i[1],i[2],i[0]))
print(""" 
</form>                 
</body>
</html>
""")
cur.execute("select * from booked where email='%s'" %(email))
p=cur.fetchall()
print("""
<html>
<body>
<br>
<br>
<br>
<div style="width: 48%;">
<table border="2" bgcolor="aqua">
""")
for k in p:
        print(
            """<b><tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td> %s </td> <td> %s </td><td><a href =" bdelete.py?id=%d">delete</a></td></tr><b>""" %(k[1],k[2],k[3],k[4],k[5],k[6],k[0]))
print("""
</table>
</div>
</body> 
""")

