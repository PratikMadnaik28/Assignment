numbers = []
for i in range(5):
    n = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(n)

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)

print("Sum of 5 numbers is", calculate_sum(numbers))
print("Average of 5 numbers is", calculate_average(numbers))