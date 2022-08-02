#!/usr/local/bin/python3

############################################################
# Exercice 3.1
#

def polyDegreOk(P) :
  degre_plus_un = len(P)
  if degre_plus_un == 1 :
    return True
  if degre_plus_un % 2 != 0 :
    return False
  return True



############################################################
# Exercice 3.2
#
# Calcule la somme des deux polynômes
#


def polySomme(P, Q) :
  R = [0] * max(len(P), len(Q))
  for i in range(min(len(P), len(Q))) :
    R[i] = P[i] + Q[i]
  if i < len(P) :
    for x in range(i+1, len(P)) :
      R[x] = P[x]
  if i < len(Q) :
    for x in range(i+1, len(Q)) :
      R[x] = Q[x] 
  return R


def polyDiff(P, Q) :  # calcule P - Q
  R = [0] * max(len(P), len(Q))
  for i in range(min(len(P), len(Q))) :
    R[i] = P[i] + Q[i]
  if i < len(P) :
    for x in range(i+1, len(P)) :
      R[x] = P[x]
  if i < len(Q) :
    for x in range(i+1, len(Q)) :
      R[x] = -1*Q[x] 
  return R 


############################################################
# Exercice 3.3
#
# Calcule le produit de P avec x**k
# 

def polyProdMonome(P, k) :
  R = [0] * (k + len(P))
  for i in range(len(P)) :
    R[i+k] = P[i]
  return R



############################################################
# Exercice 3.4
#
# Calcule le produit de polynômes par l'algorithme de Karatsuba
#

def polyProdKara(P, Q) :
  R = [0] * (len(P) + len(Q))
  if (polyDegreOk(P) and polyDegreOk(Q)) : 
    if (len(P)==1 or len(Q)==1) :
      #print(R)
      return [P[0]*Q[0]]
    else:
      np = len(P)//2
      nq = len(Q)//2
      p0 = P[:np]
      p1 = P[np:]
      q0 = Q[:nq]
      q1 = Q[nq:]
      p0q0 = polyProdKara(p0,q0)
      p1q1 = polyProdKara(p1,q1)
      p0p1 = polySomme(p0,p1)
      q0q1 = polySomme(q0,q1)
      p01q01 = polyProdKara(p0p1,q0q1)
      p01q01_pq0 = polyDiff(p01q01,p0q0)
      plus_minus = polyDiff(p01q01_pq0,p1q1)
      plus_minus_2 = polyProdMonome(plus_minus,2)
      p1q1_4 = polyProdMonome(p1q1,4)
      R = polySomme(polySomme(p1q1_4,plus_minus_2),p0q0)
      return R
  else : 
    return [0]





############################################################
# Exercice 3.5
#
# Calcul des coûts
#


def polyProdKaraOps(P, Q) :
  # À remplir
  return [0],0



############################################################
# Exercice Bonus
#
# Calcule le produit de polynômes en rajoutant des 0
# pour appliquer Karatsuba
#
# La fonction de test compare le résultat obtenu avec la fonction
# polyProd de l'exercice 2.
#

def polyProdOk(P,Q):
  # À remplir
  return [0]


############################################################
# TESTS - NE PAS MODIFIER !!!
#

from tp3_ex1 import prettyPrint


def test_polyDegreOkData():
  return [[[1], True],
          [[1, 2, 3, 5], True],
          [[3,2], True],
          [[3,2,0], False],
          [[3,2,0,0], True],
          [[1,1,1,1,1,1,1,1,1], False]]


def test_polyDegreOk () :
  print('Test polyDegreOk:')
  score = 0
  data = test_polyDegreOkData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    P = dt[0]
    pretty = prettyPrint(P)
    ref = dt[1]
    res = polyDegreOk(P)
    res = polyDegreOk(P)
    if res == ref :
      score += 1
      print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s' % pretty)
      print('    calcule : %s' % str(res))
      print('    attendu : %s' % str(ref))
  print('* Score : %d/%d\n' % (score, ldata))



def test_polySommeData():
  return [[[0,1,1], [0,2], [0, 3, 1]],
          [[1, 2, 3], [1,0,1], [2, 2, 4]],
          [[0,0,0,3], [2,-1], [2, -1, 0, 3]], 
          [[1,1,1,1,1,1], [0,1], [1, 2, 1, 1, 1, 1]]]


def test_polySomme () :
  print('Test polySomme:')
  score = 0
  data = test_polySommeData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    P = dt[0]
    Q = dt[1]
    res = polySomme(P,Q)
    ref = dt[2]
    if res == ref :
        score += 1
        print('ok')
    else :
      pP = prettyPrint(P)
      pQ = prettyPrint(Q)
      pRes = prettyPrint(res)
      pRef = prettyPrint(ref)
      print('ECHEC')
      print('    P  : %s' % pP)
      print('    Q  : %s' % pQ)
      print('    calcule : %s' % pRes)
      print('    attendu : %s' % pRef)
  print('* Score : %d/%d\n' % (score, ldata))


  
def test_polyProdMonomeData():
  return [[[0,1,1], 4, [0, 0, 0, 0, 0, 1, 1]],
          [[1, 2, 3], 3, [0, 0, 0, 1, 2, 3]],
          [[0,0,0,3], 7, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]],
          [[1,1,1,1,1,1], 3, [0, 0, 0, 1, 1, 1, 1, 1, 1]]]

def test_polyProdMonome():
  print('Test polyProdMonome:')
  score = 0
  data = test_polyProdMonomeData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    P = dt[0]
    k= dt[1]
    res = polyProdMonome(P,k)
    ref = dt[2]
    if res == ref :
        score += 1
        print('ok')
    else :
      pP = prettyPrint(P)
      pRes = prettyPrint(res)
      pRef = prettyPrint(ref)
      print('ECHEC')
      print('    P  : %s' % pP)
      print('    k  : %d' % k)
      print('    calcule : %s' % pRes)
      print('    attendu : %s' % pRef)
  print('* Score : %d/%d\n' % (score, ldata))



  
def test_polyProdData() :
  return [[[0, 1, 1], [0, 2], [0, 0, 0, 0, 0], 5],
          [[1, 2, 3], [1, 0, 1], [0, 0, 0, 0, 0, 0], 6],
          [[1, 2, 3, 0], [1, 0, 1, 0], [1, 2, 4, 2, 3, 0, 0], 171],
          [[0, 0, 0, 3], [2, -1], [0, 0, 0, 0, 0, 0], 6],
          [[0, 0, 0, 3], [2, -1, 0, 0], [0, 0, 0, 6, -3, 0, 0], 171],
          [[1, 1, 1, 1, 1, 1], [0, 1], [0, 0, 0, 0, 0, 0, 0, 0], 8],
          [[0, 1], [0, 2], [0, 0, 2], 33],
          [[1, 2, 3, 1], [1, 1, 1, 1],[1, 3, 6, 7, 6, 4, 1], 171],
          [[1, 2, 3, 1], [2, -1, 2, 4], [2, 3, 6, 7, 13, 14, 4], 171],
          [[1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 2, 2, 2, 3, 4, 4, 4, 3, 2, 2, 2, 1], 669]]


from tp3_ex2 import polyProd as pp

def normPoly(P):
  d = len(P)
  while d > 1 and P[d-1] == 0:
    d -= 1
  return P[:d]

def polyEq(P,Q):
  return normPoly(P) == normPoly(Q)
  

def test_polyProd (algo) :
  print('Test %s:' % algo.__name__)
  score = 0
  data = test_polyProdData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    P = dt[0]
    Q = dt[1]
    R = dt[2]
    res = algo(P,Q)
    if polyEq(res,R) :
      score += 1
      print('ok')
    else :
      print('ECHEC')
      pP = prettyPrint(P)
      pQ = prettyPrint(Q)
      pR = prettyPrint(R)
      pRes = prettyPrint(res)
      print('    P : %s' % pP)
      print('    Q : %s' % pQ)
      print('    calcule : %s' % pRes)
      print('    attendu : %s' % pR)
  print('* Score : %d/%d\n' % (score, ldata))



def test_polyProdKaraOps () :
  print('Test polyProdKaraOps' )
  score = 0
  data = test_polyProdData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    P = dt[0]
    Q = dt[1]
    R = dt[2]
    OPS = dt[3]
    res,ops = polyProdKaraOps(P,Q)
    if polyEq(res,R) and ops >= OPS:
      score += 1
      print('ok')
    else :
      print('ECHEC')
      pP = prettyPrint(P)
      pQ = prettyPrint(Q)
      pR = prettyPrint(R)
      pRes = prettyPrint(res)
      print('    P : %s' % pP)
      print('    Q : %s' % pQ)
      print('    calcule : %s' % pRes)
      print('    opérations : %d' % ops)
      print('    attendu : %s (en au moins %d ops)' % (pR,OPS))
  print('* Score : %d/%d\n' % (score, ldata))



  
from tp3_ex2 import polyProd

def test_polyProdOk () :
  print('Test polyProdOk')
  score = 0
  data = test_polyProdData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    P = dt[0]
    Q = dt[1]
    R1 = polyProdOk(P,Q)
    R2 = polyProd(P,Q)
    if polyEq(R1,R2):
      score += 1
      print('ok')
    else :
      print('ECHEC')
      pP = prettyPrint(P)
      pQ = prettyPrint(Q)
      pR1 = prettyPrint(R1)
      pR2 = prettyPrint(R2)
      print('    P : %s' % pP)
      print('    Q : %s' % pQ)
      print('    polyProdOk : %s' % pR1)
      print('    polyProd : %s' % pR2)
  print('* Score : %d/%d\n' % (score, ldata))


  
if __name__ == '__main__':
  test_polyDegreOk()
  test_polyDegreOk()
  test_polySomme()
  test_polyProdMonome()
  test_polyProd(polyProdKara)
  test_polyProdKaraOps()
  test_polyProdOk()
