while True:
    try:
        num = int(input("Enter a number: "))
        if num <=0:
            raise ValueError("Number must be positive.")
        print(f"Square of {num} is {num**2}")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid positive integer.")
        break

print("Program exists")
