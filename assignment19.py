n = [1, 3, 5, 7, 9]
n1 = [ 2, 4, 6, 8]
n[2] = n1
print(n)

flat = list(item for sublist in n for item in (sublist if isinstance(sublist, list) else [sublist]))
result = sorted(flat)
print(result)