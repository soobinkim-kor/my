n=5
shop=[8,3,7,9,2]

m=3
request=[5,7,9]

shop.sort()
request.sort()
result=[]
for i in range(len(m)):
  for j in range(len(n)):
    if(request[i]==shop[j]):
      result+="yes"
  
    elif(j==len(n)-1):
      result+="no"


