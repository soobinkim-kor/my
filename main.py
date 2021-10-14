#달이 차오른다, 가자

import sys
from collections import deque
input=sys.stdin.readline

"""첫째 줄에 미로의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 50) 둘째 줄부터 N개의 줄에 미로의 모양이 주어진다. 같은 타입의 열쇠가 여러 개 있을 수 있고, 문도 마찬가지이다. 그리고, 영식이가 열쇠를 숨겨놓는 다면 문에 대응하는 열쇠가 없을 수도 있다. 0은 한 개, 1은 적어도 한 개 있다. 그리고, 열쇠는 여러 번 사용할 수 있다.

예제1
1 7
f0.F..1
7

예제2
5 5
....1
#1###
.1.#0
....A
.1.#.

-1

예제3
7 8
a#c#eF.1
.#.#.#..
.#B#D###
0....F.1
C#E#A###
.#.#.#..
d#f#bF.1

55
"""
#소문자 unicode = 97~122
#대문자 unicode = 65~90

#오른쪽, 왼쪽, 위, 아래
dx=[1,-1,0,0]
dy=[0,0,-1,1]
#보유중인 키 
keys=[]
#방문

maze=[]
answer=0
n,m=map(int,input().split())

for i in range(n):
  l=[]
  line=input()
  for j in range(m):
    l.append(line[j])
  maze.append(l)

for i in range(n):
  for j in range(m):
    if maze[i][j]=='0':
      x,y=i,j

def bfs(x,y):
  global answer
  queue=deque([[x,y]])

  while(queue):
    print(maze)
    current=queue.popleft()
    print("현재 위치",current)
    print(keys)
    x=current[0]
    y=current[1]

    if maze[x][y]==1:
      return answer

    for i in range(4):
      # nx, ny = 이동하려는 x,y 
      nx,ny=x+dx[i],y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=m:
        continue    

      if maze[nx][ny]=='.':

        print(current,"방문")
        answer+=1
        queue.append([nx,ny])
      
      if ord(maze[nx][ny])>=97 and ord(maze[nx][ny])<=122:

        keys.append(maze[nx][ny])
        print([nx,ny],"에서 열쇠",maze[nx][ny],"획득")
        maze[nx][ny]='.'
        answer+=1
        queue.append([nx,ny])

      elif ord(maze[nx][ny])>=65 and ord(maze[nx][ny])<=90:
        if maze[nx][ny].lower() in keys:
          maze[nx][ny]='.'
          print([nx,ny],"에서 열쇠",maze[nx][ny],"사용")
          answer+=1
          queue.append([nx,ny])
        else:
          continue
    
      
print(x,y)

print(ord('F'))
bfs(x,y)

print(answer)