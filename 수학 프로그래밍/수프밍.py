def permut(array):
  if len(array)==1:
    return [array]
  res=[]
  for permutation in permut(array[1:]):
    for i in range(len(array)):
      res.append(permutation[:i] + array[0:1] + permutation[i:])
  return res

print(permut([2,3]))

def nextPerm(A):
  kposition=0     # k 인덱스
  lposition=0     # l 인덱스

  # 1. a[k]<a[k+1] 인 가장 큰 k 찾기
  for k in range(len(A)-1):
    if A[k]<A[k+1]:
      kposition=k
  
  # a[k]<a[k+1] 인 값이 없을 때 (내림차순으로 되어있을 때)
  if kposition==0:
    return 'no next permutation'
  #2. k보다 큰 인덱스 중 a[k]<a[l] 인 가장 큰 인덱스 l 찾기
  for l in range(kposition,len(A)):
    if A[kposition]<A[l]:
      lposition=l

  #a[k] 와 a[l] 을 바꾼다
  A[kposition],A[lposition]=A[lposition],A[kposition]

  #a[k+1,...,n] 의 순서를 뒤집는다
  A=A[0:kposition+1]+fliplist(A[kposition+1:])
  return A

def fliplist(a):
    for i in range(0,len(a)//2):
        a[i],a[len(a)-1-i]=a[len(a)-1-i],a[i]
    return a

def bubblesort(S):
    for i in range(len(S)):
        for j in range(len(S)-i-1):
            if S[j]>S[j+1]:
                S[j],S[j+1]=S[j+1],S[j]
    return S

def nextComb(n,S):
  S=bubblesort(S)
  findI=0
  for i in range(len(S)):
    if S[i]!=n-len(S)+i+1:
      break
    return "no next combination"

  for i in range(len(S)):
    if S[i]!=n-len(S)+i+1:
      findI=i

  S[findI]=S[findI]+1

  for j in range(findI+1,len(S)):
    S[j]=S[findI]+j-findI
  
  return S
 
print(nextComb(3,[1,2]))
print(nextComb(3,[1,3]))
print(nextComb(4,[1,2,4,3]))
print(nextComb(3,[1]))
print(nextComb(3,[3,5,2,1]))

