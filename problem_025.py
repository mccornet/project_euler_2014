# What is the first term in the Fibonacci sequence to contain 1000 digits?

def fibonacci():
    f_1 = 1
    f_2 = 1

    yield f_1
    yield f_2

    while True:
        f_3 = f_2 + f_1
        yield f_3
        f_1 = f_2
        f_2 = f_3

fib_gen = fibonacci()

n = 0
while True:
    n += 1
    if next(fib_gen) > 10**999:
        break

print(n)

'''
# using
phi = 1.618033988749895

n = 0.0
while True:
    n += 1

    if n > 5000:
        break

    if (phi**n // (phi + 2)) > 10**999:
        break

print(n)
'''