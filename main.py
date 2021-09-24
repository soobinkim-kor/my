
a=[1,2,3,4]
b=[4,5,6,2,1]
c=[1,2,3,4,5,6,7,8,9,10]

# 길이가 홀수일때, 짝수일 때 로 나눠서 생각
# 길이가 짝수이면 길이/2 까지 바꾸면 됨.
# 길이가 홀수이면 가운데 숫자를 제외하고 다 바꾸면 됨
# (길이/2) 를 소수점 버림하면 위 경우를 모두 충족

def FlipList(a):
  length=len(a)
  for i in range(len(a)//2):
    a[i], a[length-i-1] = a[length-i-1], a[i]
  return a

print(FlipList(a))
print(FlipList(b))
print(FlipList(c))