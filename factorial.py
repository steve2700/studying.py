# code to find the factorial of a given number in Python and explain the code logic.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n *factorial(n-1)
    

number = int(input("please enter a factorial number: "))
print("factorial number for the one you provided is",factorial(number))
