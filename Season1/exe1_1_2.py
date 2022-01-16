import functools

def copy(x):
    return f'{x}{x}'


def double_letter(my_str):
    return ''.join(map(copy, my_str))


print(double_letter("python"))
print(double_letter("we are the champions!"))