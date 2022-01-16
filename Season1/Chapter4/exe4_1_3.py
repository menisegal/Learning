

import main as m


def first_prime_over(num):
    prime_generator = (n for n in range(num,num ** num) if m.is_prime(n))
    return next(prime_generator)












print(first_prime_over(1000000))