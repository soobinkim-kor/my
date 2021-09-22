n=5
shop=[8,3,7,9,2]

m=3
request=[5,7,9]

shop.sort()

print(shop)
print(request)

def binarySearch(array,target,start,end):
  if(start>end):
    return None

  mid=(start+end)//2
  
  if(array[mid]==target):
    return mid
  
  elif(array[mid]>target):
    return binarySearch(array,target,start,mid-1)
  
  else:
    return binarySearch(array,target,mid+1,end)

answer=""

for i in range(m):
  result=binarySearch(shop,request[i],0,n-1)
  if(result==None):
    answer+="no "
  else:
    answer+="yes "
print(answer)