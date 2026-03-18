n = int(input("Enter a number: "))

def factorial(n):
    for i in range(1, n):
        n *= i
    return n

print("Factorial of", n, "is", factorial(n))