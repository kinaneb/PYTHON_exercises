#!/usr/local/bin/python3

#
# NB: T est toujours considéré trié !
#

############################################################
# Exercice 2.1
#
# Effectue une recherche dichotomique de x dans T
#

def trouve(T, x):
  if (len(T) == 0):
    return False
  l = len(T)//2
  if (x == T[l]):
    return True
  elif (x < T[l]):
    return trouve(T[:l],x)
  else: return trouve(T[l+1:],x) 



############################################################
# Exercice 2.2
#
# Effectue une recherche dichotomique de x dans T
# et le nombre de comparaisons effectees

def trouveOps(T,x):
  if (len(T) == 0):
    return False, 1
  l = len(T)//2
  if (x == T[l]):
    return True , 2
  elif (x < T[l]):
    op = 3
    op += trouveOps(T[:l],x)[1]
    return trouveOps(T[:l],x),op
  else: 
    op = 3
    op += trouveOps(T[:l],x)[1]
    return trouveOps(T[l+1:],x)



############################################################
# Exercice 2.3
#
# Renvoie l'indice de la première occurrence de x dans T
# et False si il n'y en a aucune   
#

def trouvePremier(T, x,debut=0) :
  if len(T)== 0 : return False
  n=len(T)//2
  debut+= n
  if x==T[n]: 
    if not trouve(T[:n], x) :
      return debut
    else : 
      return trouvePremier(T[:n], x)
  elif x< T[n]:
    if not trouve(T[:n], x) :
      return debut
    else :
      return trouvePremier(T[:n], x)
  else :
    if not trouve(T[:n], x) :
      return debut
    else :
      return trouvePremier(T[n+1:],x,debut)



############################################################
# Exercice 2.4
#
# Renvoie l'indice de la première occurrence de x dans T
# et False si il n'y en a aucune
# ainsi que le nombre de comparaisons nécessaires
#
  

def trouvePremierOps(T, x, debut=0) :
  if len(T)== 0 : return False,0
  n=len(T)//2
  debut+= n
  if x==T[n]:
    ops=1+trouveOps(T[:n], x) [1]
    if not trouve(T[:n], x) :
      return debut,ops
    else : 
      ops+=trouvePremierOps(T[:n], x)[1]
      return trouvePremierOps(T[:n], x)
  elif x< T[n]:
    ops=3+trouveOps(T[:n], x) [1]
    if not trouve(T[:n], x) :
      return debut,ops
    else :
      ops+=trouvePremierOps(T[:n], x)[1]
      return trouvePremierOps(T[:n], x)[0],ops
  else :
    ops=3+trouveOps(T[:n], x) [1]
    if not trouve(T[:n], x) :
      return debut,ops
    else :
      ops+=trouvePremierOps(T[n+1:],x,debut)[1]
      return trouvePremierOps(T[n+1:],x,debut)[0], ops




############################################################
# Exercice 2.5
#
# Compte les occurrences de x dans T par recherche dichotomique
#


def occurenceDichotomie(T, x) :
  # A REMPLIR !!
  return 0

############################################################
# Exercice 2.5
#
# Compte les occurrences de x dans T par recherche dichotomique
#     et le nombre d'opérations
#

def occurenceDichotomieOps(T, x) :
  # A REMPLIR !!
  return 0,0



############################################################
# TESTS - À COMPLETER 
#

def prettyT(T):
  return str(T) if len(T)<20 else str(T[:20])[:-3]+"...]"


############################################################
#
# Tests :
#


def test_trouveData() :
  return [[[1,2,3,4], 2, True],
          [[1,2,4,5] , 3, False]]



def test_trouve () :
  print('Test trouve:')
  score = 0
  data = test_trouveData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res = trouve(T,x)
    if res == ref :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    compte  : %d' % res)
      print('    attendu : %d' % ref)
  print('* Score : %d/%d\n' % (score, ldata))


############################################################
#
# Tests : trouveOps
#


def test_trouveOpsData():  
  return [[[1,2,3,4,5], 2, True, 5],
          [[1,2,2,4,5,7,10,11,11,12,14,14,15,15,20], 6, False, 13]]




def test_trouveOps () :
  print('Test trouveOps:')
  score = 0
  data = test_trouveOpsData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    refOps = dt[3]
    res,ops = trouveOps(T,x)
    if res == ref  and refOps <= ops:
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    trouve  : %s (en %d ops)' % (str(res),ops))
      print('    attendu : %s (en au moins %d ops)' % (str(ref),refOps))
  print('* Score : %d/%d\n' % (score, ldata))


    
############################################################
#
# Tests : trouvePremier
#

def test_trouvePremierData():
  return [[[1],1,0],
          [[1]+[2]*100000,1,0],
          [[1]+[2]*100000,2,1]]
    

def test_trouvePremier () :
  print('Test trouvePremier:')
  score = 0
  data = test_trouvePremierData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res = trouvePremier(T,x)
    if res == ref :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    trouve  : %s' % str(res))
      print('    attendu : %s' % str(ref))
  print('* Score : %d/%d\n' % (score, ldata))


from math import log,floor

def test_trouvePremierOps () :
  print('Test trouvePremierOps:')
  score = 0
  data = test_trouvePremierData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res,ops = trouvePremierOps(T,x)
    logLen = floor(log(max(len(T),2),2))
    if res == ref and (len(T)<2 or logLen<=ops<=6*(logLen+1)):
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    trouve  : %s (en %d ops)' % (str(ref),ops))
      if ops<logLen:
        print('    attendu : %s (en au moins %d ops)' % (str(ref),logLen))
      else :
        print('    attendu : %s (moins de %d ops)' % (str(ref),5*logLen))
  print('* Score : %d/%d\n' % (score, ldata))

  

if __name__ == '__main__':
  test_trouve()
  test_trouveOps()
  test_trouvePremier()
  test_trouvePremierOps()

