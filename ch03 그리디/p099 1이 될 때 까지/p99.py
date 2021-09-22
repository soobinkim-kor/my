n,k = map(int,input().split())
answer=0
while(True):
  if(n%k==0):
    n=n/k
  else:
    n=n-1
  answer=answer+1
  if(n==1):
    break
print(answer)