import tkinter as tk
import random

messages=[	"Stop Talking too much","Never get into a conversation about something you don't know" ]
msg=messages[random.randint(0,len(messages)-1)]
root=tk.Tk('Reminders')
label=tk.Label(root,text=msg,font=("Arial", 25))
label.pack()
root.mainloop()