cat = range(30)
print(list(cat))
cat1 = range(5, 30)
print(list(cat1))
cat = range(7, 30, 3)
print(list(cat))
print(type(cat))

# range descending
for i in range(100, 25, -7):
    print(i, end=" ")
print()

# print the list
days = ["monday", "tuesday", "wednesday", "tuesday"]
for i in range(len(days)):
    print(days[i], end=" ")
