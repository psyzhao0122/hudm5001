def fibonacci_robust(n):
    
    if (not isinstance(n, int)) or (n < 0):
        return -1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_robust(n-1) + fibonacci_robust(n-2)


print("fibonacci.py")
print(fibonacci_robust(6))

