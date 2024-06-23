#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
import mysql.connector

if (id!="null"):
    db = mysql.connector.connect(host="localhost", user="root", passwd="", db="project")
    cur = db.cursor()
    f = cgi.FieldStorage()
    id = int(f.getvalue('id'))
    cur.execute("select * from dregister where id=%d" % (id))
    r = cur.fetchone()
    print("""
      <html>
      <head>
        <center>
    	<style type="text/css">
    	.option{
    	        position:relative;
    			left:130px;
    			top:-37px:
    	  </style>
          <font size="8" color="#CCCCCC">
              <b> <br> Registration Form <br> <br> </br> </font>
          </head>
      <body bgcolor="#006699">
     <form method="post"  action="dupdate.py">
     
       <table>
          <tr>
    	    <td>
    		  <font size="5" color="#CCCCCC"> <b>
    		  
        Name:
    	
    	</td>
    	<td>
    	      <input type="text" name="a" value="%s">
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
             <input type="mail" name="c" value="%s">
    	</td>
    	</tr>
    	<tr>
    	<td> <br>
    	       <font size="5" color="#CCCCCC"> <b>
    	Password:
    	
    	</td>
    	<td> <br>
    	      <input type="Password" name="d" value="%s">
    	</td>
    	</tr>
        <tr>
        <td> <br>
               <font size="5" color="#CCCCCC"> <b>
    		   
        	Phone No.:
    			
    	</td>
    	<td> <br>
             <input type="Phone" name="e" value="%s">
    	</td>
    	</tr>
        <tr>
        <td> <br>
    	       <font size="5" color="#CCCCCC"> <b>
    		
    		
    
    		<label for="Qualification">Qualification: </label>
                    <select class="option" name="f">
    				<option disabled="disabled" selected="selected">--Choose Option</option>
                    <option value="MBBS">MBBS</option>
                    <option value="MD pathology">MD Pathology</option>
                    <option value="DNB">DNB</option>
                    <option value="DPB">DPB</option>
                    </select> <br>
    		
    	<tr>
    	<td> <br>
    	       <font size="5" color="#CCCCCC"> <b>
    		     
    			Specialisation:
    			
    	</td>
    	<td>
    	      <input type="text" name="g" value="pathology">
    	</td>
    	</tr>
    	<tr>
    	<td> <br>
        <input type="hidden" name="id" value="%d">
    	    <input type="Submit" name="">
    	</td>
    	</tr>
    	</table>
    	</form>
    	 </body>
    	 </html>
         """ % (r[1], r[3], r[4], r[5], r[0]))
else:
    print("""
      <html>
      <head>
        <center>
    	<style type="text/css">
    	.option{
    	        position:relative;
    			left:130px;
    			top:-37px:
    	  </style>
          <font size="8" color="#CCCCCC">
              <b> <br> Registration Form <br> <br> </br> </font>
          </head>
      <body bgcolor="#006699">
     <form action="Dregstoring.py">
     
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
    	       <font size="5" color="#CCCCCC"> <b>
    	Password:
    	
    	</td>
    	<td> <br>
    	      <input type="Password" name="d">
    	</td>
    	</tr>
        <tr>
        <td> <br>
               <font size="5" color="#CCCCCC"> <b>
    		   
        	Phone No.:
    			
    	</td>
    	<td> <br>
             <input type="Phone" name="e">
    	</td>
    	</tr>
        <tr>
        <td> <br>
    	       <font size="5" color="#CCCCCC"> <b>
    		
    		
    
    		<label for="Qualification">Qualification: </label>
                    <select class="option" name="f">
    				<option disabled="disabled" selected="selected">--Choose Option</option>
                    <option value="MBBS">MBBS</option>
                    <option value="MD pathology">MD Pathology</option>
                    <option value="DNB">DNB</option>
                    <option value="DPB">DPB</option>
                    </select> <br>
    		
    	<tr>
    	<td> <br>
    	       <font size="5" color="#CCCCCC"> <b>
    		     
    			Specialisation:
    			
    	</td>
    	<td>
    	      <input type="text" name="g" value="pathology">
    	</td>
    	</tr>
    	<tr>
    	<td> <br>
    	    <input type="Submit" name="">
    	</td>
    	</tr>
    	</table>
    	</form>
    	 </body>
    	 </html>
         """)
