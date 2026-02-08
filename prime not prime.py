a = int(input("Enter number: "))

if a <= 1:
    print("Not Prime")
else:
    for n in range(2, int(a**0.5) + 1):
        if a % n == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
