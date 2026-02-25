total = 0

for i in range(1, 6):
    bugs = int(input("Enter the number of bugs collected on day " + str(i) + ": "))
    total += bugs
    print("Total bugs collected this week: ", total)