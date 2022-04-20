#우애수 찾기
# DP로 풀기
 
def divisorSum(n):  # 자기 자신을 제외한 약수의 합을 구하는 함수
  sum=0
  for i in range(1,n//2+1):
    if n%i==0:
      sum+=i
  return sum

def chain2(n,a): #적어도 1개 숫자가 a 이상인 n 길이의 친화수
  numberDivSum=dict()
  #divisorSumMap=[]  #인덱스 0번째 = 0.  
  for i in range(a+1):
    numberDivSum[i]=[divisorSum(i)]
  return numberDivSum

def chain(n,a): #적어도 1개 숫자가 a 이상인 n 길이의 친화수
  numberDivSum=dict()
  count=0
  answer=[]
  #divisorSumMap=[]  #인덱스 0번째 = 0.  
  for i in range(a+1):
    numberDivSum[i]=[divisorSum(i)]
  numberDivSum=sorted(numberDivSum.items(),key=lambda item: item[1])
  for i in range(len(numberDivSum)-1):
    if numberDivSum[i][1]!=numberDivSum[i+1][1]:
      if count==n:
        return answer
      else:
        count,answer=0,[]

    if numberDivSum[i][1]==numberDivSum[i+1][1]:
      count+=1
      answer+=numberDivSum[i]
      continue
  print("***")

  return answer
print(chain(3,4000))