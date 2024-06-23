#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
f=cgi.FieldStorage()
id=int(f.getvalue('id'))
cur.execute("select * from test where tid=%d"%(id))
r=cur.fetchone()
print("""
<html>
<body>
<img src="logo1.png" style="width:100%;height:150px">
<table font-size="5">
<tr>
<td> <a href="index.html">Home</a></td>
<td> <a href="plogin.html">Patient</a></td>
<td> <a href="dlogin.html">Doctors</a></td>
<td> <a href="aregister.py">Appoinment</a></td>
</tr>
</table>
<p align="right"><a href="index.html">Log_out</a></p>
<form method ="post" action="tupdate.py">
<input type ="text" name="a1" value="%s">
<input type ="textarea" name="a2" value="%s">
<input type ="text" name="a3" value="%s">

<input type ="hidden" name="id" value="%d">
<input type ="submit">
</form>
</body>
</html>
""" %(r[1],r[2],r[3],r[0]))