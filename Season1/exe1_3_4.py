
# k -> m
# o -> q
# e -> g

def replace(x):
    return chr(ord(x) + 2)


def double_letter(my_str):
    return ''.join(map(replace, my_str))

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"


p = double_letter(password)

print(p)



a = ''.join([chr(ord(x) + 2) for x in password])

print(a)