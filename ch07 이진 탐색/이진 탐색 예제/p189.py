n,m=10,7
array=[1,3,5,7,9,11,13,15,17,19]

def binarySearch(array,start,end,target):
  if start>end:
    return None
  mid=(start+end)//2
  if(array[mid]==target):
    return mid
  
  elif(array[mid]>target):
    return binarySearch(array,start,mid-1,target)
  
  else:
    return binarySearch(array,mid+1,end,target)

result=binarySearch(array,0,n-1,m)
if result==None:
  print("원소가 존재하지 않습니다")
else:
  print(result+1)