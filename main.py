def lucas(n):
  if n==0:
    return 2
  elif n==1:
    return 1
  return lucas(n-1)+lucas(n-2)



def lucas2(n):
  def f(n):
    if n==1 or n==2:
      return 1
    return f(n-1)+f(n-2)

  return f(2*n)-lucas(n)-f(n)

print(lucas(1))
print(lucas(2))
print(lucas(3))
print(lucas(4))
print(lucas(5))



print(lucas2(1))
print(lucas2(2))                                                                                                
print(lucas2(3))
print(lucas2(4))
print(lucas2(5))

