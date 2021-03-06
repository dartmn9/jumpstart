def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

    n * factorial(n - 1)


print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),
    factorial(3),
    factorial(11)
))


def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums


for n in fibonacci(100):
    print(n, end=(', '))


def fibonacci_co(limit):
    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        yield current


for n in fibonacci_co(100):
    print(n, end=(', '))
