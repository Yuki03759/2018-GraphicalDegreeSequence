import tkinter as tk
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import util

        
def hit_search(window, selection):
    G = nx.DiGraph()
    
    def show_result():
        m = path.get()

        #input user graph
        with open(m) as csvfile: #read the csv file, row by row
            reader = csv.reader(csvfile)
            next(reader)
            source = []
            target = []
            value = []
            for row in reader:
                source.append(int(row[0]))
                target.append(int(row[1]))
                value.append(int(row[2]))
        
        util.create_graph(G, source, target, value)
        degrees = G.degree( G.nodes(), None)
        list_degrees = list(degrees)
        in_degree = G.in_degree(degrees)
        out_degree = G.out_degree(degrees)
        messagebox.showinfo(title='Result', message=('the degrees of the nodes are:', degrees))
        if selection == "is_g":
            messagebox.showinfo(title='Result', message=('the result of is_graphical:', nx.is_graphical(degrees)))
        elif selection =="is_d":
            messagebox.showinfo(title='Result', message=('the result of is_digraphical:', nx.is_digraphical(in_degree, out_degree)))
        elif selection =="is_m":
            messagebox.showinfo(title='Result', message=('the result of is_multigraphical:', nx.is_multigraphical(degrees)))
        elif selection =="is_p":
            messagebox.showinfo(title='Result', message=('the result of is_psuedographical:', nx.is_pseudographical(degrees)))
        elif selection =="is_hh":
            messagebox.showinfo(title='Result', message=('the result of is_havel_hakimi:', nx.is_valid_degree_sequence_havel_hakimi(list_degrees)))
        elif selection =="is_eg":
            messagebox.showinfo(title='Result', message=('the result of is_erdos=galli:', nx.is_valid_degree_sequence_erdos_gallai(list_degrees)))
        
        util.draw_graph(G)

    #create window for dfs_edges
    window3 = tk.Toplevel(window)
    window3.geometry('400x300')
    window3.title('Is Graphical?')
    tk.Label(window3, text='input the necessary components: ', bg='yellow').place(x=10, y=10)

    def select_path():
        path_ = askopenfilename() #path function
        path.set(path_)

    #use path function to get path
    #pass the value of path
    path = tk.StringVar()
    path.set('path')
    tk.Label(window3, text='input the path to import your own graph : ', bg = 'green').place(x=10, y=10)
    entry_path = tk.Entry(window3, textvariable = path, width = 35)
    entry_path.place(x=10, y=35)
    tk.Button(window3, text = 'choose path', command = select_path).place(x = 250, y = 35)

    #confirm, and generate the output
    confirm = tk.Button(window3, text = 'confirm', command = show_result, bg = 'yellow').place(x = 150, y = 130)
