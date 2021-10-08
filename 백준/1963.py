#소수 경로
import sys
import math
from collections import deque
input=sys.stdin.readline

def bfs(start,target):
  visited=[0 for _ in range(10000)]
  visited[start]=1
  queue=deque()
  queue.append([start,0])
  while(queue):
    current,count=queue.popleft()
    if current==target:
      return count 
    for i in range(4):
      for j in range(10):
        changed=changenum(current,j,i)
        if isPrime(changed)==True and visited[changed]==0 and changed>=1000:
          visited[changed]=1
          queue.append([changed,count+1])

def changenum(a,target,th):
  length=len(str(a))
  ret=str(a)[0:th]+str(target)+str(a)[th+1:length]
  return int(ret)

def isPrime(a):
  if a==1:
    return False
  elif a==2:
    return True
  for i in range(2,int(math.sqrt(a))+1):
    if a%i==0:
      return False
  return True

n=int(input())
for _ in range(n):
  a,b=map(int,input().split())
  result=bfs(a,b)
  print(result if result!=None else "Impossible")