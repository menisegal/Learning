


def is_prime(num):
    if num <= 1 or num == 1:
        return False

    res = True
    for i in range(2,num):
        if (num % i == 0):
            res = False
            break
    return res








if __name__ == "__main__":
    is_prime()