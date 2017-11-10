from random import randint

def hot_cold():
	number=randint(0,100)
	for i in range (0,10):
		guess=input('guess a number ')
		closeness=abs(number-guess)
		if number==guess:
			print str(number)+" that is correct"
			break
		elif closeness<=10 and closeness>5:
			print 'hot'
		elif closeness<=5:
			print "fuego"
		elif closeness>10 and closeness<=50:
			print 'cold'
		else:
			print "not even close motherfucker"
	if number!=guess:
		print "haha loser. correct answer was: ", number

hot_cold()

