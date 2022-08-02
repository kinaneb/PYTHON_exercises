#!/usr/local/bin/python3

############################################################
# Exercice 1.1
#
# Calcule le nombre d'elements de T egaux à x
#
def occurrence(T, x) :
  res = 0
  for i in range(len(T)):
    if (T[i] == x):
      res += 1;
  return res



############################################################
# Exercice 1.2
#
# Compte les occurrences des nombres de 0..m-1 en T
#    en utilisant la fonction occurence
#

def compteNaif(T, m) :
  res = [0] * m
  for i in range(m):
    res[i] = occurrence(T,i)
  return res



############################################################
# Exercice 1.3
#
# Compte les occurrences des nombres de 0..m-1 en T
#    et le nombre d'operations
#

def compteNaifOps(T, m) :
  res = [0] * m
  ops = 0
  for i in range(m):
    res[i] = occurrence(T,i)
    ops += len(T)
  return res, ops



############################################################
# Exercice 1.4
#
# Compte les occurrences des nombres de 0..m-1 en T
#    en temps lineaire
#

def compteOptimal(T, m) :
  res = [0] * m
  for x in T:
    if (x < m):  
      res[x] = res[x]+1
  # À remplir
  return res

############################################################
# Exercice 1.5
#
# Compte les occurrences des nombres de 0..m-1 en T
#    en temps lineaire
#    et le nombre d'opérations
#


def compteOptimalOps(T, m) :
  res = [0] * m
  op = 0
  for x in T:
    op += 1
    if (x < m):
      res[x] += 1
# À remplir
  return res, op+ 0






############################################################
# TESTS 
#

def prettyT(T):
  return str(T) if len(T)<20 else str(T[:20])[:-3]+"...]"


############################################################
#
# Tests : occurence
#


def test_occurrenceData() :
  return [[[4,3,1], 2, 0],
          [[1,2,3,1,2,3,1,2,3], 2, 3],
          [[2] * 1000000, 2, 1000000],
          [[3] * 10000000, 2, 0]]


def test_occurrence () :
  print('Test occurrence:')
  score = 0
  data = test_occurrenceData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res = occurrence(T,x)
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
# Tests : compteNaif
#

def test_compteNaifData():
  return [[[4,3,1], 2, [0,1]],
          [[1,2,3,1,2,3,1,2,3], 3, [0,3,3]],
          [[2] * 1000000, 3, [0,0,1000000]],
          [[3] * 10000000, 2, [0,0]]]


def test_compteNaif () :
  print('Test compte:')
  score = 0
  data = test_compteNaifData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res = compteNaif(T,x)
    if res == ref :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    compte  : %s' % str(res))
      print('    attendu : %s' % str(ref))
  print('* Score : %d/%d\n' % (score, ldata))


############################################################
#
# Tests : compteOps
#


def test_compteNaifOpsData():  
  return [[[4,3,1], 2, [0,1], 6],
          [[1,2,3,1,2,3,1,2,3], 3, [0,3,3], 27],
          [[2] * 1000000, 3, [0,0,1000000], 1000000*3],
          [[3] * 10000000, 2, [0,0], 10000000*2]]




def test_compteNaifOps () :
  print('Test compteNaifOps:')
  score = 0
  data = test_compteNaifOpsData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    refOps = dt[3]
    res,ops = compteNaifOps(T,x)
    if res == ref  and refOps <= ops:
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    compte  : %s (en %d ops)' % (str(res),ops))
      print('    attendu : %s (en au moins %d ops)' % (str(ref),refOps))
  print('* Score : %d/%d\n' % (score, ldata))


    
############################################################
#
# Tests : compteOptimal
#

def test_compteOptimalData():
  return test_compteNaifData()
    

def test_compteOptimal () :
  print('Test compteOptimal:')
  score = 0
  data = test_compteOptimalData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    res = compteOptimal(T,x)
    if res == ref :
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s x=%d' % (prettyT(T),x))
      print('    compte  : %s' % str(res))
      print('    attendu : %s' % str(ref))
  print('* Score : %d/%d\n' % (score, ldata))


############################################################
#
# Tests : compteOptimalOps
#


def test_compteOptimalOpsData():  
  return [[[4,3,1], 2, [0,1], 3],
          [[1,2,3,1,2,3,1,2,3], 3, [0,3,3], 9],
          [[2] * 1000000, 3, [0,0,1000000], 1000000],
          [[3] * 10000000, 2, [0,0], 10000000]]



def test_compteOptimalOps () :
  print('Test compteOptimalOps:')
  score = 0
  data = test_compteOptimalOpsData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    x = dt[1]
    ref = dt[2]
    refOps = dt[3]
    res,ops = compteOptimalOps(T,x)
    if res == ref  and refOps <= ops:
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s, x=%d' % (prettyT(T),x))
      print('    compte  : %s (en %d ops)' % (str(res),ops))
      print('    attendu : %s (en au moins %d ops)' % (str(ref),refOps))
  print('* Score : %d/%d\n' % (score, ldata))
  


if __name__ == '__main__':
  test_occurrence()
  test_compteNaif()
  test_compteNaifOps()
  test_compteOptimal()
  test_compteOptimalOps()

