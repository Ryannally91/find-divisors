def divisors(integer):
  a = []
  for i in range(2, integer):
    if integer % i == 0:
      a.append(i)
  if len(a) == 0:
    return f'{integer} is prime'
  else:
    retun prime
