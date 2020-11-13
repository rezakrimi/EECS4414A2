import json
import networkx as nx
import pickle
from tqdm import tqdm

with open('dblp_coauthorship.json') as f:
  data = json.load(f)
print(len(data))

G2005 = nx.Graph()
G2006 = nx.Graph()

for d in tqdm(data):
    if d[2] == 2005:
        G2005.add_edge(d[0], d[1])
    elif d[2] == 2006:
        G2006.add_edge(d[0], d[1])

with open('G2005.pkl', 'wb') as f:
    pickle.dump(G2005, f)

with open('G2006.pkl', 'wb') as f:
    pickle.dump(G2006, f)
