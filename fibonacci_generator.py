# We want to construct fibonacci
"""
Fibonacci

index   0   1   2   3   4   5   6   7   ...
f(i)    0   1   1   2   3   5   8   13  ...
"""

# Define i-th fibonacci number

def fibo(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i > 1:
        return fibo(i-1) + fibo(i-2)

print(fibo(6))