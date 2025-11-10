import math as m

def largest_prime_factor(n:int):
  prime = False
  factors = []
  while (not prime):
    M = m.floor(m.sqrt(n))
    for i in range(2, M+1):
      if n % i == 0:
         n = n //i
         factors.append(i)
         break
      if i == M:
        factors.append(n)
        prime = True
  return factors[-1]

