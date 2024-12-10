def fibonacci_robust(n):
    
    if (not isinstance(n, int)) or (n < 0):
        return -1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_robust(n-1) + fibonacci_robust(n-2)


import sys
#不可以直接输出sys.argv[1]因为他们是string type，要转换为int
print(sys.argv[0])
print(fibonacci_robust(int(sys.argv[1])))



#另一种方式
#n = int(sys.argv[1])
#result = fibonacci_robust(n)

#print(f"Fibonacci number at position {n} is: {result}")


#print("fibonacci.py")
#print(fibonacci_robust(6))

