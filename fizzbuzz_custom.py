tom(a, b, n):
    result = []
    for i in range(1, n+1):
        if i % a == 0 and i % b == 0:
            result.append("FizzBuzz")
        elif i % a == 0:
            result.append("Fizz")
        elif i % b == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return " ".join(result)

a = 3
b = 5
n = 15
print(fizzbuzz_custom(a, b, n))

