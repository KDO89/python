def fib_iter(n):
  a = 0
  b = 1
  count = 0
  while n > 1:
    count = a + b
    a = b
    b = count
    n -= 1
    continue
  return count
print(str(fib_iter(8)))
