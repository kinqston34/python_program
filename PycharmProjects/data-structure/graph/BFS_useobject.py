from edge_list_objects import Node
class BFS:
    def __init__(self,start):
        self.queue = []
        self.start = start

    def traversal(self):
        self.start.visited = True
        self.queue.append(self.start)

        while self.queue:  #O(V)
            node = self.queue.pop(0)  #刪除已經拜訪的節點
            yield node   #執行一次後會停止return並且下一次會繼續從這邊執行

            for n in node.neighbors:  #O(E)
                if n.visited == False:
                    n.visited = True
                    self.queue.append(n)
            print(self.queue)

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

bfs = BFS(na)
for node in bfs.traversal():
    print(node)

