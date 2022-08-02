#!/usr/bin/env python3

# Pour les tests
import ex1

# Pour les fonctions mathematiques
import math

# Pour l'affichage des graphiques
from matplotlib.pyplot import plot, show

###############################################################################
# Exercice 2.1
#
# A REMPLIR
#
def produit_matrice_2_2 (M1, M2) :
    '''Effectue le produit de deux matrices 2x2'''
    res = [ [0, 0], [0, 0] ]
    res[0][0] = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]
    res[1][0] = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]
    res[0][1] = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]
    res[1][1] = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]
    return res

###############################################################################
# Exercice 2.2
#
# A REMPLIR 
#
def puissance_matrice_2_2 (M, n) :
  '''Calcule la matrice M a la puissance n par exponentiation rapide'''
  if n == 0 : return [ [1, 0], [0, 1] ] # A REMPLIR
  if n == 1 : return M
  tmp = puissance_matrice_2_2(M, n // 2)
  carre = produit_matrice_2_2(tmp, tmp)
  if n % 2 == 1 : return produit_matrice_2_2(M, carre)
  else : return carre
  return M # A REMPLIR

#
# NE PAS MODIFIER !!!
#
def fibo_4(n) :
  '''Calcule le n-eme terme de la suite de Fibonacci'''
  if n <= 0 : return 0
  if n <= 2 : return 1
  M = [ [1, 1], [1, 0] ]
  # A REMPLIR
  return M[0][0]

###############################################################################
# Exercice 2.3
#
# A REMPLIR
#
def produit_matrice_2_2_adds (M1, M2) :
  ''' produit_matrice_2_2 avec calcul du nombre d'additions'''
  nO = 0
  res = [ [0, 0], [0, 0] ]
  res[0][0] = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]
  nO += 1
  res[1][0] = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]
  nO += 1
  res[0][1] = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]
  nO += 1
  res[1][1] = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]
  nO += 1
  return res, nO #A REMPLIR

def puissance_matrice_2_2_adds (M, n) :
  '''puissance_matrice_2_2 avec calcul du nombre d'additions effectuees'''
  if n == 0 : return [ [1, 0], [0, 1] ], 0 # A REMPLIR 
  if n == 1 : return M, 0
  tmp, nO = puissance_matrice_2_2_adds(M, n // 2)
  carre , nO  = produit_matrice_2_2_adds(tmp, tmp)
  if n % 2 == 1 : return produit_matrice_2_2_adds(M, carre), 0
  else : return carre, nO
  return M, nO # A REMPLIR
  
def fibo_4_adds(n) :
  '''fibo_4 avec calcul du nombre d'additions'''
  if n <= 0 : return 0, 0 # A REMPLIR
  if n <= 2 : return 1, 0 # A REMPLIR
  M = [ [1, 1], [1, 0] ]
  # A REMPLIR
  return M[0][0], 0

###############################################################################
# Exercice 2.4
#
# A REMPLIR
#
def courbes_adds(n, pas=1) :
  ''' affiche les courbes des additions effectuees pour le calcul de Fn par les algos fibo_3 et fibo_4 '''
  ops = [[]] * 2
  col = tp2_ex1.colors()
  
  # A REMPLIR
  ops[0] = [ tp2_ex1.fibo_3_adds(i)[1] for i in range(0, n, pas) ]
  plot(range(0,n,pas), ops[0], col[2])
  show()

###############################################################################
# Exercice 2.5
#
# A REMPLIR
#
def produit_matrice_2_2_bits (M1, M2) :
  ''' produit_matrice_2_2 avec calcul du nombre d'operations elementaires'''
  res = [ [0, 0], [0, 0] ]
  nO = 0
  res = [ [0, 0], [0, 0] ]
  res[0][0] = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]
  nO += int(math.log(max(abs(M1[0][0] * M2[0][0]), abs(M1[0][1] * M2[1][0])), 2)) + 2
  res[1][0] = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]
  nO += int(math.log(max(abs(M1[1][0] * M2[0][0]), abs(M1[1][1] * M2[1][0])), 2)) + 2
  res[0][1] = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]
  nO += int(math.log(max(abs(M1[0][0] * M2[0][1]), abs(M1[0][1] * M2[1][1])), 2)) + 2
  res[1][1] = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]
  nO += int(math.log(max(abs(M1[1][0] * M2[0][1]), abs(M1[1][1] * M2[1][1])), 2)) + 2
  return res, nO

def puissance_matrice_2_2_bits (M, n) :
  '''puissance_matrice_2_2 avec calcul du nombre d'operations elementaires'''
  if n == 0 : return [ [1, 0], [0, 1] ], 0 # A REMPLIR
  if n == 1 : return M, 0
  tmp, nO = puissance_matrice_2_2_adds(M, n // 2)
  carre , nO  = produit_matrice_2_2_adds(tmp, tmp)
  if n % 2 == 1 : return produit_matrice_2_2_adds(M, carre), 0
  else : return carre, nO
  return M, 0 # A REMPLIR

def fibo_4_bits(n) :
  '''fibo_4 avec calcul du nombre d'operations elementaires'''
  if n <= 0 : return 0, 0 # A REMPLIR
  if n <= 2 : return 1, 0 # A REMPLIR
  M = [ [1, 1], [1, 0] ]
  # A REMPLIR
  return M[0][0], 0

###############################################################################
# Exercice 2.4
#
# A REMPLIR
#
def courbes_bits(n, pas=1) :
  ''' affiche les courbes des operations elementaires effectuees pour le calcul de Fn par les algos fibo_3 et fibo_4 '''
  ops = [[]] * 2
  col = tp2_ex1.colors()
  # A REMPLIR
  ops[0] = [ tp2_ex1.fibo_3_bits(i)[1] for i in range(0, n, pas) ]
  plot(range(0,n,pas), ops[0], col[2])
  show()

if __name__ == '__main__':
  tp2_ex1.test_fibo(fibo_4)
  courbes_adds(30,1)      
  courbes_bits(30,1)

