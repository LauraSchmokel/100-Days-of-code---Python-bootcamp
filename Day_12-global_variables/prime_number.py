# Day 12 - Global and Local Scope
# Topics: global vs local scope, function definitions, prime number logic
# What I learned: the difference between global and local variables and how scope affects data access

def is_prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
        
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        return False
    
    else:
        return True
    
num = int(input("Insert a number. Let us check if it is prime or not: "))

print(f"The number {num} is prime? {is_prime(num)}")