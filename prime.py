
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2 , num):
        if num % i == 0:
            return False
        return True
    
    
number = 100000778
if is_prime(number):
    print("is a prime number:" , num)
else:
    print("is not a prime number:", num)



