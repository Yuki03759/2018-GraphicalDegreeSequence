import tkinter as tk
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

def show_result():
    m = path.get()
    n = depth.get()

    #input user graph
    with open(m) as csvfile: #read the csv file, row by row
        reader = csv.reader(csvfile)
        next(reader)
        source = []
        target = []
        value = []
        for row in reader:
            source.append(int(row[0])) # node
            target.append(int(row[1])) # an
            value.append(int(row[2]))
            
def select_path(path):
    path_ = askopenfilename() #path function
    path.set(path_)
    
def confirm(window, title, label_problem):
        
    #create window for dfs_edges
    window3 = tk.Toplevel(window)
    window3.geometry('400x300')
    window3.title(title)
    tk.Label(window3, text='input the necessary components: ', bg='yellow').place(x=10, y=10)


    #use path function to get path
    #pass the value of path

    path = tk.StringVar()
    path.set('path')
    tk.Label(window3, text='input the path to import your own graph : ', bg = 'green').place(x=10, y=10)
    entry_path = tk.Entry(window3, textvariable = path, width = 35)
    entry_path.place(x=10, y=35)
    tk.Button(window3, text = 'choose path', command = lambda: select_path(path)).place(x = 250, y = 35)

    #this dfs problem can be implemented with constraint of depth:
    if label_problem is not None:
        depth = tk.StringVar()
        depth.set('number')
        tk.Label(window3, text=label_problem, bg = 'green').place(x=10, y=60)
        entry_depth = tk.Entry(window3, textvariable=depth,width = 35)
        entry_depth.place(x=10, y=85)

    #confirm, and generate the output
    confirm = tk.Button(window3, text = 'confirm', command = show_result, bg = 'yellow').place(x = 150, y = 130)

    