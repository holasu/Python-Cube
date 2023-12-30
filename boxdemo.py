x = int(input("Enter the bricks numbers: "))

for k in range(x):
    for i in range(x):
        if ((k > 0) & (k < (x-1))) and ((i > 0) & (i < (x-1))):
            print("  ", end=" ")
        else:
            print("# ", end=" ")
    print()

