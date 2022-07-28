import tkinter as tk 
import mysql.connector

def func():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="",
	  database='user'
	)
	mycursor = mydb.cursor()

	user=usernam.get()
	passe=password.get()
	sql=f'Select * from user where username like "{user}" and password like "{passe}"'
	mycursor.execute(sql)
	myresult=mycursor.fetchall()
	msgLabel=tk.Label(window)
	if len(myresult)>=1:
		msgLabel.config(text='Login succeded')
	else:
		msgLabel.config(text='Login Failed')
	msgLabel.grid(row=3,column=0)
	

window=tk.Tk()

label1=tk.Label(window, text='Username : ')
label1.grid(row=0,column=0)

usernam=tk.StringVar()
password=tk.StringVar()

Entry1=tk.Entry(window,textvariable=usernam)
Entry1.grid(row=0,column=1)

label2=tk.Label(window, text='Password : ')
label2.grid(row=1,column=0)

Entry2=tk.Entry(window,textvariable=password)
Entry2.grid(row=1,column=1)

btn=tk.Button(window, text='Login',command=func)
btn.grid(row=2,column=1)


window.mainloop()