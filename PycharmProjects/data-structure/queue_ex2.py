from queue import Queue
Len = [[0 for i in range(10)]for j in range(10)] #紀錄長度
maze = [[1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,0,1,0,1,1,1,1,1],
        [1,0,0,1,0,1,0,0,0,1],
        [1,0,1,1,0,1,1,0,0,1],
        [1,0,1,0,0,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]]
# 設定 0可走 1走過了或是邊牆
q = Queue()
#設定起點
q.put((1,1))
Len[1][1] = 1
maze[1][1] = 1

while not q.empty():
    now = q.get()
    x,y = now[0],now[1] #現在的點座標
    #右方有路
    if maze[x+1][y+0] == 0:
        nx = x+1
        ny = y+0
        q.put((nx,ny))
        Len[nx][ny] = Len[x][y] + 1
        maze[nx][ny] = 1
    #下方有路
    if maze[x + 0][y + 1] == 0:
        nx = x + 0
        ny = y + 1
        q.put((nx, ny))
        Len[nx][ny] = Len[x][y] + 1
        maze[nx][ny] = 1
    #左方有路
    if maze[x - 1][y + 0] == 0:
        nx = x - 1
        ny = y + 0
        q.put((nx, ny))
        Len[nx][ny] = Len[x][y] + 1
        maze[nx][ny] = 1
        # 左方有路
    if maze[x + 0][y - 1] == 0:
        nx = x + 0
        ny = y - 1
        q.put((nx, ny))
        Len[nx][ny] = Len[x][y] + 1
        maze[nx][ny] = 1
    x,y = q.get()
    print((x,y))
    for nx,ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
        if maze[nx][ny] == 0:
            q.put((nx,ny))
            Len[nx][ny] = Len[x][y] + 1
            maze[nx][ny] = 1
    print('---------------------------')
if Len[8][8] == 0:
    print('沒有路!')
else:
    print('最短路徑為',Len[8][8])
print(Len)