from edge_list_objects import Node
class DFS:
    def __init__(self,start):
        self.start = start

    def traversal(self):
        interface = self.stack()
        interface(self.start)
        return self.result

    def stack(self):
        self.result = []
        def interface(node):
            print(self.result)
            self.result.append(node)
            node.visited = True
            for n in node.neighbors:
                if n.visited == False:
                    interface(n)    #遞迴

        return interface

print('測試開始')
na = Node('A')
nb = Node('B')
nc = Node('C')
nd = Node('D')
ne = Node('E')
nf = Node('F')

na.neighbors = [nb,nc]
nb.neighbors = [nd,ne]
nc.neighbors = [nf]

bfs = DFS(na)
for node in bfs.traversal():
    print(node)