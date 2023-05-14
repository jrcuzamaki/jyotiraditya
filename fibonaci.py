def fibonacci(lower, upper):
    a, b = 0, 1

    if lower < 0:
        lower = 0
        
 
    while b < upper:
        if b >= lower:
            print(b, end=' ')
        a, b = b, a+b

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
fibonacci(lower, upper)
