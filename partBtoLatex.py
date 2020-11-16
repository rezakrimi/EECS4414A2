path = 'G2005_edge_betweenness.txt'
file = open(path, 'r')
Lines = file.readlines()

# pagerank table
# for i, line in enumerate(Lines):
#     temp = line.strip()
#     temp = temp.split(',')
#     print(str(i+1) + ' & ' + ' & '.join(temp) + ' \\\\')

# edge betweenness table
for i, line in enumerate(Lines):
    if i == 20:
        break
    temp = line.strip()
    temp = temp.split(',')
    temp = temp[:2]
    print(str(i + 1) + ' & ' + ' & '.join(temp) + ' \\\\')