from collections import deque

#상, 하, 좌, 우
dx=[0,0,-1,1]
dy=[1,-1,0,0]

# n,m=5,6

# graph=[
#   [1,0,1,0,1,0],
#   [1,1,1,1,1,1],
#   [0,0,0,0,0,1],
#   [1,1,1,1,1,1],
#   [1,1,1,1,1,1]
# ]

n,m=3,3
graph=[
  [1,0,0],
  [0,1,0],
  [0,1,1]
]

def bfs(x,y):
  #queue 선언
  queue=deque()
  
  #(x,y) 넣음
  queue.append((x,y))
  
  #queue.isEmpty
  while queue:
    #입력 좌표 제거
    x,y=queue.popleft()

    #4가지 방향으로 큐 탐색
    for i in range(4):
      #newx,newy로 이동
      newx=x+dx[i]
      newy=y+dy[i]

      #범위에서 벗어날 경우 제외
      if(newx<0 or newy<0 or newx>=n or newy>=m):
        continue
      
      #방문하지 않은 노드이면
      if graph[newx][newy]==1:
        #길이 +1
        graph[newx][newy]=graph[x][y]+1
        #새로운 좌표에서 큐 시작
        queue.append((newx,newy))

  #가장 오른쪽 아래까지의 거리      
  return graph[n-1][m-1]

print(bfs(0,0))

"""
n,m=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))
visited=[[False]*n for _ in range(m)]
"""