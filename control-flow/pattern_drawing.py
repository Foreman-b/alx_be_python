rows = int(input("Enter the size of the pattern: "))

i = 0
while i in range(rows):
    j = 0
    for j in range(rows):
        j += 1
        print("*", end="")
    for k in range(i):
        print("", end="")
    print()
    i += 1