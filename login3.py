#!C:\Users\A\AppData\Local\Programs\Python\Python38\python.exe
#print('Content-type:text/html\r\n\r\n')
import cgi
f =cgi.FieldStorage()
a=f.getvalue('a1')
b=f.getvalue('a2')
c="AKASH"
d="gupta@123"
y=0
if c==a and d==b:
    y=1
    
else:
    y=0


if y==1:
    print("location:adminprofile.py?id=%s\r\n\r\n"%(a))   
else:
    print("location:alogin.html\r\n\r\n")