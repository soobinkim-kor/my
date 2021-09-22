array=[7,5,9,0,3,1,6,2,4,5]

for i in range(len(array)):
  index=i
  for j in range(i+1,len(array)):
    if(array[index]>array[j]):
      index=j
  array[i],array[index]=array[index],array[i]

print(array)