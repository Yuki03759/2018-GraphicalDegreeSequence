import networkx as nx
import util
def hit_is_pseudographical_search(window):
#
#
#       Write is_pseudographical here
    G = nx.DiGraph()
#
#
    title = 'search if the input is a pseudographical degree sequence'
    label_problem = None
    
    util.confirm(window, title, label_problem)