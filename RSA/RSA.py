import math, time # para medição dos tempos de execução
from ferramentas import suporte, classes # módulos auxiliares

ti = time.time() # início da execução

# menor primo maior que 10^115
p = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000079

# menor primo maior que 10^120
q = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000079

n = p * q
ln = (p - 1) * (q - 1) # totiente(n)

e = suporte.encontra_coprimo(ln) # expoente da chave publica
d = suporte.inverso_modular(e, ln) # expoente da chave privada

chave_publica = classes.chave_criptica(n, e)
chave_privada = classes.chave_criptica(n, d)
#'p', 'q' e 'ln' devem ser mantidas em sigilo, pois podem ser usadas para calcular 'd'

# distribuição da chave
# suponha que Bob queira enviar uma mensagem secreta para Alice:
# usando o RSA, Bob deve saber a chave pública de Alice para 
# encriptar a mensagem e Alice deve usar a chave privada para
# decriptar a mensagem. para que Bob possa enviar mensagens
# encriptadas, Alice transmite a chave pública (n, e) para Bob
# de uma forma não necessariamente segura. a chave privada 'd' de
# Alice nunca é distribuída.

Alice = classes.destinatario(chave_publica)
Bob = classes.mensageiro(chave_privada)

# encriptação
# depois de Bob obter a chave pública de Alice, ele pode enviar a
# mensagem 'M'. primeiro ele converte o texto em 'M' em um número
# inteiro 'm' tal que 0 ≤ m < n usando um protocolo reversível
# conhecido por Alice. em seguida, a mensagem é encriptada em 'c'
# utilizando a chave pública 'e' de Alice (c = m^e (mod n)).
# isto pode ser feito de forma razoavelmente fácil usando a 
# exponenciação modular. enfim, Bob transmite 'c' para Alice.

Bob.M = suporte.ler_mensagem() # lê a mensagem salva no arquivo 'mensagem.txt'
print('mensagem original: ')
print(Bob.M)
print()

Bob.conversor()
Bob.encriptar()
print('mensagem encriptada: ')
for k in Bob.c:
	print(k, end='')
print()
print()

# decriptação
# Alice pode recuperar 'm' de 'c' usando o expoente 'd' da chave privada
# (que apenas Alice conhece) ao computar 'c^d = m (mod n)'. a partir de
# 'm', utilizando o protocolo reversível, Alice pode recuperar a mensagem
# 'M' original.

Alice.c = Bob.c
Alice.decriptar()
Alice.desconversor()

#tf = time.time()

print('mensagem recuperada:\n', Alice.M)

#print()
#print(tf - ti)

#https://en.wikipedia.org/wiki/RSA_(cryptosystem)
#https://en.wikipedia.org/wiki/Euclidean_algorithm
#http://pt.numberempire.com/primenumbers.php