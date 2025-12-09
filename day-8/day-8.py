nodes = []


with open("day-8.txt", "r") as file:
    nodes = [[int(item) for item in node.strip().split(",")] for node in file]




def squared_distance(node1, node2): # we only need the square distance, to save processing time
    distance = (node1[0] - node2[0])**2 + (node1[1] - node2[1])**2 + (node1[2] - node2[2])**2
    return distance


# Part 1

edges = [] # size: 1000*999/2 = 499500 unique edges

for i, node1 in enumerate(nodes[:-1]):
    for j, node2 in enumerate(nodes[i+1:], start=i+1):
        edges.append((i,j,squared_distance(node1, node2)))

edges.sort(key = lambda x:x[2])
accepted_edges = []
connected_nodes = set()

for i in range(1000):
    
    accepted_edges.append((edges[i][0], edges[i][1]))
    connected_nodes.add(edges[i][0])
    connected_nodes.add(edges[i][1])

networks = []

for edge in accepted_edges:
    for network in networks:
        if edge[0] in network or edge[1] in network:
            network.add(edge[0])
            network.add(edge[1])
            break
    else:
        networks.append(set(edge))

num_combined = 1
while num_combined > 0:
    num_combined = 0
    for i, network1 in enumerate(networks[:-1]):
        for j, network2 in enumerate(networks[i+1:], start=i+1):
            if networks[i] == None or networks[j] == None:
                continue
            if len(network1.intersection(network2)) > 0:

                num_combined+=1
                networks[i] = networks[i].union(networks[j])
                networks[j] = None

networks = [n for n in networks if n]


networks.sort(key=lambda x:len(x), reverse=True)
print("Number of networks:", len(networks))
print("Top sizes:", len(networks[0]), len(networks[1]), len(networks[2]))
print("Part 1:", len(networks[0]) * len(networks[1]) * len(networks[2]))



# Part 2

accepted_edges = []
connected_nodes = set()

for i in range(len(edges)):
    accepted_edges.append((edges[i][0], edges[i][1]))
    connected_nodes.add(edges[i][0])
    connected_nodes.add(edges[i][1])

    if len(connected_nodes) == 1000:
        print("Part 2:", nodes[edges[i][0]][0] * nodes[edges[i][1]][0])
        break
