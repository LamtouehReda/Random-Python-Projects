import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from transmissionCodes import *
from plotGraph import plot
from PIL import Image, ImageTk
from tkinter import scrolledtext

class Window:
	def __init__(self,root,title,geometry):
		self.root=root
		self.root.title(title)
		self.root.geometry(geometry)

		self.BrowseBtn=tk.Button(self.root,text='Select File',command=self.openFile)
		self.BrowseBtn.grid(row=1,column=0)

		self.frame=tk.Frame(self.root)

		self.transmissonLabel=tk.Label(self.frame,text='Type de Transmission : ')
		self.transmissonLabel.grid(row=0,column=0)
		self.codesList=['RZ','NRZ','NRZI','Manchester','Manchester_Diff','Miller','CMI','AMI','MLT3','_2B1Q']
		self.ComboBox=ttk.Combobox(self.frame,values=self.codesList)
		self.ComboBox.grid(row=0,column=1)

		self.volteLabel=tk.Label(self.frame,text='Voltes : ')
		self.volteLabel.grid(row=0,column=2)
		self.volte = tk.Entry(self.frame, width=5)
		self.volte.grid(row=0, column=3, padx=5)

		self.frame.grid(row=2,column=0,pady=10)

		self.button=tk.Button(self.root,text='Apply',command=self.code)
		self.button.grid(row=3,column=0)

		self.graphLabel=tk.Label(self.root)

		self.OutputFrame=tk.Frame(self.root)

		self.filename=''

		self.root.mainloop()

	def openFile(self):
		filename=fd.askopenfilename()
		self.filename=filename

	def ImageToBinaire(self,image):
	    I=plt.imread(image)
	    l,c=I.shape[0:2]
	    r, g, b = I[:,:,0], I[:,:,1], I[:,:,2]
	    liste=np.concatenate((r,g,b),axis=None)
	    m=['0'*(64-len(bin(l)[2:]))+bin(l)[2:],'0'*(64-len(bin(c)[2:]))+bin(c)[2:]]
	    for i in liste:
	        m.append('0'*(8-len(bin(i)[2:]))+bin(i)[2:])
	    str1=''.join([str(elem) for elem in m])
	    return str1

	def TextToBinaire(self,filename):
	    file=open(filename,'r')
	    contenu=file.read()
	    print("le contenu du fichier : "+contenu)
	    return ''.join([format(ord(x),'08b') for x in contenu])


	def BinaireToText(self,s):
	    chunks = [s[i:i+8] for i in range(0, len(s), 8)]
	    data=''
	    for i in chunks:
	        data+=chr(int(i,2))
	    return data

	def BinaireToImage(self,chaine):
		pass
	    # l=''
	    # c=''
	    # for i in range(64):
	    #     l+=chaine[i]
	    # for i in range(64,128):
	    #     c+=chaine[i]
	    # pix=[]
	    # for i in range(128,len(chaine),8):
	    #     pix.append(int(chaine[i:i+8],2))
	    # l=int(l,2)
	    # c=int(c,2)
	    # P1=[]
	    # for j in range(0,l*c):
	    #     P1.append(pix[j])
	    # P1=np.array(P1)
	    # P1=P1.reshape(l,c)
	    # P2=[]
	    # for j in range(l*c,len(pix)-(l*c)):
	    #     P2.append(pix[j])
	    # P2=np.array(P2)
	    # P2=P2.reshape(l,c)
	    # P3=[]
	    # for j in range(len(pix)-(l*c),len(pix)):
	    #     P3.append(pix[j])
	    # P3=np.array(P3)
	    # P3=P3.reshape(l,c)
	    # image_or = cv2.merge(np.array([P1,P2,P3]))
	    # plt.imshow(image_or)
	    # return image_or


	def fileData(self,filename):
		fileType=filename.split('.')[-1]
		if fileType=='txt':
			data=self.TextToBinaire(filename)
		else:
			data=self.ImageToBinaire(filename)
		return data

	def decodeData(self,data):
		fileType=self.filename.split('.')[-1]
		if fileType=='txt':
			original=self.BinaireToText(data)
		else:
			original=self.BinaireToImage(data)
		return original

	def displayFile(self,data):
		root.geometry('700x400')
		fileType=self.filename.split('.')[-1]
		if fileType=='txt':
			TextLabel = scrolledtext.ScrolledText(self.OutputFrame,
                                          wrap=tk.WORD,
                                          width=50,
                                          font=("Times New Roman",
                                                9))
			TextLabel.insert(tk.INSERT,data)
			TextLabel.grid(row=0, column=1,pady=10)
		else:
			image1 = Image.open(self.filename)
			image1 = image1.resize((350, 250), Image.ANTIALIAS)
			test = ImageTk.PhotoImage(image1)

			label1 = tk.Label(self.OutputFrame,image=test)
			label1.image = test
			label1.grid(row=0,column=1)
		self.OutputFrame.grid(row=4,column=0)


	def code(self):
		data=self.fileData(self.filename)
		data=list(data)
		codeType=self.ComboBox.get()
		volte=int(self.volte.get())
		if codeType=='RZ':
			voltes=RZ(data,volte)
			decoded=RZdecode(voltes)
		elif codeType=='NRZ':
			voltes=NRZ(data,volte)
			decoded=NRZdecode(voltes)
		elif codeType=='NRZI':
			voltes=NRZI(data,volte)
			decoded=NRZIdecode(voltes)
		elif codeType=='Manchester':
			voltes=Manchester(data,volte)
			decoded=ManchesterDecode(voltes)
		elif codeType=='Manchester_Diff':
			voltes=Manchester_diff(data,volte)
			decoded=Manchester_diff_decode(voltes)
		elif codeType=='Miller':
			voltes=Miller(data,volte)
			decoded=MilerDecode(voltes)
		elif codeType=='CMI':
			voltes=CMI(data,volte)
			decoded=CMIdecode(voltes)
		elif codeType=='AMI':
			voltes=AMI(data,volte)
			decoded=AMIdecode(voltes)
		elif codeType=='MLT3':
			voltes=MLT3(data,volte)
			decoded=MLT3decode(voltes)
		elif codeType=='_2B1Q':
			voltes=_2B1Q(data,volte)
			decoded=_2B1Qdecode(voltes)

		voltes=voltes[:50]
		self.root.geometry('700x400')
		plot(self.OutputFrame,voltes)


		original=self.decodeData(decoded)
		self.displayFile(original)




		



root=tk.Tk()
Window(root,'Tp','400x200')

