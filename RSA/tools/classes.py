from tools import support

class prime:
	def __init__(self, rg): #range
		self.plist = [2, 3, 5, 7] #list of primes lesser than rg
		self.set_primes(max(rg, self.plist[-1]))

	def verify(self, x): #verify if 'x' is prime
		if self.plist[-1] * self.plist[-1] < x:
			return "it's not possible to verify"
		k = 0
		while self.plist[k] * self.plist[k] <= x:
			if x % self.plist[k] == 0:
				return False
			k += 1
		return True

	def set_primes(self, rg): #calculates the primes lesser than 'rg' and store them inside 'plist'
		pos = 0
		delta = [2, 2, 2, 4] #helps to search for primes faster, since primes        ::: xx7 xx8 xx9 xx0 xx1 xx2 xx3 xx4 xx5 xx6 xx7
							 #bigger than 5 can only have 1, 3, 7 or 9 as last digit :::   ^  +2   ^  +2   ^  +2   ^      +4       ^ 
		N = self.plist[-1] + delta[pos]
		while N < rg:
			if self.verify(N):
				self.plist.append(N)
			pos = (pos + 1) % 4
			N += delta[pos]

class cript_key:
	def __init__(self, n, k):
		self.n = n
		self.k = k

class person:
	def __init__(self, personal_key):
		self.pk = personal_key
		self.M = ''
		self.m = 0
		self.c = 0		

class messenger(person):
	def __init__(self, personal_key):
		person.__init__(self, personal_key)

	def unpadding_scheme(self):
		while self.m > 0:
			bit = self.m % 100
			self.m = self.m // 100
			if bit != 99:
				self.M += chr(bit - 1 + ord('a'))
			else:
				self.M += ' '
		self.M = self.M[::-1]

	def decript(self):
		self.m = support.modular_exponentiation(self.c, self.pk.k, self.pk.n) % self.pk.n

class receiver(person):	
	def __init__(self, personal_key):
		person.__init__(self, personal_key)

	#turn each letter of M into a number between 0 and 25 (spaces are marked as 99)
	def padding_scheme(self):
		for k in range(len(self.M)):
			if self.M[k] != ' ':
				letter = ord(self.M[k]) - ord('a') + 1
			else:
				letter = 99;
			self.m = self.m * 100 + letter

	def encript(self):
		self.c = support.modular_exponentiation(self.m, self.pk.k, self.pk.n)