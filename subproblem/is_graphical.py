import tkinter as tk
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab
from tkinter import messagebox
import util

def hit_is_graphical_search(window):
    
#
#
#       Write is_graphical here
    G = nx.DiGraph()
#
#
    title = 'search if the input is a valid degree sequence'
    label_problem = 'choose the way whether havel hakimi or erodos gallai : '
    
    util.confirm(window, title, label_problem)