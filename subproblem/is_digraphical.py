import networkx as nx
import util
def hit_is_digraphical_search(window):
#
#
#       Write is_digraphical here
    G = nx.DiGraph()
#
#
    title = 'search if the input is a directed graph degree sequence'
    label_problem = None
    
    util.confirm(window, title, label_problem)