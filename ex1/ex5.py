#!/usr/bin/env python3

#
# A REMPLIR
#
# La valeur du tableau de chiffres et le nombre d'operations elementaires
#
def valeur(tab):
  n = 0
  op = 0
  for i in range (len(tab)):
        n+=tab[i]* 10**i
        op+=i+1
  return n, op

#
# A REMPLIR
#
# Le tableau des chiffres (poids faible en premier)
#
def tableau(entier) : 
  tab = []
  entier_len=str(entier)
    for i in range (len(entier_len)):
        tab.append(entier%10)
        entier=entier/10
  return [0] if len(tab) == 0 else tab

#
# A REMPLIR
#
# L'addition de deux tableaux de chiffres decimaux de taille egale
#
def addition(nb1, nb2) :
  "addition de deux entiers representes pas des tableaux de chiffres"
  res = []
  retenue = 0
  op = 0
  for (chiffre1, chiffre2) in zip(nb1, nb2) :
    tmp = chiffre1 + chiffre2 + retenue
    op += 2
    retenue = tmp//10 
    res.append(tmp%10)
    op += 3
  return res + [retenue] if retenue > 0 else res, op

#
# A REMPLIR
#
# L'addition de deux tableaux de chiffres decimaux de taille differente
#
def additionV(nb1, nb2) :
  #print (nb1)
  #print (nb2)
    res = []
    retenue = 0
    op = 0
    n_nb1=len(nb1)
    n_nb2=len(nb2)
    for (chiffre1, chiffre2) in zip(nb1, nb2) :
        tmp = chiffre1 + chiffre2 + retenue
        op += 2
        retenue = tmp//10 
        res.append(tmp%10)
        op += 3
    if n_nb2 != n_nb1 :
            op+=1
            if n_nb1<n_nb2 :
                op+=1
                for i in range(n_nb1,n_nb2) :
                    res.append(nb2[i])
                    op+=1
            else :
                op+=1
                for i in range(n_nb2,n_nb1) :
                    res.append(nb1[i])
                    op+=1

    return res + [retenue] if retenue > 0 else res, op
    return addition(nb1, nb2)
  
#
# A COMPLETER
#
# La multiplication de deux tableaux de chiffres decimaux
#
def multiplication1(nb1, nb2) :
  "multiplication de nb1, nb2 tableaux de chiffres par additions"
  res = nb1[:]  # copie du premier nombre
  vnb2, op = valeur(nb2)
  for i in range(1, vnb2) :
    res, tmp = additionV(res, nb1)
    # A COMPLETER
    op += 0
  return res, op

#
# A COMPLETER
#
# La multiplication de deux tableaux de chiffres decimaux
#
def multiplication_par_un_chiffre(nb1, chiffre2) :
  "multiplication de nb1 par chiffre2"
  res = []
  retenue = 0
  op = 0
  for chiffre1 in nb1 :
    # A COMPLETER
    tmp = chiffre1 * chiffre2 + retenue
    op += 0
    retenue = tmp//10
    op += 0
    res.append(tmp%10)
  return res + [retenue], op

def multiplication2(nb1, nb2) :
  "multiplication de nb1, nb2 tableaux de chiffres par algo pose"
  res = []
  op = 0
  for (i, chiffre2) in enumerate(nb2) :
    tmp, opm = multiplication_par_un_chiffre(nb1, chiffre2)
    res, opa = additionV(res, [0]*i + tmp)
    # A COMPLETER
    op += 0
  return res, op

#
# A COMPLETER
#
# La multiplication de deux nombres entiers
#
def multiplication3(nb1, nb2) :
  "multiplication de nb1, nb2 entiers par la methode russe"
  res = 0
  op = 0
  while nb2 != 0 :
    if nb2%2 == 1 : 
      res += nb1
      op += 0 # A COMPLETER
    nb1 = nb1 << 1
    nb2 = nb2 >> 1
    op += 0 # A COMPLETER
  return res, op

#
# AJOUTER D'AUTRES TESTS
#  [parametres, [resultat_attendu, nb ops]]
def testDataValeur() :
  return [[[0, 1], [10, 11]], 
	  [[3, 6, 2], [263, 22]], 
	  [[0, 3, 9, 3], [3930, 33]],
	  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [2000000000, 99]],
	  [[0], [0, 10]]
	  ]

def testDataTableau() :
  return [[   0, [[0], 0]],
          [  63, [[3, 6], 0]],
          [2017, [[7, 1, 0, 2], 0]],
	  [2000000000, [[0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 0]]
	 ]

def testDataAddEq() :
  return [ [ [[0, 1], [1, 1]], [[1, 2], 6] ],
	   [ [[9, 9], [1, 1]], [[0, 1, 1], 6] ],
	   [ [[8, 7, 2, 6], [2, 2, 7, 3]], [[0, 0, 0, 0, 1], 12] ]
	 ]

def testDataMul1() :
  return [ [ [[0, 1], [0, 1]], [[0, 0, 1], 76]],
	   [ [[9, 9], [1, 1]], [[9, 8, 0, 1], 109]],
	   [ [[8, 7, 2, 6], [2, 2, 7, 3]], [[6, 1, 7, 6, 6, 3, 3, 2], 84047] ]
	 ]

def testDataMul2() :
  return [ [ [[0, 1], [0, 1]], [[0, 0, 1], 31]],
	   [ [[9, 9], [1, 1]], [[9, 8, 0, 1], 33]],
	   [ [[8, 7, 2, 6], [2, 2, 7, 3]], [[6, 1, 7, 6, 6, 3, 3, 2], 166] ]
	 ]

def testDataMul3() :
  return [ [ [10, 10], [100, 10]],
	   [ [99, 11], [1089, 11]], 
	   [ [6278, 3722], [23366716, 30]]
	 ]


#
# NE PAS MODIFIER
#
def testOp1(op, data) :
  print('\n\n* Test function %s:' % op.__name__)
  score = 0
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    x = dt[0]
    refr = 0
    refc = 0
    if (len(dt[1]) > 1) :
      refr = dt[1][0]
      refc = dt[1][1]
    else :
      refr = dt[1]
    res = op(x)
    if (refc > 0) :
      r = res[0]
      c = res[1]
    else :
      r = res
      c = 0
    if r == refr and c >= refc :
      score+=1
      print('ok (%s, %s ops)' % (r, c))
    else :
      print('ECHEC')
      print('    entree  : %s' % x)
      print('    calcule : %s' % r)
      print('    attendu : %s' % refr, end='')
      if refc > 0 :
        print(' en minimum %d operations' % refc)
      else :
        print('')

  print('** Score %d/%d' % (score, ldata))

def testOp2(op, data) :
  print('\n\n* Test function %s:' % op.__name__)
  score = 0
  ldata = len(data)
  for i, dt in enumerate(data) :
    print('** test %d/%d : ' % (i + 1, ldata), end='')
    x = dt[0][0]
    y = dt[0][1]
    refr = 0
    refc = 0
    if (len(dt[1]) > 1) :
      refr = dt[1][0]
      refc = dt[1][1]
    else :
      refr = dt[1]
    res = op(x, y)
    if (len(res) > 1) :
      r = res[0]
      c = res[1]
    else :
      r = res
      c = 0
    if (r == refr or valeur(r)[0] == valeur(refr)[0]) and c >= refc :
      score+=1
      print('ok (%s, %s ops)' % (r, c))
    else :
      print('ECHEC')
      print('    entrees : %s, %s' % (x, y))
      print('    calcule : %s' % r)
      print('    attendu : %s' % refr, end='')
      if refc > 0 :
        print(' en minimum %d operations' % refc)
      else :
        print('')

  print('** Score %d/%d' % (score, ldata))


if __name__ == '__main__':
  testOp1(valeur, testDataValeur())
  testOp1(tableau, testDataTableau())
  testOp2(addition, testDataAddEq())
  testOp2(multiplication1, testDataMul1())
  testOp2(multiplication2, testDataMul2())
  testOp2(multiplication3, testDataMul3())

