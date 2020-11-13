import json
import networkx as nx
import pickle
from tqdm import tqdm

with open('dblp_coauthorship.json') as f:
  data = json.load(f)
print(len(data))

G2005 = nx.Graph()
G2006 = nx.Graph()
G2005weighted = nx.Graph()

for d in tqdm(data):
    if d[2] == 2005:
        G2005.add_edge(d[0], d[1])
    if d[2] == 2006:
        G2006.add_edge(d[0], d[1])
    if d[2] == 2005:
        if G2005weighted.has_edge(d[0], d[1]):
            old_weight = G2005weighted.edges[d[0], d[1]]['weight']
            G2005weighted.add_edge(d[0], d[1], weight=old_weight+1)
        else:
            G2005weighted.add_edge(d[0], d[1], weight=1)

with open('G2005.pkl', 'wb') as f:
    pickle.dump(G2005, f)

with open('G2006.pkl', 'wb') as f:
    pickle.dump(G2006, f)

with open('G2005weighted.pkl', 'wb') as f:
    pickle.dump(G2005weighted, f)
