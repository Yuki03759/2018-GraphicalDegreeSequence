import tkinter as tk
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

def read_csv(s, t, v, m):
    with open(m) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        s = []
        t = []
        v = []
        for row in reader:
            s.append(int(row[0]))
            t.append(int(row[1]))
            v.append(int(row[2]))
    
    
def create_graph(G, s, t, v):
    for i in range(np.size(s)):
        G.add_weighted_edges_from([(s[i], t[i], v[i])])
    
    
def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
    pylab.title('Self_Define Net', fontsize=15)
    pylab.show()
    
    