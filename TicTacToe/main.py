import tkinter as tk

class MyButton(tk.Button):
	def __init__(self,parent,player,**kwargs):
		super().__init__(parent,**kwargs)
		self.player=player

class Window:
	def __init__(self,root,title,geometry):
		self.root=root
		self.root.title(title)
		self.root.geometry(geometry)

		self.turn=1

		self.resultLabel=tk.Label(self.root,text='TicTacToe')
		self.resultLabel.grid(row=0,column=0)

		self.frame1=tk.Frame(self.root)
		self.array=[[0,0,0],[0,0,0],[0,0,0]]

		self.array[0][0]=MyButton(self.frame1,text=f'{0},{0}',command=lambda:self.change([0,0]),player=3)
		self.array[0][1]=MyButton(self.frame1,text=f'{0},{1}',command=lambda:self.change([0,1]),player=4)
		self.array[0][2]=MyButton(self.frame1,text=f'{0},{2}',command=lambda:self.change([0,2]),player=5)
		self.array[1][0]=MyButton(self.frame1,text=f'{1},{0}',command=lambda:self.change([1,0]),player=6)
		self.array[1][1]=MyButton(self.frame1,text=f'{1},{1}',command=lambda:self.change([1,1]),player=7)
		self.array[1][2]=MyButton(self.frame1,text=f'{1},{2}',command=lambda:self.change([1,2]),player=8)
		self.array[2][0]=MyButton(self.frame1,text=f'{2},{0}',command=lambda:self.change([2,0]),player=9)
		self.array[2][1]=MyButton(self.frame1,text=f'{2},{1}',command=lambda:self.change([2,1]),player=10)
		self.array[2][2]=MyButton(self.frame1,text=f'{2},{2}',command=lambda:self.change([2,2]),player=11)


		for i in range(3):
			for j in range(3):
				image=tk.PhotoImage(file='empty.png').subsample(4,4)
				self.array[i][j].config(image=image)
				self.array[i][j].image=image
				self.array[i][j].grid(row=i,column=j)


		self.frame1.grid(row=1,column=0)

		self.frame2=tk.Frame(self.root)
		
		image1=tk.PhotoImage(file='cross.png').subsample(4,4)
		self.player1Lbl=tk.Label(self.frame2,text='Player1',image=image1,compound=tk.RIGHT)
		image2=tk.PhotoImage(file='circle.png').subsample(4,4)
		self.player2Lbl=tk.Label(self.frame2,text='Player2',image=image2,compound=tk.RIGHT)
		self.player1Lbl.grid(row=0,column=0)
		self.player2Lbl.grid(row=0,column=1)

		self.frame2.grid(row=2,column=0,pady=15)


		self.root.mainloop()

	def change(self,index):
		if self.turn==1:
			image=tk.PhotoImage(file='cross.png').subsample(4,4)
		elif self.turn==2:
			image=tk.PhotoImage(file='circle.png').subsample(4,4)

		self.array[index[0]][index[1]].config(image=image)
		self.array[index[0]][index[1]].image=image
		self.array[index[0]][index[1]].player=self.turn

		

		if self.check()==True:
			self.resultLabel.config(text=f'Player{self.turn} Win!')
			for i in range(3):
				for j in range(3):
					self.array[i][j].config(state=tk.DISABLED)
		elif self.check_draw()==True:
			self.resultLabel.config(text=f'Draw!')
			for i in range(3):
				for j in range(3):
					self.array[i][j].config(state=tk.DISABLED)

		if self.turn==1:
			self.turn=2
		else:
			self.turn=1

	def check(self):
		for i in range(3):
			if self.array[i][0].player==self.array[i][1].player==self.array[i][2].player:
				return True
		for j in range(3):
			if self.array[0][j].player==self.array[1][j].player==self.array[2][j].player:
				return True
		if self.array[0][0].player==self.array[1][1].player==self.array[2][2].player:
				return True
		if self.array[0][2].player==self.array[1][1].player==self.array[2][0].player:
					return True
		return False

	def check_draw(self):
		for i in range(3):
			for j in range(3):
				if self.array[i][j].player not in [1,2]:
					return False
		return True





root=tk.Tk()

Window(root,'TicTacToe','145x200')
