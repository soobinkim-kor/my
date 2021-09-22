# n,m=map(int,input().split())
# first=list(map(int,input().split()))
# second=list(map(int,input().split()))

n,m=5,1

first=[1,2,5,4,3]
second=[5,5,6,6,5]


first.sort()
second.sort(reverse=True)
result=0

for i in range(n):
  if(m==0):
    break
  if(first[i]<second[i]):
    first[i],second[i]=second[i],first[i]
    m=m-1

for i in range(n):
  result+=first[i]

print(result)