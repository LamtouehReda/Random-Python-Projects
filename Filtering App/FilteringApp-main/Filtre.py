import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog as fd
import numpy as np
from skimage.util import random_noise

root = Tk()
root.title('Reda Lamtoueh')
# root.geometry('1300x500')
# root.resizable(False,False)

def openImg():
    global test
    global imgOriginal
    filename=fd.askopenfilename()
    imgOriginal=Image.open(filename)
    while imgOriginal.size[0]>=300 or imgOriginal.size[1]>=500:
        imgOriginal=imgOriginal.resize((imgOriginal.size[0]//2,imgOriginal.size[1]//2))
    test = ImageTk.PhotoImage(imgOriginal)

affCount=0
bruit=0
filtre=0
def addImg():
    global label1
    global affCount
    label1=tkinter.Label(root,image=test)
    label1.image = test
    label1.grid(row=1,column=1)
    # label.place(x=1, y=100)
    affCount=1

def clearLabel1():
    if affCount!=0:
        label1.destroy()

def clearLabel2():
    if bruit != 0:
        label2.destroy()

def clearLabel3():
    if filtre!=0:
        label3.destroy()

def bruiteImg():
    global label2
    global bruit
    array=np.array(imgOriginal)
    noisedImg=random_noise(array,mode='s&p')
    noisedImg = np.array(255*noisedImg, dtype = 'uint8')
    noisedImg=Image.fromarray(noisedImg)
    test = ImageTk.PhotoImage(noisedImg)
    label2=tkinter.Label(root,image=test)
    label2.image = test
    label2.grid(row=1,column=2)
    bruit=1
    # label.place(x=400, y=100)

def filterMoyenneur(t):
    global label3
    global filtre
    k=3
    k=k//2
    array=np.array(imgOriginal)
    shape=np.shape(array)
    new=np.zeros(shape)
    for i in range(k,shape[0]-k):
        for j in range(k,shape[1]-k):
            voisins=array[i-k:i+k+1,j-k:j+k+1]
            if t==0:
                new[i,j]=np.mean(voisins)
            if t==1:
                new[i, j] = np.median(voisins)

    new=Image.fromarray(new.astype(np.uint8))
    test = ImageTk.PhotoImage(new)
    label3 = tkinter.Label(root, image=test)
    label3.image = test
    label3.grid(row=1,column=3)
    I1 = array
    I2 = np.array(new)
    mse = round(np.mean((I1 - I2) ** 2),2)
    psnr = round(10 * np.log10(np.max(I1 ** 2) / mse),2)
    label4=tkinter.Label(root,text='MSE='+str(mse)+'   PSNR='+str(psnr))
    label4.grid(row=4,column=2,pady=(30,30))

    filtre=1
    # label.place(x=800, y=100)
message='Step1 : Choisir\nStep2 : Afficher\nStep3 : Bruiter\nStep4 : Choisir Le filtre\nStep5 : Filtrer'
guidLabel=tkinter.Label(root,text=message)
guidLabel.config(font=('Helvetica bold', 26))
guidLabel.grid(row=1,column=2,pady=(10,10))
btnChoisir=ttk.Button(root,text='Choisir',command=lambda:[openImg()])
btnChoisir.grid(row=2,column=2)
btnAfficher=ttk.Button(root,text='Afficher',command=lambda:[clearGuid(),clearLabel1(),addImg()])
btnAfficher.grid(row=3,column=1)
btnBruite=ttk.Button(root,text='Bruite',command=lambda:[clearLabel2(),bruiteImg()])
btnBruite.grid(row=3,column=2)
btnFiltrer=ttk.Button(root,text='Filtrer',command=lambda:[clearLabel3(),filtrer()])
btnFiltrer.grid(row=3,column=3)
vlist = ["Moyenneur", "Median"]
Combo = ttk.Combobox(root, values=vlist)
Combo.set("Choisir Filtre")
Combo.grid(row=3,column=4)

def filtrer():
    if Combo.current()==0:
        filterMoyenneur(0)
    if Combo.current()==1:
        filterMoyenneur(1)

def clearGuid():
    guidLabel.destroy()

root.mainloop()
