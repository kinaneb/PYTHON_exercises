#!/usr/local/bin/python3

############################################################
# Exercice 2.1
#
# Calcule le pôlynome PxQ
#

def polyProd(P, Q) :
  R = [0] * (len(P) + len(Q) - 1)
  if len(P) < len(Q) :
    for i in range(len(P),len(Q)) :
      P += [0]
  if len(Q) < len(P) :
    for i in range(len(Q),len(P)) :
      Q += [0]
  V = [0] * (len(P) + len(Q) - 1)
  for n in range(0, len(P)) :
    for x in range(0 , len(P)) :
      V[n+x] = V[n+x]+P[x]*Q[n]
  for c in range(len(R)) :
    R[c] = V[c]
  return R

############################################################
# TESTS - NE PAS MODIFIER !!!
#

from tp3_ex1 import prettyPrint

def polyEq(P,Q) :
  res = 1
  if len(P) != len(Q) :
    return 0;
  for i in range(len(P)) :
    if P[i] != Q[i] :
      return 0
  return 1


def test_polyProdData() :
  return [[[0,1,1], [0,2], [0,0,2,2]],
          [[1,2,3], [1,0,1], [1,2,4,2,3]],
          [[0,0,0,3], [2,-1], [0,0,0,6,-3]],
          [[1,1,1,1,1,1], [0,1], [0,1,1,1,1,1,1]],
          [[0,1], [0,2], [0,0,2]],
          [[1,2,3,1], [1,1,1,1], [1, 3, 6, 7, 6, 4, 1]],
          [[1,2,3,1], [2,-1,2,4], [2, 3, 6, 7, 13, 14, 4]],
          [[1,1,1,1,1,1,1,1], [0,0,1,1,0,0,1,1], [0, 0, 1, 2, 2, 2, 3, 4, 4, 4, 3, 2, 2, 2, 1]]]

  
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
    ok = polyEq(res,R)
    if ok :
      score += 1
      print('ok')
    else :
      pP = prettyPrint(P)
      pQ = prettyPrint(Q)
      pR = prettyPrint(R)
      pRes = prettyPrint(res)
      print('ECHEC')
      print('    P : %s' % pP)
      print('    Q : %s' % pQ)
      print('    calcule : %s' % pRes)
      print('    attendu : %s' % pR)
  print('* Score : %d/%d\n' % (score, ldata))

if __name__ == '__main__':
  test_polyProd(polyProd)

