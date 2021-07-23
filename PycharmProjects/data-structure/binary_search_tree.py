class Node:                        #建立節點
    def __init__(self,value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None   #pointer
class bineary_search_tree:          #建立二元搜尋樹
    def __init__(self):
        self.root = None

    def insert(self,value):           #insert 二元搜尋樹
        if self.root == None:         #如果是根
            self.root = Node(value)
        else:                             #不是根 則向下insert
            self._insert(value,self.root)
    def _insert(self,value,cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value,cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("This value has existed")

    def height(self):               #找樹高度
        if self.root != None:
            return self._height(self.root,0)
    def _height(self,cur_node,cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child,cur_height+1)
        right_height = self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)

    def find(self,value):               #搜尋value->node
        if self.root == None:
            return None
        else:
            return self._find(value,self.root)
    def _find(self,value,cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value,cur_node.right_child)

    def delete_value(self,value):                   #刪除node
        return self.delete_node(self.find(value))   #<---在這裡呼叫find

    def delete_node(self,node):
        def min_value_node(n):     #use in case 3   #找到刪除node後,parent要指向的node(最小的)
            current = n
            while current.left_child !=None:
                current = current.left_child
            return current

        def count_children(n):
            num_children = 0
            if n.left_child != None:
                num_children+=1
            if n.right_child != None:
                num_children+=1
            return num_children

        node_parent = node.parent
        node_children = count_children(node)

        #判斷刪除三種情形
        #case 1 : node has no children
        if node_children == 0:
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        #case 2 : node has one children
        if node_children == 1:
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            child.parent = node_parent
        #case 3 : node has two children
        if node_children == 2:
            successor = min_value_node(node.right_child)
            node.value = successor.value
            self.delete_node(successor)

    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False
    def _search(self,value,cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value,cur_node.right_child)
        else:
            return False

    def print_tree(self):               #print tree
        if self.root != None:
            self._print_tree(self.root)
    def _print_tree(self,cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

def fill_tree(tree,num_elems=10,max_int = 50):          #亂數建立
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0,max_int)               #亂數的node
        tree.insert(cur_elem)                       #將node 傳入開始建樹
    return tree             #傳回整棵樹(root)

tree = bineary_search_tree()  #建立實體物件
tree = fill_tree(tree)    #亂數產生node 並 insert 方法
tree.print_tree()         #印樹

tree1 = bineary_search_tree()
for num in range(10):
    tree1.insert(num)
tree1.delete_value(5)
tree1.print_tree()