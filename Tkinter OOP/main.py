import tkinter as tk

class Window:
	n=0
	def __init__(self, root, title, geometry, message):
		self.root=root
		self.root.title(title)
		self.root.geometry(geometry)
		self.label=tk.Label(self.root, text=str(self.n))
		self.label.pack()
		btn=tk.Button(self.root, text='increment', command=self.increment)
		btn.pack()
		self.root.mainloop()
		pass

	def increment(self):
		self.n+=1
		self.label.config(text=self.n)

	pass

root=tk.Tk()
window=Window(root, 'Tkinter OOP', '500x500', 'Hello World')
