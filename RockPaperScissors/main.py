import tkinter as tk 
import random 

class Window:

	def __init__(self,root,title,geometry):
		self.root=root
		self.root.title(title)
		self.root.geometry(geometry)

		self.player1Score=0
		self.computerScore=0

		self.scoreLbl=tk.Label(self.root,text='Score : 0 - 0')
		self.scoreLbl.grid(row=0,column=0,pady=10,padx=5)

		self.frame1=tk.Frame(self.root)

		self.player1Lbl=tk.Label(self.frame1,text='Player1')
		self.player1Lbl.grid(row=1,column=0)

		photoC1=tk.PhotoImage(file='rock.png').subsample(10,10)
		self.player1ChoiceLbl=tk.Label(self.frame1,image=photoC1)
		self.player1ChoiceLbl.grid(row=1,column=1)

		photoC2=tk.PhotoImage(file='rock.png').subsample(10,10)
		self.player2ChoiceLbl=tk.Label(self.frame1,image=photoC2)
		self.player2ChoiceLbl.grid(row=1,column=2)

		self.player2Lbl=tk.Label(self.frame1,text='Computer')
		self.player2Lbl.grid(row=1,column=3)

		self.frame1.grid(row=1,column=0,pady=10,padx=5)

		self.frame2=tk.Frame(self.root)

		self.photo1=tk.PhotoImage(file='rock.png').subsample(10,10)
		self.rockBtn=tk.Button(self.frame2,image=self.photo1,command=lambda:[self.setOption(self.photo1)])
		self.photo2=tk.PhotoImage(file='scissor.png').subsample(10,10)
		self.paperBtn=tk.Button(self.frame2,image=self.photo2,command=lambda:[self.setOption(self.photo2)])
		self.photo3=tk.PhotoImage(file='paper.png').subsample(10,10)
		self.scissorBtn=tk.Button(self.frame2,image=self.photo3,command=lambda:[self.setOption(self.photo3)])

		self.rockBtn.grid(row=0,column=0)
		self.paperBtn.grid(row=0,column=1)
		self.scissorBtn.grid(row=0,column=2)

		self.frame2.grid(row=2,column=0,pady=10,padx=5)

		self.root.mainloop()

	def setOption(self,playerChoice):
		self.player1ChoiceLbl.config(image=playerChoice)
		photos=[self.photo1,self.photo2,self.photo3]
		computerChoice=photos[random.randint(0,2)]
		self.player2ChoiceLbl.config(image=computerChoice)
		rock=self.photo1
		scissor=self.photo2
		paper=self.photo3
		if computerChoice==rock and playerChoice==paper:
			self.player1Score+=1
			self.scoreLbl.config(text=f'Score : {self.player1Score} - {self.computerScore}')
		elif computerChoice==rock and playerChoice==scissor:
			self.computerScore+=1
			self.scoreLbl.config(text=f'Score : {self.player1Score} - {self.computerScore}')
		elif computerChoice==paper and playerChoice==rock:
			self.computerScore+=1
			self.scoreLbl.config(text=f'Score : {self.player1Score} - {self.computerScore}')
		elif computerChoice==paper and playerChoice==scissor:
			self.player1Score+=1
			self.scoreLbl.config(text=f'Score : {self.player1Score} - {self.computerScore}')
		elif computerChoice==scissor and playerChoice==paper:
			self.computerScore+=1
			self.scoreLbl.config(text=f'Score : {self.player1Score} - {self.computerScore}')
		elif computerChoice==scissor and playerChoice==rock:
			self.player1Score+=1
			self.scoreLbl.config(text=f'Score : {self.player1Score} - {self.computerScore}')

        


	


root=tk.Tk()
window=Window(root,'Rock Paper Scissor','290x200')