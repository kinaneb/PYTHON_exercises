import time
############################ 
#ex 4
#############################

# ex 4.2 ##################
# try: Z==None
# ... except NameError: False
# ...
# False

# ex 4.3 ##################
#try: Z == ""
#... except NameError: False
#...
#False

# ex 4.4 ##################
#"Sans valeur" if(Z==None) else "Chaine vide" if(Z == "") else "Autre"
#'Chaine vide' @@ more developed @@
#try: "Sans valeur" if(Z==None) else "Chaine vide" if(Z == "") else "Autre"
#... except NameError: "Autre"
#...
#'Chaine vide'


############################ 
# ex 5 #
#############################

## ex 5.1 ###################
#s = sum([i for i in range(x+1)])

## ex 5.2 ##################
#l = [i for i in range(10)] start=Non=0, last=(sum(start + i.step)<end=10, step=Non=1
#print(l)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#l = [i for i in range(3, 40, 5)] start=3, last=(sum(start + i.step)<end, step=5
#print(l)
#[3, 8, 13, 18, 23, 28, 33, 38]

## ex 5.3 ##################
def somme_bete(x):
    """creat a list of [0-x] and return it's sum"""
    return sum([i for i in range(x+1)])

def somme_rapide(x):
    """return the result of x(x+1)/2"""
    return x(x+1)/2

## ex 5.4 ##################
#from tp1 import somme_bete 
#somme_bete(10)
#55


############################ 
# ex 6 #
#############################

## ex 6.1 #################
def sans_e(str):
    """remove 'e' from the string"""
    i = 0
    while (i<len(str)):
        if (str[i] =='e'):
            str = str[:i] + str[(i+1):]
        else: 
            i += 1
    return str

## ex 6.2 #################
def compt_espace(str):
    """count the space occurences in the string"""
    i = 0
    for e in str:
        if e ==' ':
            i += 1
    return i

## ex 6.3 #################
def palindrome(str):
    """check if the string is a palindrome"""
    m = len(str)//2
    for i in range(m):
        if(not (str[i] == str[len(str)-1-i])): return False
    return True

## ex 6.4 #################
def prefixe(str1, str2):
    """check if str1 is a prefix of str2"""
    if(len(str1) <= len(str2)):
        for i in range(len(str1)):
            if(not(str1[i] == str2[i])): return False
        return True
    return False

## ex 6.5 #################
def facture(str1, str2):
    """check if str1 is a factur of str2"""
    if(len(str1) <= len(str2)):
        for i in range(len(str2)):
            if (str2[i] == str1[0]) and (len(str1) <= len(str2[i:])):
                b = True
                for j in range(len(str1)):
                    if (not(str2[i+j] == str1[j])):
                        b = False
                        j = len(str1)
                if b : return b
    return False


## ex 6.6 #################
def sub(str1, str2):
    """check if str1 is a sous chaine of str2"""
    if(len(str1) <= len(str2)):
        j = 0
        for e in str1:
            i = 0
            while (i < len(str2)):
                if (str2[i] == e):
                    j += 1
                    str2 = str2[:i] + str2[i+1:]
                    i = len(str2)
                else: i +=1
        if j == len(str1): return True
    return False

## ex 6.7 #################
def perm(str1, str2):
    """check if str1 is a permutaion of str2"""
    if(len(str1)==len(str2)):
        return sub(str1, str2)
    return False

############################ 
# ex 7 #
#############################


## ex 7.1 #################
def sec_to_hms(n):
    """convert n seconds to h:m:s"""
    h = n // 3600 if (not (n < 3600)) else 0
    m = (n - h*3600)//60 if(not(n - h*3600 < 60)) else 0
    s = n - ((h*3600) + (m*60))
    return str(h) + ":" + str(m) + ":" + str(s)


## ex 7.2 #################
def hms_to_sec(hms):
    """convert h:m:s to n seconds"""
    h, m, s = int(hms.split(":")[0]), int(hms.split(":")[1]), int(hms.split(":")[2])
    return h*3600 + m *60 + s


## ex 7.3 #################
def timenow():
    """return computer time as h:m:s"""
    n = int((time.time()))%(3600*24)
    return sec_to_hms(n)


