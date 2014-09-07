def fibo(n):
  if n == 0:
      #print("fibo(" + str(n) + ")")
      return 0
  if n == 1:
      #print("fibo(" + str(n) + ")")
      return 1
  #print("fibo(" + str(n - 1) + ") + " + "fibo(" + str(n - 2) + ")")
  return fibo(n - 1) + fibo(n - 2)
#print(str(fibo(8)))
    
def fib_iter(n):
  a = 0
  b = 1
  count = 0
  while n > 1:
    count = a + b
    a = b
    b = count
    n -= 1
  return count
#print(str(fib_iter(8)))

import time

def compare_functions(f, g, arg):
  i = 0
  t1 = 0
  t2 = 0
  while i < 1000:
    last_time = time.clock()
    f(arg)
    t1 += time.clock() - last_time
    last_time = time.clock()
    g(arg)
    t2 += time.clock() - last_time
    i += 1
  print(t2 / t1)

# допустим fibo1 и fibo2 - это две функции
# вычисляющие значения чисел Фибоначчи,
# но разными методами
compare_functions(fibo, fib_iter, 10)
# после этого вызова на экран будет выведено
# во сколько раз вторая функция работает быстрее
# или медленнее первой
