import math
N=int(input())
total = 0
for j in range(1,N):
  total+= (1/j**2)
print("\t",total)