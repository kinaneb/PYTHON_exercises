#!/usr/bin/env python3

from ex1 import *

#
# A COMPLETER !
#
def profondeur(arbre, i) :
  ''' retourne la profondeur de i dans l'arbre '''
  p = 0
  if(estValide(arbre, i)):
    if(etiquette(arbre, i) == None):
      i = pere(arbre, i)
    while (pere(arbre, i) != None):
      p += 1
      i = pere(arbre, i)
  return p
  
#
# NE PAS MODIFIER !
#
def hauteurNaive(arbre) :
  ''' retourne la hauteur de l'arbre '''
  if estVide(arbre) : return 0
  return max (profondeur(arbre, i) for i in range(len(arbre)) 
      if etiquette(arbre, i) != None)


#
# HAUTEUR AUX !
#
def hauteurAux(arbre, i) :
  if(estFeuille(arbre,i)):
    return 0
  d = hauteurAux(arbre, filsDroit(arbre, i)) + 1
  g = hauteurAux(arbre, filsGauche(arbre, i)) + 1
  return max(d,g)
  

#
# A COMPLETER !
#
def racineIndice(arbre):
  for i in range(len(arbre)):
    if(estRacine(arbre, i)):
      return i
  


#
# A COMPLETER !
#
def hauteur(arbre) :
  ''' retourne la hauteur de l'arbre '''
  return hauteurAux(arbre,racineIndice(arbre))
  
  
#
# A COMPLETER !
#

def parcoursPrefixe(arbre) :
  ''' retourne la liste des etiquettes en ordre prefixe '''
  i = racineIndice(arbre)
  res = []
  while(estFeuille(arbre, i) is False):
    if (etiquette(arbre, i) is not None):
      res += etiquette(arbre, i)
    i = filsGauche(arbre, i)
    if(estFeuille(arbre, i)):
      print("$")
        #i = filsDroit(arbre, pere(arbre,i))
  return res

        
#
# A COMPLETER !
#
def estUnABR(arbre) :
  ''' teste si arbre est un ABR '''
  return False


#
# A COMPLETER !
#

def testResults() :
  return [
  [profondeur, (arbreABR,0,2), (arbreABR,3,1), (arbreABR,5,0), (arbreABR,8,2)],
  [hauteur
  , (arbreABR,hauteurNaive(arbreABR))
  , (arbreNABR,hauteurNaive(arbreNABR))
  , (arbreFeuilleComplet,hauteurNaive(arbreFeuilleComplet))
  , (arbreFeuille,hauteurNaive(arbreFeuille))
  , (arbreVideComplet,hauteurNaive(arbreVideComplet))
  , (arbreFilGauche,hauteurNaive(arbreFilGauche))
  , (arbreFilDroit,hauteurNaive(arbreFilDroit))
  , (arbreParfait,hauteurNaive(arbreParfait))
  , (arbrePlanetes,hauteurNaive(arbrePlanetes))
  , (arbrePlanetesComplet,hauteurNaive(arbrePlanetesComplet))
  , (arbreFilsGaucheComplet,hauteurNaive(arbreFilsGaucheComplet))]
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


  