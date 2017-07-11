from tools import support

tam_bloco = 3

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
		self.m = []
		self.c = []		

class messenger(person):
	def __init__(self, personal_key):
		person.__init__(self, personal_key)

	def unpadding_scheme(self):
		print('oi')
		for k in self.m:
			for j in range(tam_bloco, 0):
				self.M += chr(k/(1000**(tam_bloco-j-1)))
				k %= (1000**(tam_bloco-j-1))

	def decript(self):
		for k in self.c:
			self.m.append(support.modular_exponentiation(k, self.pk.k, self.pk.n) % self.pk.n)

class receiver(person):	
	def __init__(self, personal_key):
		person.__init__(self, personal_key)

	#turn each letter of M into a number between 0 and 255 (spaces are marked as 99)
	def padding_scheme(self):
		for k in range(tam_bloco - len(self.M)%tam_bloco):
			self.M.append('\0')
		for k in range(len(self.M)//tam_bloco):
			valor = 0
			for j in range(tam_bloco):
				valor = valor*1000 + ord(self.M[k*tam_bloco+j])
			self.m.append(valor)


	def encript(self):
		for k in self.m:
			self.c.append(support.modular_exponentiation(k, self.pk.k, self.pk.n) % self.pk.n)