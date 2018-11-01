import networkx as nx
import util
def hit_is_havel_hakimi_search(window):
#
#
#       Write is_havel_hakimi here
    G = nx.DiGraph()
#
#
    title = 'search if the input is havel_hakimi degree sequence'
    label_problem = None
    
    util.confirm(window, title, label_problem)