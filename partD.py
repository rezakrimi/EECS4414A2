import pickle
import networkx as nx

with open('G2005.pkl', 'rb') as f:
    G2005_copy = pickle.load(f)

def find_gcc(G):
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    return G.subgraph(Gcc[0])

G2005_copy = find_gcc(G2005_copy)

G2005 = nx.Graph()

for n in G2005_copy.edges():
    G2005.add_edge(n[0], n[1])

while True:
    print('iter')
    if len(list(nx.connected_components(G2005))) >= 10:
        break
    edge_betweenness = nx.edge_betweenness_centrality(G2005, k=10)
    sorted_edge_betweenness = sorted(edge_betweenness.items(), key=lambda kv: kv[1], reverse=True)
    G2005.remove_edge(*sorted_edge_betweenness[0][0])

community_sizes = sorted(nx.connected_components(G2005), key=len, reverse=True)
for i, cs in enumerate(community_sizes):
    print('community number ' + str(i) + ' ' + str(cs))