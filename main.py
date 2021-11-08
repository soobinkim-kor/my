#하노이 횟수 count
def Hanoi(n,k):
  a=loops(n,"첫째","둘째","셋째",k,0)
  print(a)


def loops(n,a,b,c,k,count):
  if n==1:
    if k==1:
      count+=1
      print("원판%d를 %s에서 %s로 옮긴다. 총%d번째" % (n,a,c,count))
      return count
    else:    
      print("원판%d를 %s에서 %s로 옮긴다." % (n,a,c))
      return count
  
  else:
    if k==n:
      count=loops(n-1,a,c,b,k,count)
      count+=1
      print("원판 %d를 %s에서 %s로 옮긴다. 총 %d번째" %(n,a,c,count))
      count=loops(n-1,b,a,c,k,count)
    else:
      count=loops(n-1,a,c,b,k,count) #hanoi
      print("원판 %d를 %s에서 %s로 옮긴다." %(n,a,c))
      count=loops(n-1,b,a,c,k,count) #hanoi
    return count

Hanoi(3,2)