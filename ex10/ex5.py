
def find_lines_in_file():
    print(" entre file name please: ")
    fname = input()
    print("inter the word that you want to find pleas: ")
    w = input()
    f = open(fname, 'r')
    for line in f:
        if line.find(w) > -1 :
            print(line)

if __name__ == '__main__':
    find_lines_in_file()


