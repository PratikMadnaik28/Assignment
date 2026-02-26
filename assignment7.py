number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 3, 7, 2, 9, 1, 3, 5, 8, 2, 4]
n = int(input("Enter a number between 1 and 9: "))

for index, value in enumerate(number):
    if value == n:
        print("The number", n, "appears at index", index)
if n not in number:
    print("The number does not exist in the list.")


