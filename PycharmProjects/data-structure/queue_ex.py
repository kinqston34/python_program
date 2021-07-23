# 給你一疊有1~n編號的牌(1在最上面，n在最下面)，在牌數大於1的時候執行以下操作：「丟掉最
# 上面的牌，並把現在最上面的的牌放到最下面。」
# 求最後剩下的那張牌編號為?(7->6、10->4)
from queue import Queue                 # q.qsize()	回傳佇列大小
#                                         q.empty()	佇列是否為空
#                                         q.put(x)	將元素加入佇列後端
#                                         x=q.get()	取出佇列前端的元素
q = Queue()
n = int(input('請輸入牌數'))
for i in range(1,n+1):
    q.put(i)
while q.qsize() > 1:
    f1 = q.get()   #取出最上面的牌，並刪除queue中元素
    f2 = q.get()
    q.put(f2)
    print("size = %d"%(q.qsize()))
    print('-----------------')
print(q.get())    #印出最後一張牌

