#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
cur.execute("select * from test")
r=cur.fetchall()
db.commit()
print("""
    <html>
    <head>
    <img src="logo1.png" style="width:100%;height:150px">
<table font-size="5">
<tr>
<td> <a href="index.html">Home</a></td>
<td> <a href="plogin.html">Patient</a></td>
<td> <a href="dlogin.html">Doctors</a></td>
<td> <a href="aregister.py">Appoinment</a></td>
</tr>
</table>
    <body style="background-color:#006699;>
    
    <font size = "5" color="CCCCCC" >
    <h1 align= "center"> BOOK YOUR TEST NOW </h1>
<center>    
	<table border= "1px double black" align= "center" cellspacing= "10" cellpadding= "10">
""")
for i in r:
    print("""    
	     <tr align= "center">
		 <td>
         <form action="booking.py">
		 <font color="CCCCCC" > 
		 <h2> %s <h2> <br>
		 <h4> <p> %s </h4></p>
		 <font color="000000" > <b> <u>Price %s</b></u>
         <input type="hidden" name="id" value="%s">
		 <input type="submit" value="Book Now">
         </form>
		 </td>
         """%(i[1],i[2],i[3],i[0]))
print("""
    </table>
    </form>
    </html>
""")
