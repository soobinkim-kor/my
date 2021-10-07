import sys
from collections import deque

input=sys.stdin.readline

n,m,k,x=map(int,input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
print(graph)
distance=[-1]*(n+1)
distance[x]=0

queue=deque([x])
while(queue):
  print(queue)
  current=queue.popleft()
  for node in graph[current]:
    if distance[node]==-1:
      distance[node]=distance[current]+1
      queue.append(node)
has=False
for i in range(len(distance)):
  if distance[i]==k:
    print(i)
    has=True

if has==False:
  print(-1)