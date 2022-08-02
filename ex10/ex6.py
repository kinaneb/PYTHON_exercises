def copy_without_e():
    print("Enter the name of the file please")
    fname = input()
    o_f = open(fname)
    n_f = open("no_e_"+fname, "w+")
    for line in o_f:
        l = line.split(" ")
        for i in range(len(l)):
            if(l[i].find("e") > -1):
                s = l[i].split("e")
                l[i] = "".join(s)
        n_f.write(" ".join(l))
    n_f.close()
    o_f.close()

if __name__ == '__main__':
    copy_without_e()
