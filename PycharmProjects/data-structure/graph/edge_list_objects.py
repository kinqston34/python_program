class Node:
    
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.neighbors = [] #nodes
        self.predecessor = None

    def __repr__(self):
        return 'Node(name={})'.format(self.name)

# print('測試開始')
# key = Node('玩具')
# print(key)
