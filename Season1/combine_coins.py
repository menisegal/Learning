






def combine(x,y):
    return [f'{x}{i}' for i in y]

def main():
    print("Hello World!")
    print(combine('$', range(5)))

if __name__ == "__main__":
    main()