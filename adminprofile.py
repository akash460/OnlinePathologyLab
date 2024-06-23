#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
cur.execute("select * from pregister")
t=cur.fetchall()
print("""
<html>
<head>
<link rel="stylesheet" type="text/css" href="table.css">
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
<form  >
<font size="8">
<body bgcolor="#006699">
<center>
<table border="2" width="70%" bgcolor="aqua">
<th> Patient Details:- </th></center>
""")
for i in t:
    print(
        """<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td> %s </td> <td> %s </td><td><a href =" del.py?id=%d">delete</a></td><td> <a href="pedit.py?id=%d">edit</a></td></tr>""" %(i[0],i[1],i[2],i[3],i[4],i[5],i[0],i[0]))
print("""
</table>
</form>                 
</body>
</html>
""")
cur.execute("select * from dregister")
t=cur.fetchall()
print("""
<html>
<body>
<br>
<form  >
<font size="8">
<body bgcolor="#006699">
<table border="2" width="70%" bgcolor="aqua">
<center><th> Doctor Details:- </th></center>
""")
for i in t:
    print(
        """<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td> %s </td> <td> %s </td><td> %s </td> <td> %s </td><td><a href =" ddelete.py?id=%d">delete</a></td><td> <a href="dedit.py?id=%d">edit</a></td></tr>""" %(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0],i[0]))
print("""
</table>
</form>                 
</body>
</html>
""")
cur.execute("select * from aregister ")
s=cur.fetchall()
print("""
<html>
<body>
<br>
<br>
<br>
<div >
<table border="2" width="70%"bgcolor="aqua">
<th> Apointment Details:- </th>
""")
for j in s:
        print(
            """<b><tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td> %s </td> <td> %s </td><td> %s </td><td> %s </td><td>%s</td><td><a href =" del.py?id=%d">delete</a></td><td> <a href="edit.py?id=%d">Accept Appointment</a></td></tr><b>""" %(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[0],j[0]))
print("""
</table>
</div>
</body> 
""")
cur.execute("select * from test ")
v=cur.fetchall()
print("""
<html>
<body>
<br>
<br>
<br>
<div >
<table border="2" width="70%"bgcolor="aqua">
<th> Test Details:- </th>
""")
for k in v:
        print(
            """<b><tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><a href =" tdelete.py?id=%d">delete</a></td><td><a href =" tedit.py?id=%d">edit</a></td></tr><b>""" %(k[0],k[1],k[2],k[3],k[0],k[0]))
print("""
</table>
</div>
</body> 
""")
print("""
<html>
<body>
<form action="addtest.html">
<input type="submit" value="Add New Test">
</form>
</body>
</html>
""")
cur.execute("select * from booked ")
y=cur.fetchall()
print("""
<html>
<body>
<br>
<br>
<br>
<div >
<table border="2" width="70%"bgcolor="aqua">
<th> Booked Test Details:- </th>
""")
for l in y:
        print(
            """<b><tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td> %s </td> <td> %s </td><td> %s </td></tr><b>""" %(l[0],l[1],l[2],l[3],l[4],l[5],l[6]))
print("""
</table>
</div>
</body> 
""")
