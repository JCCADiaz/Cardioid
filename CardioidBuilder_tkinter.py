from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

import math
from matplotlib.collections  import LineCollection

from matplotlib import cm
import matplotlib.collections as mc
import matplotlib.transforms as tx

from tkinter import filedialog
from tkinter.filedialog import askopenfilename

root = Tk()
root.title("Cardioid Builder")
# to use an icon uncomment the following line and include a path
# root.iconbitmap('path/icone.ico')
root.geometry("435x350")

###############################
def lineas_cardioide(r,N,factor):
    x = np.zeros(N);  y = np.zeros(N)
    b = np.zeros(N)
    i=0
    while i <= N-1:
        ang = ((2*math.pi/N)*(1*i))-math.pi/2
        x[i] =r* math.cos(ang)
        y[i] =r* math.sin(ang)

        b[i]=i*factor
    
        if b[i]>=N:
            b[i]=b[i]-((b[i]//N)*N)
    
        i=i+1
    return x,y,b
###############################

###############################
def plot_lines_Circle(r,x,y,b,N):
    global factor
    global fig
    fig, ax = plt.subplots()
    fig.canvas.set_window_title('Factor_'+factor_box.get()+"_Lines_"+lines_box.get())

    A=0
    for i in range(N):
                
        A=[(x[i],y[i]),(x[int(b[i])],y[int(b[i])])]
    
        lines = mc.LineCollection([A],colors='black', lw=1)
        ax.add_collection(lines)  

    circle = plt.Circle((0, 0), r, color='red', fill=False,linestyle='-', lw=3,zorder=N+1)
    ax.add_artist(circle)
    
    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
    ax.set_aspect('equal')
    ax.axis([-1*(r+0.1),1*(r+0.1), -1*(r+0.1), 1*(r+0.1)])
    ax.axis('off')
    plt.tight_layout()
    plt.show()
    
###############################

###############################
def graph():
    global factor
    r=10
    factor= float(factor_box.get())
    N=int(lines_box.get())
    x,y,b = lineas_cardioide(r,N,factor)
    plot_lines_Circle(r,x,y,b,N)

###############################

###############################
def save():
    export_folder = filedialog.askdirectory()
    figname= 'Factor_'+factor_box.get()+"_Lines_"+lines_box.get()
    fig.savefig(export_folder+"/"+figname+clicked_type.get(), dpi=int(clicked_dpi.get()),bbox_inches='tight')

###############################

###############################
# Between frame frame_Graph
frame_Graph = LabelFrame(root, text="Show Cardioid", padx=5, pady=5)#padx and pady inside of the frame
# in frame text="..." is optional

frame_Graph.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")#padx and pady outside of the frame

#boxes
factor_box = Entry(frame_Graph, width=30)
factor_box.insert(0, "36")
factor_box.grid(row=0, column=1, padx=10, pady=10)

lines_box = Entry(frame_Graph, width=30)
lines_box.insert(0, "350")
lines_box.grid(row=1, column=1, padx=10, pady=10)

#Labels
factor_box_label = Label(frame_Graph, text="Desired factor ")
factor_box_label.grid(row=0, column=0, padx=10, pady=(10, 0))

lines_box_label = Label(frame_Graph, text="Number of lines ")
lines_box_label.grid(row=1, column=0, padx=10, pady=(10, 0))

#Buttons
my_button = Button(frame_Graph, text="Graph It!",
                   font=("", 10), background="SkyBlue1", width=30, command=graph)
my_button.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 5))
###############################

###############################
# Between frame frame_save

frame_save = LabelFrame(root, text="Save options", padx=45, pady=5)#padx and pady inside of the frame
# in frame text="..." is optional

frame_save.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")#padx and pady outside of the frame
    
options = [200, 250, 300, 350, 400, 500, 600]
optionsformat = [".png", ".jpg",".eps"]

clicked_dpi = StringVar()
clicked_dpi.set(options[2])

clicked_type = StringVar()
clicked_type.set(optionsformat[0])


drop_dpi = OptionMenu(frame_save, clicked_dpi, *options)
drop_dpi.grid(row=0, column=1)

drop_type = OptionMenu(frame_save, clicked_type, *optionsformat)
drop_type.grid(row=0, column=3)


drop_dpi_label= Label(frame_save, text="dpi")
drop_dpi_label.grid(row=0, column=0)

drop_type_label= Label(frame_save, text="Type")
drop_type_label.grid(row=0, column=2)

save_button = Button(frame_save, text="Click to Save",
                      font=("", 10), background="SkyBlue1", width=30, command=save)
save_button.grid(row=1, column=0, columnspan=4, padx=20, pady=(10, 5))

###############################

root.mainloop()
