import pickle
import networkx as nx

def find_gcc(G):
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    return G.subgraph(Gcc[0])

with open('G2005.pkl', 'rb') as f:
    G2005 = pickle.load(f)

# with open('G2006.pkl', 'rb') as f:
#     G2006 = pickle.load(f)
#
# with open('G2005weighted.pkl', 'rb') as f:
#     G2005weighted = pickle.load(f)

selected = find_gcc(G2005)
# scores = nx.pagerank(selected)
# sorted_scores = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
# counter = 0
# print(sorted_scores)
# with open('pagerank.txt', 'wt') as file:
#     for s in sorted_scores:
#         if counter == 50:
#             break
#         file.write(s[0] + ', ' + str(s[1])+ '\n')

edge_betweenness = nx.edge_betweenness_centrality(selected, k=10)
print(edge_betweenness)