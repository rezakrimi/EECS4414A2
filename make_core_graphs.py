import pickle
import networkx as nx

def find_gcc(G):
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    return G.subgraph(Gcc[0])

with open('G2005.pkl', 'rb') as f:
    G2005 = pickle.load(f)

with open('G2006.pkl', 'rb') as f:
    G2006 = pickle.load(f)

# Finding the giant connected component of each graph
G2005 = find_gcc(G2005)
G2006 = find_gcc(G2006)

core_nodes2005 = []
core_nodes2006 = []

for n in G2005.nodes:
    if G2005.degree[n] >= 3:
        core_nodes2005.append(n)

for n in G2006.nodes:
    if G2006.degree[n] >= 3:
        core_nodes2006.append(n)

core2005 = G2005.subgraph(core_nodes2005)
core2006 = G2006.subgraph(core_nodes2006)

with open('dblp2005-core.pkl', 'wb') as f:
    pickle.dump(core2005, f)

with open('dblp2006-core.pkl', 'wb') as f:
    pickle.dump(core2006, f)