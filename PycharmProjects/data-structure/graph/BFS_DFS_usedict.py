graph = {          #利用字典造圖
    "A": ['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    "D":['B','C','E','F'],
    'E':['C','D'],
    'F':['D']
}

def BFS(graph,s):    #DFS
    queue = []         #將queue改成stack
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s:None}
    while len(queue) >0:
        vertex = queue.pop(0)   #vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex #記錄前一個點
        #print(vertex)
    return parent

parent = BFS(graph,'B')
for key in parent:
    print(key,parent[key])

target='B'   #搜尋最短路徑
while target !=None:
    print(target)
    target = parent[target]




BFS(graph,'A')
BFS(graph,'B')