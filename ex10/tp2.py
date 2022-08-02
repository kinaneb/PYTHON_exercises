############################
## ex 1 #
#############################

## ex 1.1 ##################
def inversion(line):
    """reverse the line's words as list"""
    line = line.split(' ')
    return line[::-1]

## ex 1.2 ##################
def inversion_v2(line):
    """reverse the line's words as text line"""
    return " ".join(inversion(line))

## ex 1.3 ##################
def inclus(l1, l2):
    if(not (len(l1) > len(l2))):
        for e in l1:
            try:
                i = l2.index(e)
                l2 = l2[i+1:]
            except ValueError: return False
        return True
    return False


############################
## ex 2 #
#############################

## ex 2.1.a ################
def genlist_v1():
    return [ i for i in range(0, 200, 5)] # or 7

## ex 2.1.b ################
def genlist_v2(l):
    return [v for i, v in enumerate(l) if(i%2 ==0)]

## ex 2.1.c ################
def genlist_v3(l1, l2):
    return list(tuple(zip(l1, l2)))

## ex 2.2.a ##################
def diviseurs(n):
    l = [n//i for i in range(1, (n//2)+1) if(n%i == 0)]
    return [1]+l[::-1]

## ex 2.2.a ##################
def premiers(n):
    l = []
    for i in range(n+1):
        d = diviseurs(i)
        if(len(d) == 2):
            l.append(i)
    return l

############################
## ex 3 #
#############################

## ex 3.1 ##################
def sans_e(l):
    return [v for v in l if(v.find('e') == -1)]

## ex 3.2 ##################
def anti_begue(line):
    l = []
    line = line.split(' ')
    for i in range(len(line)-1):
        if (line[i] != line[i+1]):
            l.append(line[i])
    l.append(line[-1])
    return  " ".join(l)

############################
## ex 4 #
#############################

## ex 4.1 ##################
def prefixes(w, n):
    l = []
    if(n <= len(w)) and (n > 0):
        for i in range(1, n):
            l.append(w[:i])
    return l

## ex 4.1 ##################
# aux ###
def est_sans_se_prefixe_cube(w, p):
    lw, lp  = len(w), len(p)
    l=[]
    j = w.find(p)
    if (j > -1) and (lw >= 3*lp):
        l = [ w[i:i+lp] for i in range(j,(j+(3*lp)),lp) if (w[i:i+lp] == p) ]
        if len(l) == 3: return True
    return False


def est_sans_prefixes_cube(w):
    n = len(w)//3



############################
## main #
#############################

if __name__ == '__main__':

    l = "I'am testing invesrion"
    print("test 1:", inversion_v2(l))
    print("test inclus: ", inclus([0,1,2,3,4,5], [0,2,1,2,3,7,4,2,1,5]))
    print("test 2.1.a: ", genlist_v1())
    print("test 2.1.b: ", genlist_v2(["a","b","c","d","e"]))
    print("test 2.1.c: ", genlist_v3(["a","b","c"], [1,2,3]))
    print("test 2.2.a: ", diviseurs(40))
    print("test 2.2.b: ", premiers(37))
    print("test 3.1: ", sans_e(["", " ", "abc", "eabc", "abec", "abce"]))
    print("test 3.2: ", anti_begue("ceci ceci est un un test test"))
    print("test 4.1: ", prefixes("testing", 4))
    print("test 4.2: ", est_sans_se_prefixe_cube("aaaaaaaa","aa"))
