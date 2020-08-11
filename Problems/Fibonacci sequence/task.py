def fibonacci(n):
    a, b = 0, 1
    yield a
    yield b
    i = 2
    while i < n:
        a, b = b, a + b
        yield b
        i += 1
