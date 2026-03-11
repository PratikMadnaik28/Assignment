#1 Write a Python program to create a set
my_set = set()

#2 Write a Python program to iteration over sets
my_set = {1, 2, 3, 4, 5}

for item in my_set:
    print(item)
    
#3 Write a Python program to add member(s) in a set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

#4 ⁠Write a Python program to remove item(s) from a given set
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)

#5 ⁠Write a Python program to remove an item from a set if it is present in the set.
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set)