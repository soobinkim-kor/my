def bubble2(A):
  for i in range(len(A)-1):
    for j in range(len(A)-i-1):
      if A[j]<A[j+1]:
        A[j],A[j+1]=A[j+1],A[j]
        print(A)

a=[1,2,5,7,8,3,4]

b=[1,2,5,7,8,3,4]

def bubble23(A):
  for i in range(0,len(A)):
    for j in range(0,len(A)-i-1):
      if A[j]<A[j+1]:
        A[j],A[j+1]=A[j+1],A[j]
        print(A)


bubble2(a)
print()
bubble23(b)
# def bubble2(A):
#   print(A)
#   for i in range(0,len(A)):
#     for j in range(0,len(A)-i-1):
#       if A[j]<A[j+1]:
#         A[j],A[j+1]=A[j+1],A[j]
#         print(A)
#   return A




  
# bubble2([1,2,5,7])