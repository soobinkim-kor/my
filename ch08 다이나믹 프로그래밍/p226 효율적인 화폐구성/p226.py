n=3
m=4
array=[3,5,7]
d=[10001]*(m+1)
for i in range(n):
  d[i]=array[i]
for i in range(n):
  for j in range(array[i],m+1):
    if d[j-array[i]]!=10001:
      d[j]=min(d[j-array[i]]+1)

if d[m]==10001:
  print(-1)
else:
  print(d[m])