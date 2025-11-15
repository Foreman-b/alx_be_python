rows = int(input("Enter the size of the pattern: "))

i = 1
while i <= rows:
    j = 1
    for j in range(rows):
        j += 1
        print("*", end="")
    for k in range(i):
        print("", end="")
        k += 1
    print()
    i += 1