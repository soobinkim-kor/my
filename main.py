# def mergesort2(a):
#   print(a)
#   if len(a)<=1 : return

#   mid=len(a)//2
#   left=a[0:mid]
#   right=a[mid:]
#   mergesort2(left)
#   mergesort2(right)

#   i,l,r = 0,0,0

#   while l<len(left) and r<len(right): 
#     if left[l]>right[r]: ## 여기 등호만 바꾸면 됨
#       a[i]=left[l]
#       l+=1

#     else:
#       a[i]=right[r]
#       r+=1
#     i+=1


#   while l<len(left):
#     a[i]=left[l]
#     i+=1
#     l+=1
#   while r<len(right):
#     a[i]=right[r]
#     i+=1
#     r+=1


def mergesort2(A):
  if len(A)<=1 : return A

  mid=len(A)//2
  left=A[0:mid]
  right=A[mid:]
  mergesort2(left)
  mergesort2(right)

  i,l,r = 0,0,0

  while l<len(left) and r<len(right): 
    if left[l]>right[r]:
      A[i]=left[l]
      l+=1

    else:
      A[i]=right[r]
      r+=1
    i+=1


  while l<len(left):
    A[i]=left[l]
    i+=1
    l+=1
  while r<len(right):
    A[i]=right[r]
    i+=1
    r+=1

a=[1,5,2,8,0,3]

print(mergesort2(a))