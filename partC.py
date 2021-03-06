import pickle
import networkx as nx
from tqdm import tqdm

def common_neighbor_centrality(G, pairs, alpha=0.8):
    result = []
    print('calculating common neighbors centrality')
    for p in tqdm(pairs):
        common_neighbors = list(nx.common_neighbors(G, p[0], p[1]))
        score = (alpha * len(common_neighbors)) + ((1-alpha) * G.number_of_nodes() / 2)
        result.append((p[0], p[1], score))
    return result

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

with open('T.pkl', 'wb') as f:
    pickle.dump(T, f)

#code to load fof
with open('fof.pkl', 'rb') as f:
    fof = pickle.load(f)

# preds = nx.jaccard_coefficient(core2005, fof)
# preds = sorted(preds, key= lambda x:x[2], reverse=True)
# with open('jaccard_coefficient.pkl', 'wb') as f:
#     pickle.dump(preds, f)


# Common_Neighbor_centrality
preds = common_neighbor_centrality(core2005, fof, alpha=0.8)
preds = sorted(preds, key= lambda x:x[2], reverse=True)
with open('common_neighbor_centrality.pkl', 'wb') as f:
   pickle.dump(preds, f)

#Preferential_attachment
# preds = nx.preferential_attachment(core2005, fof)
# preds = sorted(preds, key= lambda x:x[2], reverse=True)
# with open('preferential_attachment.pkl', 'wb') as f:
#     pickle.dump(preds, f)
#
# #Adamic_Adar_index
# preds = nx.adamic_adar_index(core2005, fof)
# preds = sorted(preds, key= lambda x:x[2], reverse=True)
# with open('adamic_adar_idex.pkl', 'wb') as f:
#     pickle.dump(preds, f)
