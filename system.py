import tkinter as tk
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import csv
import pylab
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import subproblem.is_graphical as is_g
import subproblem.is_digraphical as is_d
import subproblem.is_pseudographical as is_p
import subproblem.is_multigraphical as is_m
import subproblem.is_havel_hakimi as is_hh
import subproblem.is_erdos_galli as is_eg


#when clicking graphical degree problem:
def hit_graphical_degree():
    #create a menu for traversal problems
    window1 = tk.Toplevel(window)
    window1.geometry('400x400')
    window1.title('graphical degree')
    tk.Label(window1, text='choose the sort of graphical degree problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
    
    is_g_button = tk.Button(window1, text = 'Is_graphical_search', \
                            command = lambda: is_g.hit_is_graphical_search(window), \
                            width = 25, anchor = 'w')
    is_d_button = tk.Button(window1, text = 'Is_digraphical_search', \
                            command = lambda: is_d.hit_is_digraphical_search(window), \
                            width = 25, anchor = 'w')
    is_m_button = tk.Button(window1, text = 'Is_multigraphical_search', \
                                    command = lambda: is_m.hit_is_multigraphical_search(window), \
                                    width = 25, anchor = 'w')
    is_p_button = tk.Button(window1, text = 'Is_pseudographical_search', \
                                command = lambda: is_p.hit_is_pseudographical_search(window), \
                                width = 25, anchor = 'w')
    is_hh_button = tk.Button(window1, text = 'Is_havel_hakimi_search', \
                                command = lambda: is_hh.hit_is_havel_hakimi_search(window), \
                                width = 25, anchor = 'w')
    is_eg_button = tk.Button(window1, text = 'Is_erdos_galli_search', \
                                command = lambda: is_eg.hit_is_erdos_galli_search(window), \
                                width = 25, anchor = 'w')
                                
    is_g_button.place(x = 10, y = 50)
    is_d_button.place(x = 10, y = 80)
    is_m_button.place(x = 10, y = 110)
    is_p_button.place(x = 10, y = 140)
    is_hh_button.place(x = 10, y = 170)
    is_eg_button.place(x = 10, y = 200)

#build a window using tkInter
window = tk.Tk()
window.title('Menu of Graph problems')
window.geometry('500x800')

graphical_degree = tk.Button(window, text = '28. Graphical_degree problem', 
                                command = hit_graphical_degree, width = 25, anchor = 'w')
graphical_degree.place(x = 50, y = 50)




#
# --------------------------------------- Traversal --------------------------------------------------------------------
#
'''
#when clickc(hit) on traversal_dfs_edges  to calculate input graph's using dfs
def hit_traversal_dfs_edges():
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
                source.append(int(row[0]))
                target.append(int(row[1]))
                value.append(int(row[2]))

        #create one empty graph
        G = nx.DiGraph()

        #add nodes to the graph
        for i in range(0, np.size(target) + 1):
            G.add_node(i)

        #add weighted edges to the graph
        for i in range(np.size(source)):
            G.add_weighted_edges_from([(source[i], target[i], value[i])])

        #assign layout with spacing
        pos = nx.spring_layout(G)
        #graph is loaded completely

        messagebox.showinfo(title='Result', message=('the edges of G in dfs are:', list(nx.dfs_edges(G, source=0, depth_limit=int(n))))) #this is the function that you need to solve the problem: nx.dfs_edges()

        #draw the graph
        nx.draw(G, pos, with_labels=True, node_color='b', edge_color='k', node_size=200, alpha=0.5)
        pylab.title('Self_Define Net', fontsize=15)
        pylab.show()

    #create window for dfs_edges
    window3 = tk.Toplevel(window)
    window3.geometry('400x300')
    window3.title('Iterate over edges in a depth-ﬁrst-search')
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

    #this dfs problem can be implemented with constraint of depth:
    depth = tk.StringVar()
    depth.set('number')
    tk.Label(window3, text='input the depth limit you want to see: ', bg = 'green').place(x=10, y=60)
    entry_depth = tk.Entry(window3, textvariable=depth,width = 35)
    entry_depth.place(x=10, y=85)

    #confirm, and generate the output
    confirm = tk.Button(window3, text = 'confirm', command = show_result, bg = 'yellow').place(x = 150, y = 130)

def hit_traversal_dfs():
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen Depth_first_search problem, continue?')
    if(a == True):
        #create a new window for traversal_dfs problem
        #create a menu of dfs subproblems
        window2 = tk.Toplevel(window)
        window2.geometry('500x300')
        window2.title('Depth_first_search problems')
        tk.Label(window2, text='choose the sort of Depth_first_search problem you want to deal with: ', bg='yellow').place(x = 10, y = 10)
        dfs_edges = tk.Button(window2, text='Iterate over edges in a depth-ﬁrst-search', command = hit_traversal_dfs_edges, width = 40, anchor = 'w')
        dfs_edges.place(x = 10, y = 50)
        dfs_tree = tk.Button(window2, text='Return oriented tree constructed from a depth-ﬁrst-search from source', width = 40, anchor = 'w')
        dfs_tree .place(x=10, y=80)
        dfs_predecessors = tk.Button(window2, text='Return dictionary of predecessors in depth-ﬁrst-search from source', width = 40, anchor = 'w')
        dfs_predecessors.place(x=10, y=110)
        dfs_successors = tk.Button(window2, text='Return dictionary of successors in depth-ﬁrst-search from source', width = 40, anchor = 'w')
        dfs_successors.place(x=10, y=140)
        dfs_preorder_nodes = tk.Button(window2, text='Generate nodes in a depth-ﬁrst-search pre-ordering starting at source', width = 40, anchor = 'w')
        dfs_preorder_nodes.place(x=10, y=170)
        dfs_postorder_nodes = tk.Button(window2, text='Generate nodes in a depth-ﬁrst-search post-ordering starting at source', width = 40, anchor = 'w')
        dfs_postorder_nodes.place(x=10, y=200)
        dfs_labeled_edges = tk.Button(window2, text='Iterate over edges in a depth-ﬁrst-search labeled by type',width=40, anchor='w')
        dfs_labeled_edges.place(x=10, y=230)


#when choosing traversal problem:
def hit_traversal():
    #prompt for confirmation
    a = messagebox.askyesno(title = 'are you sure', message = 'you have chosen traversal problem, continue?')
    if(a == True):
        #create a menu for traversal problems
        window1 = tk.Toplevel(window)
        window1.geometry('400x200')
        window1.title('traversal problems')
        tk.Label(window1, text='choose the sort of traversal problem you want to deal with: ', bg = 'yellow').place(x=10, y=10)
        dfs = tk.Button(window1, text = 'Depth_first_search', command = hit_traversal_dfs, width = 25, anchor = 'w')
        dfs.place(x = 10, y = 50)
        bfs = tk.Button(window1, text = 'Breadth_first_search', width = 25, anchor = 'w')
        bfs.place(x = 10, y = 80)
        bs = tk.Button(window1, text = 'Beam_search', width = 25, anchor = 'w')
        bs.place(x = 10, y = 110)


traversal = tk.Button(window, text = '46.Traversal problem', command = hit_traversal, width = 25, anchor = 'w')
traversal.place(x= 50, y = 100)
'''
window.mainloop()
