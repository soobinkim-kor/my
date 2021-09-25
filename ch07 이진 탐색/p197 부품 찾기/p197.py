n=5
shop=[8,3,7,9,2]

m=3
request=[5,7,9]

shop.sort()
request.sort()
result=[]

def binarySearch(array,target,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  if(array[mid]==target):
    return mid
  elif array[mid]>target:
    return binarySearch(array,target,start,mid-1)
  else:
    return binarySearch(array,target,mid+1,end)

for requests in request:
  if(binarySearch(shop,requests,0,len(shop)-1)!=None):
    print("yes",end=' ')
  else:
    print("no",end=' ')