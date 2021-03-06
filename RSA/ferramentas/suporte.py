import math

# lê a mensagem salva no arquivo 'mensagem.txt' e retorna uma string com o texto lido
def ler_mensagem(nome = 'mensagem.txt'):
	f = open(nome, 'r')
	line = f.readlines()
	f.close()
	return line[0]

def atualiza(var, nova_var, q):
	aux = nova_var
	nova_var = var - q * nova_var
	var = aux
	return var, nova_var

# calcula o MDC de 'a' e 'b'
def MDC(a, b): # -> O(log2(min(a, b)))
	while b != 0:
		r = a % b
		a = b
		b = r
	return a

# calcula 'c = m^e (mod n)'
def exponenciacao_modular(x, e, n): # -> O(log2(e)) . O(% n)
	return pow(x, e, n)

# calcula o inverso de 'a' módulo 'n'
def inverso_modular(a, n): # -> log²(n)
	t, r = 0, n
	novo_t, novo_r = 1, a
	while novo_r != 0:
		q = r // novo_r
		t, novo_t = atualiza(t, novo_t, q)
		r, novo_r = atualiza(r, novo_r, q)
	if r > 1:
		return 'não inversível'
	elif t < 0:
		return t + n
	return t

# encontra um número menor que 'x' que seja coprimo com 'x'
divisor = 10 # esta variável pode assumir qualquer valor entre 1 e 'x'
             # sua finalidade é impedir que as chaves pública e privada seja iguais 
def encontra_coprimo(x):
	y = x // divisor
	while y > 1: # -> O(log2(y) * x)
		if MDC(y, x) == 1: 
			return y
		y -= 1
	y = (x // divisor) + 1
	while y < x: # -> O(log2(x) * x)
		if MDC(y, x) == 1:
			return y
		y += 1
	return None