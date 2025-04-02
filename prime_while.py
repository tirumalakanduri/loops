number = int(input("enter the number : "))
i = 2
if number <= 1:
    print(f"the given number {number} is not a prime number")
else: 
    i = 2
    while i < number: 
        if number % 1 == 0:
            print(f"the given number {number} is not a prime number")
            break
        i+= 1
    else:
        print(f"the given number {number} is a prime number")


