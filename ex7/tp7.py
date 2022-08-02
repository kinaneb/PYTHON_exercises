#!/usr/local/bin/python3

from math import sqrt
from random import randint
from time import process_time
import matplotlib.pyplot as plt


#
# À COMPLETER
#
# Calcule la distance entre les points p1 et p2
#
def dist(p1,p2) :
  return 0


#
# À COMPLETER
#
# Renvoie la paire de points de la list L les plus proches
#

def minDistNaive(L) :
  return None

  
#
# À COMPLETER
#
# Test la fonction minDistNaive
#
def testMinDistNaive() :
  return False


#
# A COMPLETER
#
# Retourne une copie triée de la liste de points L, dans l'ordre croissant des abscisses
#
def sortX(L) :
  return None


#
# A COMPLETER
#
# Retourne une copie triée de la liste de points L, dans l'ordre croissant des ordonnées
#
def sortY(L) :
  return None


#
# À COMPLETER
#
# Renvoie une valeur x telle que la moitié de points du Lx 
# ont abscisse mineur ou égale a x, et l'autre moitié ont
# abscisse majeur de x.
#

def abscisseMediane(Lx, debut, fin) :
  return 0


#
# À COMPLETER
#
# Renvoie la liste de points de Ly dont l'abscisse diffère de x
# de moins de d
#

def bandeVerticale(Ly,x,d) :
  return None


######## NE PAS MODIFIER - DEBUT
#
#
# Entrées:
# - L : liste de points 
# - x_median : abscisse centrale de la bande
# - d : demi-largeur de la bande
# - p,q : le deux points les plus proches
#

def plotPoints(L, x_median, d, p, q) :
  plt.clf()
  plt.title("Nuage de points du plan")
  plt.xlabel('x')
  plt.ylabel('y')

  xL = [ x for (x,y) in L if x<= x_median ]
  yL = [ y for (x,y) in L if x<= x_median ]
  xR = [ x for (x,y) in L if x > x_median ]
  yR = [ y for (x,y) in L if x > x_median ]
  
  plt.plot(xL,yL,'bs', # left points
           xR,yR,'gs', # right points
           (x_median,x_median),(0,100),'y-', # point of split
           (x_median - d , x_median - d), (0,100),'r-', # 
           (x_median + d, x_median + d), (0,100),'r-',
           [p[0],q[0]],[p[1],q[1]],'mo-', linewidth=2)
  plt.draw()
  input("Press [enter] to continue.")

######## NE PAS MODIFIER - FIN

#
# À COMPLETER
#
# Renvoie le (un) couple de points de Lx[debut:fin] avec distance minimale.
#
# Entrée :
# - Lx : liste de points triée selon les absisses
# - Ly : liste des mêmes points, triée selon les ordonnées
# - debut : premier indice de la portion de Lx concernée
# - fin : premier indice après la portion de Lx concernée
# - plot: parametre optionnel permettant de faire (ou non) des
#     affichages
#
# Assumption: chaque point de Lx a une seule occurrence dans Lx
#
def minDistAux(Lx, Ly, debut, fin, plot=False) :
  return None

#
# À COMPLETER
#
# Renvoie le (un) couple de points de la liste L à distance minimale l'un
# de l'autre
#

def minDist(L, plot=False) :
  return None


##################################################################################
#
# NE PAS MODIFIER
#
##################################################################################

def errmessage(r,refr) :
  print('ECHEC ')
  print('   calcule : ', end='')
  print(r)
  print('   attendu : ', end='')
  print(refr)


def data() :
  L = []
  for i in range(5):
    points = []
    for j in range(50):
      points.append( (randint(0,100),randint(0,100)) )
    L.append(points)
  return L


def plotTimes(n = 1000, step = 50):
  print("Calcul de temps en cours...")
  opsN = []
  opsE = []
  steps = list(range(step, n, step))
  
  # gather the time taken by the two algos
  for i in steps :
    L = []
    for j in range(i): # generate a list of i points
      L.append((randint(0,100), randint(0,100)))

    t0 = process_time()
    minDistNaive(L)
    opsN.append(process_time() - t0)

    t0 = process_time()
    minDist(L)
    opsE.append(process_time() - t0)

  plt.close()
  plt.xlabel("taille de L")
  plt.ylabel("temps")
  plt.title("temps d'exécution de minDistNaive et minDist")
  plt.plot(steps, opsN, 'r^', steps, opsE, 'bo')
  plt.show()



if __name__ == '__main__':
  print('Et les tests, alors?')

  
  
