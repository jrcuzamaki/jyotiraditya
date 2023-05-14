def recur(n):
    if n == 0:
        return 1
    else:
        return n * recur(n-1)
num = int(input("Enter a number: "))
result = recur(num)
print(f"The recursion of {num} is {result}")
