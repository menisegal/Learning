import functools


def multy(x,y):
    return x*y

my_list = [200, 123,3213,3213,31123]

print(functools.reduce(multy, my_list))

print("The variable __name__ tells me which context this file is running in.")
print("The value of __name__ is:", repr(__name__))


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()