def sieve(n):
  """Finding sieve of Eratosthenes"""
  list = []
  sieveList = []
  i = 2
  while i <= n:
    list = list + [i]
    i = i + 1
  p = 0
  while True:
    i = p
    sieveList = sieveList + [list[p]]
    while i < len(list):
      if list[i] % list[p] != 0:
        sieveList = sieveList + [list[i]]
      i = i + 1
    p = p + 1
    list = []
    list.extend(sieveList)
    sieveList = []
    sieveList = list[:p]
    if p == len(list):
      break
  return sieveList
print(sieve(30))
