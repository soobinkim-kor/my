def perm(A,r):
    res=[]
    if r==1:
        for item in A:
            res.append([item])
        return res
    for i in range(0,len(A)):
        B=A[:i]+A[i+1:]
        for permutation in perm(B,r-1):
            res.append([A[i]]+permutation)
    return res
def bubblesort(S):
    for i in range(len(S)):
        for j in range(len(S)-i-1):
            if S[j]>S[j+1]:
                S[j],S[j+1]=S[j+1],S[j]
    return S
def combinations(n,r):
  answer=[]
  numbers = list(range(1, n+1, 1))
  permlist=perm(numbers,r)
  for perms in permlist:
    perms=bubblesort(perms)
  
  for perms in permlist:
    if perms not in answer:
      answer.append(perms)
  
  return answer
  print(answer)




combinations(4,3)