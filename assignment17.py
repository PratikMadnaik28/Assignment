try:
    with open("numbers.txt", "r") as file:
        for line in file:
            try:
                num = int(line.strip())
                print(f"Read number: {num}")
            except ValueError:
                print(f"Invalid number found in file: '{line.strip()}'. Skipping this line.")
except FileNotFoundError:
    print("The file 'numbers.txt' was not found. Please make sure it exists in the current directory.") 