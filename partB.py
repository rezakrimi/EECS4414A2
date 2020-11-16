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

pagerank_list = ["G2005_pagerank.txt", "G2006_pagerank.txt", "G2005weighted_pagerank.txt"]
edge_betweenness_list = ["G2005_edge_betweenness.txt", "G2006_edge_betweenness.txt", "G2005weighted_edge_betweenness.txt"]

selected = [find_gcc(G2005), find_gcc(G2006), find_gcc(G2005weighted)]

for i in range(0, 3): 
    scores = nx.pagerank(selected[i])
    sorted_scores = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
    counter = 0
    #print(sorted_scores)
    with open(pagerank_list[i] , 'wt') as file:
        for s in sorted_scores:
            if counter == 50:
                break
            file.write(s[0] + ', ' + str(s[1])+ '\n')
            counter += 1

    edge_betweenness = nx.edge_betweenness_centrality(selected[i], k=10)
    sorted_edge_betweenness = sorted(edge_betweenness.items(), key=lambda kv: kv[1], reverse=True)
    counter = 0
    with open(edge_betweenness_list[i], 'wt') as file:
        for s in sorted_edge_betweenness:
            if counter == 50:
                break
            file.write(s[0][0] + ', ' + s[0][1] + ', ' + str(s[1])+ '\n')
            counter += 1