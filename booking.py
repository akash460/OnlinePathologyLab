#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="project")
cur=db.cursor()
t =cgi.FieldStorage()
id =int(t.getvalue('id'))
cur.execute("select * from test where tid=%d"%(id))
r=cur.fetchone()
db.commit()
print("""
    <html>
    <head>
    <link rel="stylesheet" type="text/css" href="image.css">
	    <style type="text/css">
	    .option{
	        position:relative;
			left:130px;
			top:-37px:
	  </style>
      </head>
  <body bgcolor="#006699">
 <form action="bookstoring.py">
 <img src="logo1.png">
<table font-size="5">
<tr>
<td> <a href="index.html">Home</a></td>
<td> <a href="plogin.html">Patient</a></td>
<td> <a href="dlogin.html">Doctors</a></td>
<td> <a href="aregister.py">Appoinment</a></td>
</tr>
</table>
<center>
 <font size="8" color="#CCCCCC">
          <b> <br> Test Booking Form <br> <br> </br> </font>
 
   <table>
      <tr>
	    <td>
		  <font size="5" color="#CCCCCC"> <b>
		  
    Name:
	
	</td>
	<td>
	      <input type="text" name="a">
	</td>
	</tr>
	<tr>
	<td> <br>
	       <font size="5" color="#CCCCCC"> <b>
		  
    Gender:
	
	</td>
	
	
	<td> 
	     <input type="radio" name="b" value="male"><font size="4" color="#CCCCCC"> <b>
	Male
	 
	     <input type="radio" name="b" value="female">
	Female
	
	</td>
	</tr>
	
	<tr> 
	<td> <br>
	     <font size="5" color="#CCCCCC"> <b>
		
	   Email:
		
	</td>
	<td> <br>
         <input type="mail" name="c">
	</td>
	</tr>
	<tr>
	
	<td> <br>
	      <input type="hidden" name="d" value="%s">
	</td>
	</tr>
    <tr>
    <td> <br>
           <font size="5" color="#CCCCCC"> <b>
		   
    	Test Name:
			
	</td>
	<td> <br>
         <input type="text" name="e" value="%s">
	</td>
	</tr>
    <tr>
    
	<td> <br>
	       <font size="5" color="#CCCCCC"> <b>
		     
			Test Price:
			
	</td>
	<td>
	      <input type="text" name="f" value="%s">
	</td>
	</tr>
	<tr>
	<td> <br>
	    <input type="Submit" name="">
	</td>
	</tr>"""%(r[0],r[1],r[3]))
print("""
	</table>
	</form>
	</body>
	</html>
""")