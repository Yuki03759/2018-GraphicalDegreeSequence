import networkx as nx
import util
def hit_is_multigraphical_search(window):
#
#
#       Write is_multigraphical here
    G = nx.DiGraph()
#
#
    title = 'search if the input is a multigraphical degree sequence'
    label_problem = None
    
    util.confirm(window, title, label_problem)