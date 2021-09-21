n=input()
xaxis='abcdefgh'
x=n[0]
for i in range(len(xaxis)):
  if x==xaxis[i]:
    x=i+1
y=int(n[1])
nx,ny=x,y
print(nx,ny)
dx=[-2,-2,2,2,1,1,-1,-1]
dy=[1,-1,1,-1,2,-2,2,-2]
answer=0

for i in range(len(dx)):
  print("초기 위치 ",x,y)
  x+=dx[i]
  y+=dy[i]
  print("움직인 후 위치 ",x,y)
  if(x<1 or y<1 or x>8 or y>8):
    print("무시된 이동 위치 ",x,y)
    x,y=nx,ny
    continue
  answer+=1
  x,y=nx,ny

print(answer)