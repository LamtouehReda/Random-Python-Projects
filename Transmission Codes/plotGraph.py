from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

def plot(root,ls):

    fig = Figure(figsize=(3, 2), dpi=100)
    plot = fig.add_subplot(111)
    title = plot.set_title("Plot")

    plot.step([x for x in range(len(ls))],ls,color='red',where='post')
    plot.axhline(linewidth=1,color='black')
    plot.set_yticks(np.arange(-20,20,5))
    plot.set_xticks([])
    plot.set_ylabel("Tension")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0,padx=20)