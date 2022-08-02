#!/usr/local/bin/python3

############################################################
# Exercice 1.1
#
# Calcule la valeur de P(x)
#

def polyEval(P, x) :
  T = 0
  for i in range(len(P)):
    T += P[i] * (x ** i)
  return T



############################################################
# Exercice 1.2
#
# Calcule la valeur de P(x) et compte le nombre d'opérations
#

def polyEvalOps(P, x) :
  T = 0
  nO = 0
  for i in range(len(P)):
    T += P[i] * (x ** i)
    nO += i + 2
  return T,nO



############################################################
# Exercice 1.3
#
# Algorithme calculant P(x) par évaluation de Hörner.
# À modifier pour compter le nombre d'opérations
#

def hornerOps(P, x) :
  res = 0
  nO = 0
  for coeff in P[::-1] : #parcours de P à  l'envers
    res = res * x + coeff
    nO += 2
  return res , nO

#
# Classe de complexité: O(2n)
#


############################################################
# Exercice 1.4
#
# Fonction comparant le coût de polyEval et horner :
#   renvoie 1 si horner effectue moins d'opérations
#      "    0  "   "       "    autant d'opétations
#      "   -1  "   "       "      plus d'opétations
#

def hornerIsBetter(P,x):
  p , a = polyEvalOps(P, x)
  y , b = hornerOps(P, x)
  if(a < b):
    return -1
  elif (a == b):
    return 0
  else :
    return 1
  # À remplir
  return 0




############################################################
# TESTS - NE PAS MODIFIER !!!
#

def prettyPrint(P):
  s=str(P[0])
  if(len(P))>0:
    for i,c in enumerate(P[1:]):
      s+=" + " + str(c)+"*X^"+str(i+1)
  return s  

def test_polyEvalData() :
  #   [P,x,res,opsEval,opsHorner]
  return [[[0,1,1],       2,  6,  9,  6],
          [[1,2,3],       1,  6,  9,  6],
          [[0,0,0,3],     2, 24, 14,  8],
          [[1,1,1,1,1,1], 2, 63, 27, 12]]


def test_polyEvalBase (algo,withOps=0) :
  print('Test %s:' % algo.__name__)
  score = 0
  data = test_polyEvalData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    P = dt[0]
    pretty = prettyPrint(P)
    x = dt[1]
    ref = dt[2]

    # Test seulement de l'évaluation
    if (withOps == 0 ):
      ev = algo(P,x)
      if ev == ref :
        score += 1
        print('ok')
      else :
        print('ECHEC')
        print('    entree  : %s, x=%d' % (pretty,x))
        print('    calcule : %d' % ev)
        print('    attendu : %d' % ref)
        
    # Test de l'évaluation et du coût
    elif (withOps == 1 or withOps == 2 ):
      refOps = dt[2+withOps]
      ev,ops = algo(P,x)
      if ev == ref and ops == refOps:
        score += 1
        print('ok')
      else :
        print('ECHEC')
        print('    entree  : %s,x=%d' % (pretty,x))
        print('    calcule : %d (en %d ops)' % (ev,ops))
        print('    attendu : %d (en %d ops)' % (ref,refOps))
    else:
      raise Exception("Mauvaise usage du test, withOps devrait être 0,1 ou 2")
  print('* Score : %d/%d\n' % (score, ldata))

  
def test_polyEval ():
  return test_polyEvalBase (polyEval)

def test_polyEvalOps ():
  return test_polyEvalBase (polyEvalOps,1)

def test_hornerOps ():
  return test_polyEvalBase (hornerOps,2)

def sign (a):
  if a==0: return 0
  else : return abs(a)//a

def test_compare():
  print('Test: hornerIsBetter')
  score = 0
  data = test_polyEvalData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    
    P = dt[0]
    pretty = prettyPrint(P)
    x = dt[1]
    ref = dt[2]
    opE = dt[3]
    opH = dt[4]
    res = hornerIsBetter(P,x)
    ref = sign(opE-opH)
    if res == ref:
        score += 1
        print('ok')
    else :
        print('ECHEC')
        print('    entree  : %s,x=%d' % (pretty,x))
        print('    calcule : %d' % res)
        print('    attendu : %d (Horner: %d | eval: %d) ' % (ref,opH,opE))
  print('* Score : %d/%d\n' % (score, ldata))

  

if __name__ == '__main__':
  test_polyEval()
  test_polyEvalOps()
  test_hornerOps()
  test_compare()
