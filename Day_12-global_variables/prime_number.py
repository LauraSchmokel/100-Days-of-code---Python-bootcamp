
def is_prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
        
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    
    else:
        return True
    
num = int(input("Insert a number. Let us check if it is prime or not: "))

print(f"The number {num} is prime? {is_prime(num)}")