Name = input("Enter file name: ")
try:
    with open(Name, "r") as file:
        line = file.readlines()
       
        if len(line) <= 5:
            print("File contains less than or equal to 5 lines. Display all lines")
            for line in line:
                print(line.strip())
        else:
            print("File contains more than 5 lines. Displaying first 5 lines:")
            for line in line[:5]:
                print(line.strip())
except FileNotFoundError:
    print(f"The file '{Name}' was not found. Please make sure it exists in the current directory.")