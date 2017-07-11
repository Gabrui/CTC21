from ferramentas import suporte

tam_bloco = 78 # agrupa a mensagem em blocos de 78 caracteres

class chave_criptica: # classe da chave (publica ou privada)
	def __init__(self, n, k):
		self.n = n # produto de dois primos grandes
		self.k = k # expoente 

class pessoa:
	def __init__(self, chave_pessoal):
		self.pk = chave_pessoal
		self.M = '' # mensagem a ser enviada
		self.m = [] # mensagem convertida em números
		self.c = []	# mensagem encriptada

class mensageiro(pessoa):	
	def __init__(self, chave_pessoal):
		pessoa.__init__(self, chave_pessoal)

	def conversor(self): # transforma a mensagem 'M' (caracteres) em um conjunto de números 'm'
		# a mensagem 'M' é separada em blocos de 'tam_bloco' caracteres. caso a mensagem tenha um tamanho
		# que não seja múltiplo de 'tam_bloco', o bloco é completado com '\0'.
		for k in range(tam_bloco - len(self.M) % tam_bloco):
			self.M += '\0'
		# os blocos de 'tam_bloco' caracteres são transformados em número seguindo a codificação ASCII.
		# por exemplo, o bloco 'cripto' seria convertido em '099114105112116111'. primeiramente os caracteres
		# são convertidos em seus correspondentes ascii ('c = 99', 'r = 114', 'i = 105', 'p = 112', 't = 116'
		# e 'o = 111') e concatenados: 99 + 114 + 105 + 112 + 116 + 111 = 099114105112116111 (aqui '+' significa
		# concatenação e não soma) completando com zeros à esquerda onde for necessário.
		for k in range(len(self.M) // tam_bloco):
			valor = 0
			for j in range(tam_bloco):
				valor = valor * 1000 + ord(self.M[k * tam_bloco + j])
			self.m.append(valor)

	def encriptar(self): # encripta a mensagem convertida 'm'
		for k in self.m:
			self.c.append(suporte.exponenciacao_modular(k, self.pk.k, self.pk.n) % self.pk.n)

class destinatario(pessoa):
	def __init__(self, chave_pessoal):
		pessoa.__init__(self, chave_pessoal)

	def desconversor(self): # transforma a mensagem 'm' (números) decriptada na mensagem original 'M' (caracteres)
		# o processo é o inverso do exemplificado no 'conversor'. os blocos são separados em grupos de números
		# de 3 dígitos (na codificação ASCII, os caracteres são mapeados em números de 0 a 255) e, em seguida, os
		# números em ASCII são convertidos em seus caracteres correspondentes. por exemplo: o bloco '114115097'
		# seria separado em 114, 115 e 97. em seguida, os números seriam convertidos em seus correspondentes ASCII:
		# 114 = 'r', 115 = 's' e 97 = 'a'. assim, a mensagem desconvertida é 'rsa'.
		for k in self.m:
			for j in range(tam_bloco):
				l = chr(k // (1000 ** (tam_bloco - j - 1)))
				if l != '\0':
					self.M += l
				k %= (1000 ** (tam_bloco - j - 1))

	def decriptar(self): # decripta a mensagem 'c' no conjunto de números 'm'
		for k in self.c:
			self.m.append(suporte.exponenciacao_modular(k, self.pk.k, self.pk.n) % self.pk.n)