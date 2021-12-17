#우애수 찾기
# DP로 풀기

def divisorSum(n):  # 자기 자신을 제외한 약수의 합을 구하는 함수
  sum=0
  for i in range(1,n//2+1):
    if n%i==0:
      sum+=i
  return sum

def chain(n,a): #적어도 1개 숫자가 a 이상인 n 길이의 친화수
  numberDivSum=dict()
  #divisorSumMap=[]  #인덱스 0번째 = 0.  
  for i in range(a+1):
    numberDivSum[i]=[divisorSum(i)]
  numberDivSum=sorted(numberDivSum.items(),key=lambda item: item[1])
  return numberDivSum

print(chain(1,100))