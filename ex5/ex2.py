#!/usr/local/bin/python3

from random import randint
from time import clock
from matplotlib.pyplot import plot, show, legend
from ex1 import *

# Exercice 2.1
#
# À REMPLIR
#
# Construit une permutation de {1,2,...,n} aléatoire
#   selon la loi de probabilité uniforme
#
def randomPerm(n) :
  l = [i + 1 for i in range(n)]
  for i in range(n):
    r = randint(i, n -1 )
    if (i != r) : l[i], l[r] = l[r], l[i]
  return l


# Exercice 2.2
#
# À REMPLIR
#
# Renvoie une permutation et le nombre de comparaisons
#   et d'affectations effectuées par l'algorithme
#
def randomPermOps(n) :
  ops = 0
  l = [i + 1 for i in range(n)]
  for i in range(n):
    #ops += 1
    r = randint(i, n - 1)
    ops += 1
    if (i != r) :
      #ops += 2 
      l[i], l[r] = l[r], l[i]
  return l, ops


# Exercice 2.3
#
# À COMPLÉTER
#
# Prend en paramètre deux tableaux triés gauche et droite 
# et retourne une copie triée de gauche+droite ainsi que son nombre d'inversions
#

def fusionInv(gauche, droite) :	# écrite de manière itérative
  i = j = x = 0
  m, n = len(gauche), len(droite)
  res = []
  while i < m and j < n :
    if gauche[i] < droite[j] :
      res.append(gauche[i])
      i += 1
    else :
      res.append(droite[j])
      j += 1
      x += (m-i)
  return res + gauche[i:] + droite[j:], x

# Exercice 2.3
#
# À COMPLÉTER
#
# Prend en paramètre un tableau T et en retourne une copie triée ainsi
# que son nombre d' inversions
#

def triFusionInv(L) :
  if len(L) <= 1 : return L, 0
  m = len(L) // 2
  G, xg = triFusionInv(L[:m])
  D, xd = triFusionInv(L[m:])
  res ,r = fusionInv(G, D)
  return res, (r+xd+xg)


# Exercice 2.4
#
# À REMPLIR
#
# Prend en paramètre un tableau T
#   et réalise le tri par insertion de T
#
def triInsertion(T) :
  for i in range(1, len(T)) :
    for j in range(i, 0, -1) :
      if T[j-1] > T[j] :
        T[j-1], T[j] = T[j], T[j-1]
      else : break
  return T


# Exercice 2.5
#
# À REMPLIR
#
# Renvoie le tableau T trié (par insertion)
#   et le nombre d'échanges faits par l'algorithme
#
def triInsertionOps(T) :
  ops=0
  for i in range(1, len(T)) :
    for j in range(i, 0, -1) :
      if T[j-1] > T[j] :
        ops += 1
        T[j-1], T[j] = T[j], T[j-1]
      else : break
  return T, ops



##############################################################
#
# TESTS
#

def prettyT(T):
  return str(T) if len(T)<20 else str(T[:20])[:-3]+"...]"

##############################################################
#
# Tests des algos de tri
#

def est_triee(L):
  for i in range(len(L)-1):
    if L[i]>L[i+1]: return False
  return True

def test_triData():
  return [[],[1]] + [[i for i in range(n,0,-1)] for n in range(2,80,10)]

def test_tri(algo):
  print('Test %s:' % algo.__name__)
  score = 0
  data = test_triData()
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    L = algo(dt)
    if est_triee(L):
        score += 1
        print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s' % prettyT(dt))
      print('    renvoie : %s ' % (prettyT(L)))
  print('* Score : %d/%d\n' % (score, ldata))

##############################################################
#
# Tests des fonctions retournant liste, entier
#

data_testFonction = {}
def testFonctionOps(fonction) :
  print('Test %s :' % fonction.__name__)
  score = 0
  ldata = len(data_testFonction[fonction])
  for i, dt in enumerate(data_testFonction[fonction]):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[:-1]		# tous les elts sauf le dernier
    ref = dt[-1]	# dernier elt
    res = fonction(*T)	# ie fonction(T[0], T[1], ...)
    if res == ref :
      score += 1
      print('ok')
    else :
      print('ÉCHEC')
      print('    entrée  : %s' % prettyT(T))
      print('    résultat obtenu  : %s %d' % res)
      print('    résultat attendu : %s %d' % ref)
  print('* Score : %d/%d\n' % (score, ldata))

##############################################################
#
#
#

def myTest(fonction) :
  print('myTest %s :' % fonction.__name__)
  score = 0
  ldata = len(data_testFonction[fonction])
  for i, dt in enumerate(data_testFonction[fonction]):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    T = randomPerm(n)
    print("n : ", n ,"; random permitation :\n",T)
    r = estPerm(T)
    if r == dt[1] :
      score += 1
      print('ok')
    else :
      print('ÉCHEC')
  print('* Score : %d/%d\n' % (score, ldata))

##############################################################
#
#
#

def myTestOps(fonction) :
  print('myTest %s :' % fonction.__name__)
  score = 0
  ldata = len(data_testFonction[fonction])
  for i, dt in enumerate(data_testFonction[fonction]):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    T, ops1 = randomPermOps(n)
    r, ops2 = estPermOps(T)

    print("n : ", n ,"; random permitation :\n",T,"ops : ", (ops1+ops2))
    if r == dt[1] : #and dt[2] == ops1+ops2 but what the right number of operations
      score += 1
      print('ok')
    else :
      print('ÉCHEC')
  print('* Score : %d/%d\n' % (score, ldata))

##############################################################
#
#
#

def myfusionInvTest(fonction) :
  print('myfusionInvTest %s :' % fonction.__name__)
  score = 0
  ldata = len(data_testFonction[fonction])
  for i, dt in enumerate(data_testFonction[fonction]):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    Td = dt[0]
    Tg = dt[1]
    res1, res2 = fonction(Td,Tg)
    if res2 == dt[2][1] :
      score += 1
      print('ok\n',Tg, Td)
      print('res\n',res1, res2)
    else :
      print('ÉCHEC')
  print('* Score : %d/%d\n' % (score, ldata))


##############################################################
#
#
#

data_testFonction[randomPerm] = [
  [3,True],
  [5,True],
  [12,True],
  [7,True],
  [7,True],
  [7,True],
  [8,True]
  ]

data_testFonction[randomPermOps] = [
  [2,True],
  [5,True],
  [12,True],
  [7,True],
  [8,True]
  ]


data_testFonction[triFusionInv] = [
  [[1,2,4,3], ([1,2,3,4], 1)],
  [[1,3,2,4], ([1,2,3,4], 1)],
  [[4,3,2,1], ([1,2,3,4], 6)]
  ]

data_testFonction[fusionInv] = [
  [[1,3,5,7], [2,4,6,8], ([1,2,3,4,5,6,7,8], 6)],
  [[1,2,3,4], [5,6,7,8], ([1,2,3,4,5,6,7,8], 0)],
  [[3,4], [1,2], ([1,2,3,4], 4)],
  [[2,4,6], [1,3,5], ([1,2,3,4,5,6], 6)],
  [[1,3,7,8], [2,4,5,6], ([1,2,3,4,5,6,7,8], 9)],
  [[5,6,7,8], [1,2,3,4], ([1,2,3,4,5,6,7,8], 16)]
  ]

data_testFonction[triInsertionOps] = [
  [[9,6,3,8,1], ([1,3,6,8,9], 8)],
  [[10,7,1,4,7], ([1,4,7,7,10], 7)],
  [[1,9,5,6,4], ([1,4,5,6,9], 5)],
  [[1,5,7,10,9], ([1,5,7,9,10], 1)]
  ]

##############################################################
#
# Pour les courbes de temps
# 
# NE PAS MODIFIER
#

def mesure(algo, T) :
  debut = clock()
  algo(T)
  return clock() - debut

def mesureMoyenne(algo, tableaux) :
  return sum([ mesure(algo, t[:]) for t in tableaux ]) / len(tableaux)

couleurs = ['b', 'g', 'r', 'm', 'c', 'k', 'y', '#ff7f00', '.5', '#00ff7f', '#7f00ff', '#ff007f', '#7fff00', '#007fff' ]
marqueurs = ['o', '^', 's', '*', '+', 'd', 'x', '<', 'h', '>', '1', 'p', '2', 'H', '3', 'D', '4', 'v' ]

def courbes(algos, tableaux, styleLigne='-') :
  x = [ t[0] for t in tableaux ]
  for i, algo in enumerate(algos) :
    print('Mesures en cours pour %s...' % algo.__name__)
    y = [ mesureMoyenne(algo, t[1]) for t in tableaux ]
    plt.plot(x, y, color=couleurs[i%len(couleurs)], marker=marqueurs[i%len(marqueurs)], linestyle=styleLigne, label=algo.__name__)

def affiche() :
  plt.xlabel('taille du tableau')
  plt.ylabel('temps d\'execution')
  plt.legend(loc='upper left')
  plt.show()

##############################################################

if __name__ == '__main__':
  myTest(randomPerm)
  myTestOps(randomPermOps)
  testFonctionOps(fusionInv)
  testFonctionOps(triFusionInv)
  test_tri(triInsertion)
  testFonctionOps(triInsertionOps)
  #courbes()
  #affiche()

