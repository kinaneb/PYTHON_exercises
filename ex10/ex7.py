def csv():
    print("Enter the name of the file please" )
    fname = input()
    o_f = open(fname)
    for line in o_f:
        l = line.split(";")
        print(" e-mail: ", l[3])
    o_f.close()

if __name__=='__main__':
    csv()


