#!/usr/local/bin/python3

# Pour l'affichage des graphiques
from matplotlib.pyplot import plot, show

############################################################
# Exercice 3.1
#
# Fusion de deux listes - Pensez aux tests !
#

def fusion(L1,L2):
  R = []
  while ((len(L1) > 0) and (len(L2) > 0)):
    if (L1[0] < L2[0]) :
      R.append(L1[0])
      L1.remove(L1[0])
    else :
      R.append(L2[0])
      L2.remove(L2[0])
  if (len(L1) == 0) :
    R += L2
  else :
    R += L1
  return R

############################################################
# Exercice 3.2
#
# Tri Fusion 
#

def triFusion(L):
  if len(L) < 2 :
      return L  
  else:
      n = len(L)//2
      L1 = triFusion(L[:n])
      L2 = triFusion(L[n:])
      return fusion(L1,L2)


############################################################
# Exercice 3.3
#
# Programme de test pour algorithme triant des listes
#
def test_triData() :
  return [[[10,3,2,7,5],[2,3,5,7,10]],
          [[16,2,1,4,3,2,3,6],[1,2,2,3,3,4,6,16]],
          [[],[]],
          [[4,8,37,49,0,5,4],[0,4,4,5,8,37,49]],
          [[38,14,21],[14,21,38]],
          [[23,7,48,0],[0,7,23,48]]]

def test_tri(algo) :
  print('Test %s:' % algo.__name__)
  score = 0
  data = test_triData()
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    refr = dt[1]
    tri = algo(n)
    if tri == refr :
      score += 1
      print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s' % n)
      print('    calcule : %s' % tri)
      print('    attendu : %s' % refr)
  print('** Score %d/%d' % (score, ldata))

############################################################
# Exercice 3.3
#
# bubble Sort
#

def bubbleSort(L):
  for i in range(len(L)-1,0,-1):
      for x in range(i):
          if L[x]>L[x+1]:
            L[x], L[x + 1] = L[x + 1], L[x]
  return L

############################################################
# Exercice 3.4
#
# Indice du minimum d'une liste - (pensez aux test!)
#

def idxMin(L) :
  minL = L[0]
  indxML = 0
  for i in range(len(L)) :
    if (L[i] <= minL):
      minL = L[i]
      indxML = i
  return indxML

############################################################
# Exercice 3.5
#
# Tri sélection
#

def triSelection(L) :
  for i in range(len(L) - 1):
    L[i],L[idxMin(L[i:]) + i] = L[idxMin(L[i:]) +i ],L[i]
  return L



############################################################
# Exercice 3.6
#
# Fonctions de tri comptant le nombre d'opérations
#

def triFusionOps(L) :
  # À remplir
  return L,0

def triSelectionOps(L) :
  # À remplir
  return L,0

############################################################
# Exercice 3.7
#
# Affiche les courbes d'efficacité des tris passés en arguments
#  pour des tests sur listes de longueurs 1 à n

def colors() :
  return ['ro', 'co', 'go', 'bo']


def courbesTri(A,n) :
  listes = [[]]*n
  # À compléter
  ops = [[]]*len(A)
  # plot(...)
  # show(...)

    

############################################################
#
# Main
#

if __name__ == '__main__':
  test_tri(triFusion)
  test_tri(triSelection)
  test_tri(bubbleSort)

