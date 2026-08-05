def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

while True:
    num = input("Enter number: ")
    print(is_prime(int(num)))
    User_choice = input("Would you like to continue? (y/n): ").lower()
    if User_choice != "y":
        break
