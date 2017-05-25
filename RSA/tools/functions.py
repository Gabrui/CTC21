#https://en.wikipedia.org/wiki/Euclidean_algorithm
import random
from tools import support, classes

#list of prime numbers lesser than 'MAX_PRIME'
MAX_PRIME = 100000
prime_list = classes.prime(MAX_PRIME)

#calculats the modular inverse of 'a' modulo 'n'
def modular_inverse(a, n):
	t, r = 0, n
	new_t, new_r = 1, a
	while new_r != 0:
		q = r // new_r
		t, new_t = support.update(t, new_t, q)
		r, new_r = support.update(r, new_r, q)
	if r > 1:
		return 'not invertible'
	elif t < 0:
		return t + n
	return t
#change variables latter!!!!

#choses at random two prime numbers from 'plist'
def rand_pq():
	leng = len(prime_list.plist) - 1
	p = prime_list.plist[random.randint(0, leng)]
	q = prime_list.plist[random.randint(0, leng)]
	return p, q

#https://en.wikipedia.org/wiki/Carmichael_function
def reduced_totient(p, q):
	return support.LCM(p - 1, q - 1)

#find a number lesser than 'x' that is coprime with 'x'
divider = 10 #this variable can be any number between 1 and 'x'
             #it's here just to prevent equal public and private keys
def coprime_finder(x):
	y = x // divider
	while y > 1:
		if support.GCD(y, x) == 1:
			return y
		y -= 1
	y = (x // divider) + 1
	while y < x:
		if support.GCD(y, x) == 1:
			return y
		y += 1
	return None