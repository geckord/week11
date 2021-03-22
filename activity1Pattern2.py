numberOfLines = int(input("How many lines do you want? "))

for i in range(0, numberOfLines):
    for j in range(0, numberOfLines - i):
        print(end=" ")

    for k in range(0, i + 1):
        print("*", end=" ")

    print()
