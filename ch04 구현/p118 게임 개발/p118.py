# n행 m열 맵
n,m=map(int,input().split())
d=[[0]*m for _ in range(n)]

x,y,direction=map(int,input().split())
d[x][y]=1

array=[]
for i in range(n):
  array.append(list(map(int,input().split())))
#북,동,남,서 움직이기

#dx=[-1,0,1,0]
#dy=[0,1,0,-1]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

#왼쪽으로 회전 북,동,남,서 순
#             0, 1, 2, 3
def turn_left():
  global direction
  direction-=1
  if(direction==-1):
    direction=3

count=1
turn_time=0
while True:
  turn_left()
  nx=x+dx[direction]
  ny=y+dy[direction]
  if d[nx][ny]==0 and array[nx][ny]==0:
    d[nx][ny]=1
    x=nx
    y=ny
    count+=1
    turn_time=0
    continue

  else: turn_time+=1

  if(turn_time==4):
    nx=x-dx[direction]
    ny=y-dy[direction]

    if array[nx][ny]==0:
      x=nx
      y=ny
    else:
      break
    turn_time=0

print(count)
"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
###########
