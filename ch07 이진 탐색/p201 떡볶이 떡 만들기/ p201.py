n,m=list(map(int,input().split(' ')))
array=list(map(int,input().split()))
start=0
end=max(array)

def calcleft(array,start,end):
  mid=(start+end)//2
  left=0
  for acomp in array:
    if(acomp-mid<=0):
      continue
    else:
      left+=acomp-mid
  
  if(left>m):
    return calcleft(array,mid+1,end)

  elif left==m:
    return mid
  
  else:
    return calcleft(array,start,mid-1)

print(calcleft(array,start,end))