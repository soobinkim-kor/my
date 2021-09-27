from collections import deque

#아래, 위, 오른쪽, 왼쪽
dx=[1,-1,0,0]
dy=[0,0,-1,1]

def solution(maps):
    answer = 0
    visited=[[False]*len(maps[0]) for _ in range(len(maps))]
    bfs(0,0,maps,visited)
    if visited[len(maps)-1][len(maps[0])-1]==False:
        return -1
    return maps[len(maps)-1][len(maps[0])-1]

def bfs(x,y,maps,visited):    
    queue=deque()
    queue.append([x,y])
    while(queue):
        x,y=queue.popleft()
        visited[x][y]=True       
        for i in range(4):
            newx=x+dx[i]
            newy=y+dy[i]
            if(newx<0 or newy<0 or newx>=len(maps) or newy>=len(maps[0])):
                continue
            if maps[newx][newy]==1 and visited[newx][newy]==False:
                visited[newx][newy]=True
                maps[newx][newy]=maps[x][y]+1
                queue.append([newx,newy])