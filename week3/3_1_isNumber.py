def is_number(x):
  """Finding if the input String is a number"""
  i = 0
  if x[0] == "-":
    numberOfDigitals = 1
  else:
    numberOfDigitals = 0
  numberOfPoints = 0
  while i < len(x):
    if x[i].isdigit():
      numberOfDigitals += 1
    if x[i] == ".":
      numberOfPoints += 1
    i += 1
  if numberOfDigitals + numberOfPoints == len(x) and numberOfPoints <= 1:
    return True
  else:
    return False
print(is_number("1.245"))
