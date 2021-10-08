#텀 프로젝트

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
t = int(input())

def dfs(x):
  global result
  visited[x] = 1
  cycled.append(x)
  next = graph[x]
  if visited[next] == 1:
    if next in cycled:
      result+=cycled[cycled.index(next):]
  else:
      dfs(next)


for i in range(t):
    graph = dict()
    n = int(input())
    students = list(map(int, input().split()))
    result=[]
    for i in range(len(students)):
        graph[i + 1] = students[i]
    visited = [0] * (n + 1)
    for i in range(1,n+1):
      if visited[i]==0:
        cycled=[]
        dfs(i)
    print(n-len(result))