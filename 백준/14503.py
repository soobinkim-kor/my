#로봇 청소기

import sys

input=sys.stdin.readline

# (r,c) r= 북쪽으로부터 떨어진 칸/ c= 서쪽으로부터 떨어진 칸
#북, 동, 남, 서
#0,  1,  2,  3
dr=[-1,0,1,0]
dc=[0,1,0,-1]


def clean(r,c,d):
  global answer
  if room[r][c]==0:
    room[r][c]=2
    answer+=1
  for _ in range(4):
    nd=(d+3)%4
    nr=r+dr[nd]
    nc=c+dc[nd]
    if(room[nr][nc]==0):
      clean(nr,nc,nd)
      return
    d=nd
  nd=(d+2)%4
  nr=r+dr[nd]
  nc=c+dc[nd]
  if room[nr][nc]==1:
    return
  clean(nr,nc,d)  

n,m=map(int,input().split())
r,c,d =map(int,input().split())
room=[list(map(int,input().split())) for _ in range(n)]

answer=0
clean(r,c,d)
print(answer)