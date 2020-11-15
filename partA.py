import pickle
import networkx as nx

def find_gcc(G):
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    return G.subgraph(Gcc[0])

with open('G2005.pkl', 'rb') as f:
    G2005 = pickle.load(f)

with open('G2006.pkl', 'rb') as f:
    G2006 = pickle.load(f)

with open('G2005weighted.pkl', 'rb') as f:
    G2005weighted = pickle.load(f)

# Finding the giant connected component of each graph
G2005weighted = find_gcc(G2005weighted)
G2005 = find_gcc(G2005)
G2006 = find_gcc(G2006)

print(G2005weighted.number_of_nodes(), G2005weighted.number_of_edges())
print(G2005.number_of_nodes(), G2005.number_of_edges())
print(G2006.number_of_nodes(), G2006.number_of_edges())