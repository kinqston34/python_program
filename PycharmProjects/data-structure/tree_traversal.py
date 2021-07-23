data = [0,1,2,3,4,5,6]

def preorder(i):
    if i < 7:
        print(data[i],end=' ')
        preorder(i*2+1)
        preorder(i*2+2)
def inorder(i):
    if i < 7:
        inorder(i*2+1)
        print(data[i],end=' ')
        inorder(i*2+2)
def postorder(i):
    if i < 7:
        postorder(i*2+1)
        print(data[i],end=' ')
        postorder(i*2+2)
preorder(0)
print('\n')
inorder(0)
print('\n')
postorder(0)
