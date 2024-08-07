def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(V, edges):
    parent = []
    rank = []

    edges.sort(key=lambda x: x[2])  

    for node in range(V):
        parent.append(node)
        rank.append(0)

    mst_cost = 0
    mst_edges = []

    for u, v, wt in edges:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            mst_cost += wt
            mst_edges.append([u, v, wt])
            union(parent, rank, x, y)

    return mst_cost, mst_edges

V = int(input("Enter the number of vertices:"))
edges=[]
E = int(input("enter the number of edges:"))
for i in range(E):
    print("Enter the edge(u,v):")
    u = int(input())
    v=int(input())
    weight = int(input("enter the edge weight:"))
    edges.append([u,v,weight])

mst_cost, mst_edges = kruskal(V, edges)
print("Minimum Cost of Spanning Tree:", mst_cost)
print("Edges in Minimum Spanning Tree:")
for edge in mst_edges:
    print(edge)