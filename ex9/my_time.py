#my_time.py

import time
def sec_to_hms(sec):
    ''' retourne le temps correspondant en (h,m,s)'''
    h = sec // 3600 if (not (sec < 3600)) else 0
    m = (sec - h*3600)//60 if(not(sec - h*3600 < 60)) else 0
    s = sec - ((h*3600) + (m*60))
    return str(h) + ":" + str(m) + ":" + str(s)

def hms_to_sec(h, m, s):
    '''retourne le temps correspondant en seconde'''
    #h, m, s = int(hms.split(":")[0]), int(hms.split(":")[1]), int(hms.split(":")[2])
    return h*3600 + m *60 + s

def timenow():
    ''' utilise le module time pour donner l'heure sous la forme (h, m, s)'''
    n = int((time.time()))%(3600*24)
    return sec_to_hms(n)

if __name__== "__main__":
    while(True):
        print(timenow())
        time.sleep(5)

