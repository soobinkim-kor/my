n=int(input())
count=0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        count+=1

print(count)


#나의 풀이 = range  60을 이용하지 않았고, 문자열을 따로따로 비교했음. 개선할 것
# 12분/15분
# import time

# start_time=time.time()

# n=int(input())
# hour=0
# minute=0
# sec=0
# answer=0
# while(True):
#   if(sec==60):
#     minute=minute+1
#     sec=0
#   if(minute==60):
#     hour=hour+1
#     minute=0
#   if(hour==n+1):
#     break
#   if('3' in str(hour) or '3' in str(minute) or '3' in str(sec)):
#     answer=answer+1
#   sec=sec+1
# end_time=time.time()
# print(end_time-start_time)
# print(answer)

#1.2750 sec