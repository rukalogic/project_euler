def sum_of_multiples(limit:int) -> int:
  three_multiple_sum = (3*(limit//3)*(limit//3 + 1))//2
  five_multiple_sum = (5*((limit-1)//5)*((limit-1)//5 + 1))//2
  fifteen_multiple_sum = (15*(limit//15)*(limit//15 + 1))//2
  return three_multiple_sum + five_multiple_sum - fifteen_multiple_sum

print(sum_of_multiples(1000))
