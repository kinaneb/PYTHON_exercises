#!/usr/bin/env python 3

from random import randint
from time import clock
import matplotlib.pyplot as plt

##############################################################
#
# Tri à bulles naïf
#

def triBullesNaif(T) :
  for i in range(len(T)-1,0,-1) :
    for j in range(i) :
      if T[j]>T[j+1]:
        T[j],T[j+1]=T[j+1],T[j]
  return T

##############################################################
#
# Tri à bulles tronqué (cf TD 3, ex.4)
#

def triBullesTronque(T) :
  a=True
  for i in range(len(T)-1,0,-1) :
    for j in range(i) :
      if T[j]>T[j+1]:
           a=False 
           T[j],T[j+1]=T[j+1],T[j]
    if a==True:
      break   
  return T

##############################################################
#
# Tri shaker (cf TD 3, ex.4)
#

def triShaker(T) :
  d=len(T)-1
  g = 0
  while g<d: 
    tri = True
    for j in range(g,d,1) :
      if T[j]>T[j+1]:
           T[j],T[j+1]=T[j+1],T[j]
           tri = False
    if tri==True:
      return T

    tri = True
    for j in range(d-1,g,-1):
      if T[j]<T[j-1]:
        T[j],T[j-1]=T[j-1],T[j]
        tri = False

    if tri==True:
      return T

    g+=1
    d-=1

  return T

##############################################################
#
# Tri par sélection
#

def triSelection(T) :
  for i in range(len(T)-1):
    idxMin = i
    for j in range(i+1,len(T)):
      if(T[j] < T[idxMin]):
        idxMin = j
    if(idxMin != i):
      T[i],T[idxMin] = T[idxMin],T[i]
  return T

##############################################################
#
# Tri par insertion "normal", 
# ie en insérant l'élément par échanges successifs
#

def triInsertionParEchangesSuccessifs(T) :
  for i in range(1, len(T)) :
    for j in range(i, 0, -1) :
      if T[j-1] > T[j] :
        T[j-1], T[j] = T[j], T[j-1]
      else : break
  return T

##############################################################
#
# Tri par insertion "par rotation" : en déplaçant les éléments d'un cran
# vers la droite avant de placer le nouvel élément dans la case libérée
#

def triInsertionRotation(T) :
  for i in range(1,len(T)):
     j=i-1
     temp=T[i]
     while (T[j]>temp and j>=0):
        T[j+1]=T[j]
        j=j-1      
     T[j+1]=temp
  return T

##############################################################
#
# Tri par insertion logarithmique : en déterminant la place où l'élément
# doit être inséré grâce à une recherche dichotomique
#

def triInsertionLogarithmique(T) :
    # à remplir !
    return T

##############################################################
#
# Fusion (récursive)

def fusionRecursive(T1, T2) :
  if len (T1) ==0 : return T2
  elif len (T2) ==0 : return T1
  elif T1 [0]<T2[0] : return [T1[0]] + fusionRecursive (T1[1:],T2)
  else : return [T2[0]] + fusionRecursive (T1,T2[1:])

##############################################################
#
# Fusion (itérative)

def fusionIterative(T1, T2) :
  R = []
  while ((len(T1) > 0) and (len(T2) > 0)):
    if (T1[0] < T2[0]) :
      R.append(T1[0])
      T1.remove(T1[0])
    else :
      R.append(T2[0])
      T2.remove(T2[0])
  if (len(T1) == 0) :
    R += T2
  else :
    R += T1
  return R


##############################################################
#
# Tri par fusion récursive

def triFusionRecursive(T) :
  if len(T) <2 : return T
  else : 
    milieu = len (T)//2
    gauche=triFusionRecursive(T[:milieu])
    droite=triFusionRecursive(T[milieu:])
    return fusionRecursive(gauche,droite)

##############################################################
#
# Tri par fusion itérative

def triFusionIterative(T) :
  if len(T) <2 : return T
  else : 
    milieu = len (T)//2
    gauche=triFusionRecursive(T[:milieu])
    droite=triFusionRecursive(T[milieu:])
    return fusionIterative(gauche,droite)

##############################################################
#
# Tri rapide naïf

def partition(T) :
  pivot = T[0]
  gauche = [ elt for elt in T[1:] if elt <= pivot ]
  droite = [ elt for elt in T[1:] if elt > pivot ]
  return pivot, gauche, droite

def triRapideNaif(T) :
  if len(T) < 2 : return T
  pivot, gauche, droite = partition(T)
  return triRapideNaif(gauche) + [pivot] + triRapideNaif(droite)
 


##############################################################
#
# Tri rapide en place

def triRapideEnPlace(T) :
  if (len(T) > 1) :
    pivot = T[len(T)//2]
    gauche = 0
    droite = len(T) - 1
    while (gauche <= droite):
      while (T[gauche] < pivot):
        gauche += 1
      while (T[droite] > pivot):
        droite -= 1
      if (gauche >= droite):
        T[gauche],T[droite] = T[droite],T[gauche]
        gauche += 1
        droite -= 1
    triRapideEnPlace(T[:droite])
    triRapideEnPlace(T[gauche:])
  return T


##############################################################
#
# choix des meilleures versions

triInsertion = None
triFusion = None
triRapide = None


##############################################################
#
# Utilitaires
#

##############################################################
#
# Génération d'une permutation aléatoire de taille n
#

def randomPerm(n) :
    l = list(range(1, n + 1))
    for i in range(n) :
        r = randint(i, n - 1)
        if i != r :
            l[i], l[r] = l[r], l[i]
    return l

##############################################################
#
# Mesure du temps
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
#
# Tests
#

def prettyT(T):
  return str(T) if len(T)<20 else str(T[:20])[:-3]+"...]"

def dataTestTri() : 
  return [
  [[], []],
  [[2,1], [1,2]],
  [[3,1,2], [1,2,3]],
  [[3,1,2,4,5], [1,2,3,4,5]],
  [[1,4,7,3,6,2,5], [1,2,3,4,5,6,7]],
  [[9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9]]
  ]

def testTri(algo) :
  print('Test %s :' % algo.__name__)
  data = dataTestTri()
  score = 0
  ldata = len(data)
  for i, dt in enumerate(data):
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    T = dt[0]
    ref = dt[1]
    res = algo(T)
    if res == ref :
      score += 1
      print('ok')
    else :
      print('ÉCHEC')
      print('    entrée  : %s' % prettyT(T))
      print('    résultat obtenu  : %s' % res)
      print('    résultat attendu : %s' % ref)
  print('* Score : %d/%d\n' % (score, ldata))


##############################################################
#
# Main
#

if __name__ == '__main__':
  algos = [triSelection,triInsertionRotation,triInsertionParEchangesSuccessifs,triFusionRecursive,
  triBullesNaif,triShaker,triFusionIterative,triRapideNaif] # chaque case contient un algorithme de tri différent, à remplir !
  #algos=[triRapideEnPlace]
  for tri in algos :
    testTri(tri)
  taille = 200 # taille maximale des tableaux à trier, à modifier !
  pas = 25 # pas entre les tailles des tableaux à trier, à modifier !
  ech = 50 # taille de l'échantillon pris pour faire la moyenne, à modifier !
  tableaux = [[i, [randomPerm(i) for j in range(ech)]] for i in range(0, taille, pas)]
  courbes(algos, tableaux, styleLigne='-')
  affiche()
