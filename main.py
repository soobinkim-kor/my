#하노이 탑
def hanoi(n):
  hanoimove(n,"첫째","셋째","둘째")

def hanoimove(n, from_pos, to_pos, sub_pos):
  if n==1:
    print("원판",n,"을",from_pos, "에서", to_pos , "로 이동")
    return
  hanoimove(n-1,from_pos,sub_pos,to_pos)
  print("원판",n,"을",from_pos, "에서", to_pos, "로 이동")
  hanoimove(n-1,sub_pos,to_pos,from_pos) 
hanoi(3)


def numberHanoi1(n,count):
  if n==1:
    count+=1    
    return count
  hanoimove1(n-1,from_pos,sub_pos,to_pos, count)
  count+=1  
  hanoimove1(n-1,sub_pos,to_pos,from_pos, count)


numberHanoi(3)


