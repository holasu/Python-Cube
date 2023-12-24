# string operations
name = input("Enter a name with length 7 character: ")
if len(name) < 7:
    print(len(name))
    print(name[0])
    print(name[1])
    print(name[0:5])
    print(name[:4])
    print(name[4:])
    print(name[-1])
else:
    print("please enter proper string./n")
