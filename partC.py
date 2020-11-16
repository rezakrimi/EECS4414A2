import pickle
import networkx as nx
from tqdm import tqdm

def find_fof(G, node):
    result = []
    visited = [node]
    neighbors = []
    for n in nx.neighbors(G, node):
        neighbors.append(n)
        visited.append(n)
    for neighbor in neighbors:
        for n in nx.neighbors(G, neighbor):
            if n not in visited:
                result.append(n)
    return result

with open('dblp2005-core.pkl', 'rb') as f:
    core2005 = pickle.load(f)

with open('dblp2006-core.pkl', 'rb') as f:
    core2006 = pickle.load(f)

# code to find fof
'''
fof = set([])
for n in tqdm(core2005.nodes):
    current_fof = find_fof(core2005, n)
    for cf in current_fof:
        if (n, cf) not in fof and (cf, n) not in fof:
            fof.add((n, cf))

with open('fof.pkl', 'wb') as f:
    pickle.dump(fof, f)
'''

#code to find set T
T = []
for edge in tqdm(core2006.edges()):
    if not core2005.has_edge(edge[0], edge[1]):
        T.append(edge)

#code to load fof
with open('fof.pkl', 'rb') as f:
    fof = pickle.load(f)

preds = nx.jaccard_coefficient(core2005, fof)
preds = sorted(preds, key= lambda x:x[2], reverse=True)
with open('jaccard_coefficient.pkl', 'wb') as f:
    pickle.dump(preds, f)
