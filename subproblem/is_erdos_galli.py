import networkx as nx
import util
def hit_is_erdos_galli_search(window):
#
#
#       Write is_erdos_galli here
    G = nx.DiGraph()
#
#
    title = 'search if the input is_erdos_galli degree sequence'
    label_problem = None
    
    util.confirm(window, title, label_problem)