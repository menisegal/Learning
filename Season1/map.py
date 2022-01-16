import reduce
import time

# we can use lambda function instead of square function
def square(num):
    return num**2


def map_exe():
    list_of_numbers = [2,4,5,6,7]

    # option 1
    map_res = map(lambda x: x**2, list_of_numbers)
    print(list(map_res))

    # option 2
    map_res = map(square, list_of_numbers)
    print(list(map_res))

    print("The variable __name__ tells me which context this file is running in.")
    print("The value of __name__ is:", repr(__name__))


def main():
    print("Hello World!")

if __name__ == "__main__":
    for i in range(10):
        a = time.time()
        print(list(map(lambda x:x**2,range(100))))
        b = time.time()
        print([x ** 2 for x in range(100)])
        c = time.time()
        print("Seconds since epoch =", a)
        print("Seconds since epoch =", b)
        print("Seconds since epoch =", c)
        fst = b-a
        scd = c-b
        print(fst)
        print(scd)
        if (fst > scd):
            print('second')
        else:
            print('first')
        time.sleep(2)
    #local_time = time.ctime(seconds)
    #main()