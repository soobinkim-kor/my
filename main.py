#배주항등식
def extended_gcd(a,b):
  if a==0:
    return [0,1,b]
  else:
    c = extended_gcd(b%a,a)
    x,y,d=c[0],c[1],c[2]
    return [y-(b//a)*x,x,d]

def bezout3(a,b,c):
  i=extended_gcd(a,b)
  j=extended_gcd(i[2],c)
  return [i[0]*j[0],i[1]*j[0],j[1]]


def gcd(a,b):
  if a==0: return b
  elif b==0: return a
  elif a==b: return a
  elif a>b: return gcd(a-b,b)
  return gcd(a,b-a)

def gcd2(a,b):
  if a==0:return b
  return gcd(b%a,a)

def lcm(a,b):
  return a*b/gcd(a,b)

print(bezout3(2,3,5))
print(bezout3(4,6,9))