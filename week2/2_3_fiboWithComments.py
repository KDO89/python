def fibo(n):
  if n == 0:
      print("fibo(" + str(n) + ")")
      return 0
  if n == 1:
      print("fibo(" + str(n) + ")")
      return 1
  print("fibo(" + str(n - 1) + ") + " + "fibo(" + str(n - 2) + ")")
  return fibo(n - 1) + fibo(n - 2)
print(str(fibo(8)))
