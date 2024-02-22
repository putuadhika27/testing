def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

# Example usage
input_number = int(input("Enter a number: "))
if is_odd(input_number):
    print("The number is odd.")
else:
    print("The number is even.")

# function to check if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
    #function to check if number is a prime number
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    else:
        return False
    
# Example usage
input_number = int(input("Enter a number: "))
if is_prime(input_number):
    print("The number is prime.")
else:
    print("The number is not prime.")

    #function to query the user for a number and check if it is a prime number
def is_prime():
    number = int(input("Enter a number: "))
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print("The number is not prime.")
                break
        else:
            print("The number is prime.")
    else:
        print("The number is not prime.")

        
