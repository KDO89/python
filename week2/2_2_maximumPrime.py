def maximum_prime(n):
    divisor = 2
    while True:
        if n == divisor:
            return divisor
        if n % divisor == 0:
            n = n // divisor
            continue
        else:
            if divisor != 2:
                divisor += 2
            else:
                divisor = 3
            continue
print("divisor is " + str(maximum_prime(50)))
