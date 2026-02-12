# Week 1 – Professional FizzBuzz Function

def fizzbuzz_optimized(n: int):
    result = []

    for num in range(1, n + 1):
        if num % 15 == 0:
            value = "FizzBuzz"
        elif num % 3 == 0:
            value = "Fizz"
        elif num % 5 == 0:
            value = "Buzz"
        else:
            value = str(num)
        result.append(value)

    print(" ".join(result))

number = int(input("Enter a number: "))
fizzbuzz_optimized(number)
