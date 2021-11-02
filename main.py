import numpy

n = [[1,4,5],[4,1,2],[4,8,1]]
m=[[1,2,3,4],[2,4,5,1],[5,2,1,2],[5,1,2,4]]

det1=numpy.linalg.det(m)
det = numpy.linalg.det(n)

print(det1)
print (det)


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
print(matrixDet(A))
print(matrixDet(B))
print(matrixDet(m))