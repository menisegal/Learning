def factorial(num):
    if not isinstance(num, int):
        print ("Error")
    else:
        sum = 1
        for i in range(1,num+1,1):
            sum *= i

        return sum; 