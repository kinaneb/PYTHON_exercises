#!/usr/bin/env python3

from e8 import *

#
# A COMPLETER !
#
def estVide(arbre) :
  ''' teste si l'arbre est vide '''
  if ((len(arbre) == 0) or (arbre == [[None, None, None, None]])):
    return True
  return False
  
#
# Est Valide Arbre, INdice!
#
def estValide(arbre, i):
  if(i < len(arbre)):
    #("indice dépasse le taille de l'arbre")
    return True
  return False

#
# A COMPLETER !
#
def etiquette(arbre, i) :
  ''' retourne l'etiquette (ou None) '''
  if(estValide(arbre, i)):
    return arbre[i][0]
  return None
  
#
# A COMPLETER !
#
def filsGauche(arbre, i) :
  ''' retourne l'indice du fils gauche (ou None) '''
  if(estValide(arbre, i)):
    return arbre[i][1]
  return None
  
#
# A COMPLETER !
#
def filsDroit(arbre, i) :
  ''' retourne l'indice du fils droit (ou None) '''
  if(estValide(arbre, i)):
    return arbre[i][2]
  return None
  
#
# A COMPLETER !
#
def pere(arbre, i) :
  ''' retourne l'indice du pere (ou None) '''
  if(estValide(arbre, i)):
    return arbre[i][3]
  return None
  
#
# A COMPLETER !
#
def estRacine(arbre, i) :
  ''' teste si i est l'indice de la racine '''
  if(estValide(arbre, i)):
    if(pere(arbre, i) == None):
      return True
  return False
  
#
# A COMPLETER !
#
def estFilsGauche(arbre, i) :
  ''' teste si i est le fils gauche de son pere '''
  if(estValide(arbre, i)):
    if(estRacine(arbre, i) is False):
      if(filsGauche(arbre, pere(arbre, i)) == i):
        return True
  return False
  
#
# A COMPLETER !
#
def estFilsDroit(arbre, i) :
  ''' teste si i est le fils droit de son pere '''
  if(estValide(arbre, i)):
    if(estRacine(arbre, i) is False):
      if(filsDroit(arbre, pere(arbre, i)) == i):
        return True
  return False
  
#
# A COMPLETER !
#
def estFeuille(arbre, i) :
  ''' teste si i est l'indice d'une feuille '''
  if(filsGauche(arbre, i) is None):
    if(filsDroit(arbre, i) is None):
      return True
  return False


#
# A COMPLETER !
#

def testResults() :
  return [[estVide, (arbreVide, True), (arbreVideComplet, True)],
          [etiquette, (arbreVide, 1, None), (arbreFilGauche, 1, 'b')],
          [estFilsDroit,(arbreFilDroit,0, False), (arbreFilDroit,1, True), (arbreFilDroit,2, True)],
          [estFilsGauche,(arbreFilGauche,0, False), (arbreFilGauche,1, True), (arbreFilGauche,2, True)],
          [estFeuille, (arbreFeuille,0,True),(arbreFilGauche,0, False), (arbreFilGauche,1, False), (arbreFilGauche,2, True)]
	  ]


#
# NE PAS MODIFIER
#

def testAll() :
  tst = testResults()

  for fname, *tests in tst :
    score = 0
    print('Test %s :' % fname.__name__)
    for j, test in enumerate(tests) :
      *farg, fres = test
      print (' - test %d/%d : ' % (j + 1, len(tests)), end='')
      res = fname(*farg)
      if (res == fres) :
        print(' ok')
        score += 1
      else :
        print(" échec sur", *farg)
        print("\t résultat obtenu :", res, end='')
        print(" <> attendu :", fres)
    print ('  score %d/%d ' % (score, len(tests)))
	
    
if __name__ == '__main__':
  testAll()
  #print(testResults())
  #print(etiquette([['a', 1, 2, None], [None, None, None, 0], [None,
  #None, None, 0]],0))
  
