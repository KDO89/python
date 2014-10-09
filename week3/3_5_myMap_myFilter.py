from math import sqrt

def myMap(function, sequence):
  result = []
  for x in sequence:
    result.append(function(x))
  return result
print(list(map(sqrt, [9, 25, 133])))
print(myMap(sqrt, [9, 25, 133]))

def lessThenZero(x):
  if x < 0:
    return True
  else:
    return False

def myFilter(function, sequence):
  result = []
  for x in sequence:
    if function(x):
      result.append(x)  
  return result
print(list(filter((lambda x: x < 0), [2, 3, -1, -5, 6])))
print(myFilter(lessThenZero, [2, 3, -1, -5, 6]))
  
  
