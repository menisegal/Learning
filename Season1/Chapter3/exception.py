
import sys

def main():
    try:
        i = 5
        j = 0

        v = i/j
    except:
        print("Done")

def get_file_line_num(file_name):
    print("Read file name:", file_name)
    try:
        f = open(file_name)
    except IOError:
        print("IO Error with file: ", file_name)
    else:
        print("Number of lines in file: ", len(f.readlines()))
        f.close()


if __name__ == "__main__":
    for arg in sys.argv:
        print(arg)
    get_file_line_num(sys.argv[1])