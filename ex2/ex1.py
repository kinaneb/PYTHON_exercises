#!/usr/bin/env python3

# Pour les fonctions mathematiques
import math

# Pour l'affichage des graphiques
from matplotlib.pyplot import plot, show

# NE PAS MODIFIER
# Calcule
#    le n-eme terme de la suite de Fibonacci
# par 3 méthodes
def fibo_1(n) :
  if n <= 0 : return 0
  if n <= 2 : return 1
  return fibo_1(n-1) + fibo_1(n-2)

def fibo_2(n) :
  if n <= 0 : return 0
  liste = [0, 1]
  for i in range(1, n) :
    liste.append(liste[i-1] + liste[i])
  return liste[n]

def fibo_3(n) :
  if n <= 0 : return 0
  previous, last = 0, 1
  for i in range(1, n) :
    previous, last = last, previous + last
  return last

###############################################################################
# Exercice 1.1
#
# A REMPLIR
# Calcule
#    le n-eme terme de la suite de Fibonacci et 
#    le nombre d'additions utilisees
def fibo_1_adds(n) :
  if n <= 0 : return 0, 0 # A REMPLIR
  if n <= 2 : return 1, 0 # A REMPLIR
  fb1, op1 = fibo_1_adds(n - 1)
  fb2, op2 = fibo_1_adds(n - 2)
  return fb1 + fb2, op1+op2+1 # A REMPLIR

def fibo_2_adds(n) :
  if n <= 0 : return 0, 0 # A REMPLIR
  i = 0
  liste = [0, 1]
  for i in range(1, n) :
    liste.append(liste[i - 1] + liste[i])
    i +=1
  return liste[n], 0 # A REMPLIR

def fibo_3_adds(n) :
  if n <= 0 : return 0, 0 # A REMPLIR
  i = 0
  previous, last = 0, 1
  for i in range(1, n) :
    previous, last = last, previous + last
    i += 1
  return last, i # A REMPLIR

#
# LIRE, NE PAS MODIFIER
#
def colors() :
  return ['ro', 'co', 'go', 'bo']
def courbes_adds(n, alg, pas=1) :
  ''' affiche les courbes des additions effectuees pour le calcul de Fn par les différents algos '''
  if alg <= 0 or alg >= 4 :
    return
  ops = [[]] * alg
  
  if alg >= 3:
    ops[2] = [ fibo_3_adds(i)[1] for i in range(0, n, pas) ]
  if alg >= 2:
    ops[1] = [ fibo_2_adds(i)[1] for i in range(0, n, pas) ]
  if alg >= 1:
    ops[0] = [ fibo_1_adds(i)[1] for i in range(0, n, pas) ]

  col = colors()
  for i in range(0,alg) :
    plot(range(0,n,pas), ops[i], col[i])
  show()


###############################################################################
# Exercice 1.3  
# A REMPLIR
def nbOfBits(i) :
  return int(math.log(i, 2)) + 1 # A REMPLIR

###############################################################################
# Exercice 1.4
# A REMPLIR
def fibo_1_bits(n) :
  if n <= 0 : return 0, 0 # A REMPLIR                      
  if n <= 2 : return 1, 0 # A REMPLIR
  fb1, op1 = fibo_1_bits(n - 1)
  fb2, op2 = fibo_1_bits(n - 2)
  return fb1 + fb2, op2+nbOfBits(fb1)+1 # A REMPLIR

def fibo_2_bits(n) :
  if n <= 0 : return 0, 0 # A REMPLIR
  liste = [0, 1]
  nO=0
  for i in range(1, n) :
    liste.append(liste[i - 1] + liste[i])
    nO += nbOfBits(liste[i])+1
  return liste[n], nO # A REMPLIR

def fibo_3_bits(n) :
  if n <= 0 : return 0, 0 # A REMPLIR 
  previous, last = 0, 1
  nO = 0
  for i in range(1, n) :
    previous, last = last, previous + last
    nO += nbOfBits(last)+1
  return last, nO # A REMPLIR                                              

def courbes_bits(n, alg, pas=1) :
  ''' affiche les courbes des additions effectuees pour le calcul de Fn par les  différents algos '''
  if alg <= 0 or alg >= 4 :
    return
  ops = [[]] * alg

  if alg >= 3:
    ops[2] = [ fibo_3_bits(i)[1] for i in range(0, n, pas) ]
  if alg >= 2:
    ops[1] = [ fibo_2_bits(i)[1] for i in range(0, n, pas) ]
  if alg >= 1:
    ops[0] = [ fibo_1_bits(i)[1] for i in range(0, n, pas) ]

  col = colors()
  for i in range(0,alg) :
    plot(range(0,n,pas), ops[i], col[i])
  show()

  
#
# AJOUTER D'AUTRES DONNEES DE TEST
# [<valeur n>, <valeur F_n>]
def test_fiboData() :
  return [[-1, fibo_3(-1)],
          [2, fibo_3(2)],
          [4, fibo_3(4)],
          [8, fibo_3(8)],
          [16, fibo_3(16)]]
                    
#
# NE PAS MODIFIER
#
def test_fibo(algo):
  print('Test %s:' % algo.__name__)
  score = 0
  data = test_fiboData()
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    n = dt[0]
    refr = dt[1]
    fb = algo(n)
    if fb == refr :
      score += 1
      print('ok')
    else :
      print('ECHEC')
      print('    entree  : %s' % n)
      print('    calcule : %s' % fb)
      print('    attendu : %s' % refr)
  print('** Score %d/%d' % (score, ldata))


if __name__ == '__main__':
  test_fibo(fibo_1)
  test_fibo(fibo_2)
  test_fibo(fibo_3)
  courbes_adds(15, 3, 1)
  # Exercice 1.2: A REMPLIR avec d'autres appels à courbes_adds
  courbes_bits(15, 3, 1)
  # Exercice 1.5: A CODER courbes_ops
