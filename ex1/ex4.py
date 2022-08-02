#!/usr/bin/env python3

#
#
# Somme des entiers de 1 a x avec un boucle
#
def somme_bete(x) :
	S=0
	for i in range (0,x+1) :
		S+=i
	return S

#
# A REMPLIR
#
# Somme des entiers de 1 a x avec la formule
#
def somme_rapide(x) :
	S = x*(x + 1)/2
	return S

# 
# A REMPLIR
#
# Liste des premiers n carres : version avec boucle
#
def premiersCarresIt(n):
	res = [0] * (n + 1)
	for x in range(1, n + 1):
		res[x] = x**2
	return res

# 
# A REMPLIR
#
# Liste des premiers n carres : version recursive
#
def premiersCarresRec(n, res=None) :
    if res is None:
        res =[]
    res.append(n**2)
    if n > 0 :
        premiersCarresRec(n - 1, res)           
    return res[::-1]


#
# AJOUTER D'AUTRES TESTS
#  [valeur_x, resultat_attendu]
def testDataSomme() :
	return [[0, 0], [3, 6], [24, 300], [-3, 0]]


def testDataCarres() :
	return [	[0, []], 
			[-2, []], 
			[2, [0, 1]], 
			[10, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]]
		]

#
# NE PAS MODIFIER
#
def testOp(op, data) :
	print('\n\n* Test function %s:' % op.__name__)
	score = 0
	ldata = len(data)
	for i, dt in enumerate(data) :
		print('** test %d/%d : ' % (i + 1, ldata), end='')
		x = dt[0]
		refr = dt[1]
		r = op(x)
		if r == refr :
			score+=1
			print('ok')
		else :
			print('ECHEC')
			print('    entree  : %s' % x)
			print('    calcule : %s' % r)
			print('    attendu : %s' % refr)
	print('** Score %d/%d' % (score, ldata))


if __name__ == '__main__':
	testOp(somme_bete, testDataSomme())
	testOp(somme_rapide, testDataSomme())
	testOp(premiersCarresIt, testDataCarres())
	testOp(premiersCarresRec, testDataCarres())

