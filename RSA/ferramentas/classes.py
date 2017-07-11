import time
from ferramentas import suporte

tam_bloco = 95 # agrupa a mensagem em blocos de 95 caracteres

# classe da chave (publica ou privada)
class chave_criptica:
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

	# transforma a mensagem 'M' (caracteres) em um conjunto de números 'm'
	def conversor(self): 
		# a mensagem 'M' é separada em blocos de 'tam_bloco' caracteres. caso a mensagem tenha um tamanho
		# que não seja múltiplo de 'tam_bloco', o bloco é completado com '\0'.
		for k in range(tam_bloco - len(self.M) % tam_bloco):
			self.M += '\0'
		# os blocos de 'tam_bloco' caracteres são transformados em número seguindo a codificação ASCII e trabalhando na
		# base 256 (uma vez que a codificação ASCII admite 256 caracteres). por exemplo, supondo 'tam_bloco = 6' o bloco 
		# 'cripto' seria convertido em '99 * 256^5 + 114 * 256^4 + 105 * 256^3 + 112 * 256^2 + 116 * 256 + 111'
		# que equivale a '109343046399087'. aqui os caracteres foram convertidos em seus valores ASCII ('c = 99', 'r = 114',
		# 'i = 105', 'p = 112', 't = 116' e 'o = 111') e tratados como dígitos de um número de 6 dígitos na base 256.
		for k in range(len(self.M) // tam_bloco):
			valor = 0
			for j in range(tam_bloco):
				valor = valor * 256 + ord(self.M[k * tam_bloco + j])
			self.m.append(valor)

	# encripta a mensagem convertida 'm'
	def encriptar(self):
		for k in self.m: # -> O(len(m)) . O(log2(e)) . O(% n)
			self.c.append(suporte.exponenciacao_modular(k, self.pk.k, self.pk.n) % self.pk.n)
	
class destinatario(pessoa):
	def __init__(self, chave_pessoal):
		pessoa.__init__(self, chave_pessoal)

	# transforma a mensagem 'm' (números) decriptada na mensagem original 'M' (caracteres)
	def desconversor(self):
		# o processo é o inverso do exemplificado no 'conversor'. os blocos são desmembrados em seus dígitos (considerando
		# a base 256) e, em seguida, os números são convertidos em seus caracteres correspondentes segundo a codificação 
		# ASCII. por exemplo: o bloco '7500641 = 114 * 256^2 + 115 * 256 + 97' seria separado em 114, 115 e 97. em seguida,
		# os números seriam convertidos em seus correspondentes ASCII: 114 = 'r', 115 = 's' e 97 = 'a'. assim, a mensagem
		# desconvertida é 'rsa'.
		for k in self.m:
			for j in range(tam_bloco):
				l = chr(k // (256 ** (tam_bloco - j - 1)))
				if l != '\0': # desconsidera os caracteres '\0' inseridos para completar os blocos
					self.M += l
				k %= (256 ** (tam_bloco - j - 1))

	# decripta a mensagem 'c' no conjunto de números 'm'
	def decriptar(self):
		for k in self.c: # -> O(len(m)) . O(log2(d)) . O(% n)
			self.m.append(suporte.exponenciacao_modular(k, self.pk.k, self.pk.n) % self.pk.n)