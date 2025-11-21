def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
