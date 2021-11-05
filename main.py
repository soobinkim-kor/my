import numpy



def makeZeroMatrix(n,m):
  A=[]
  for i in range(n):
    A=A+[[0]*m]
  return A

def makeC(A,i,j):
  n=len(A)
  B=makeZeroMatrix(n-1,n-1)
  for a in range(n-1):
    for b in range(n-1):
      if a>=i and b<j:
        B[a][b]=A[a+1][b]
      elif a<i and b>=j:
        B[a][b]=A[a][b+1]
      elif a>=i and b>=j:
        B[a][b]=A[a+1][b+1]
      else:
        B[a][b]=A[a][b]
  return B

A=[[1,1,0],[2,2,1],[0,1,1]]
B=[[1,4,5],[4,1,2],[4,8,1]]
# 1 1 0 
# 2 2 1
# 0 1 1

# 1 4 5
# 4 1 2
# 4 8 1
-15+16+140
def matrixDet(A):
    if len(A)==1: return A[0][0]

    if len(A) == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]

    determinant = 0

    for j in range(len(A)):
      C_1=makeC(A,0,j)
      determinant=determinant+A[0][j]*(-1)**(j)*matrixDet(C_1)

    return determinant


#3 x 2 (len(A[0])),len(A))
A=[[1,1,0],[2,2,1]]

def transpose(A):
  n=len(A) #    2
  m=len(A[0])#  3
  b=makeZeroMatrix(m,n)
  for i in range(len(A)):
    for j in range(len(A[0])):
      b[j][i]=A[i][j]
  return b

def inverse(A):
  b=makeZeroMatrix(len(A),len(A))
  A=transpose(A)
  for i in range(len(A)):
    for j in range(len(A)):
      b[i][j]=(-1)**(i+j)*matrixDet(makeC(A,i,j))/matrixDet(A)
  return b


B=[[1,2,3],[0,1,4],[5,6,0]]
#print(inverse(A))


print(inverse(B))
b=numpy.linalg.inv(B)
print(b)