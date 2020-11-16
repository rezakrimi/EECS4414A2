import pickle
import networkx as nx
from tqdm import tqdm

def neighborhood(G, node, n):
    path_lengths = nx.single_source_dijkstra_path_length(G, node)
    return [node for node, length in path_lengths.items()
                    if length == n]

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
    core2006= pickle.load(f)

fof = []
for n in tqdm(core2005.nodes):
    current_fof = find_fof(core2005, n)
    for cf in current_fof:
        if (n, cf) not in fof or (cf, n) not in fof:
            fof.append((n, cf))

with open('fof.pkl', 'wb') as f:
    pickle.dump(fof, f)