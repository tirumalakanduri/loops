number = int(input("enter the number : "))
if number > 1:
    for i in range(2, int(number ** 0.5) +1 ):
        if number %i == 0:
            print(f" the given number { number } is not a prime a number")
            break
        else:
            print(f" the given number { number } is  a prime a number")
else:
    print(f" the given number { number } is not a prime a number")

print("end")
            