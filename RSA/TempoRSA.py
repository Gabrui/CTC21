#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math, time # para medição dos tempos de execução
from ferramentas import suporte, classes # módulos auxiliares

ti = time.time() # início da execução

# Chave de 2048 bits
p = 0x00f0d1d6f7167056d39e22cd86ae0c4cc7ef4673e9b7799191d32446c78d3e77e8c90a9192170f60f482d5af25216dac068067e71e8e69fb3f42af96d2116d6693b43715a5d2ebf6fa5f13ee5977e44b876ec62bd2013d33f8ad23209272d5b0c070d22411839377e7d0319aca293beedc3ca1a169c26d24ae9ea3c5b779daecf1
q = 0x00d35b3c8c74c84e0200baff2f400e405e353b9bcd089fc1dc684460512adea0359c17b972586900c224aaf73ee3ffb2258d731c44bd19067ebe0f104d67f9a5c2d35e533ab580d202194d3a84081cbb8dc3c4d21411514f90c7904766bd97fbfa4fa423712bc2b169b14b196838a2200cfd3d08ab31468feff8dfe0942b13bc1b
n = p * q
ln = (p - 1) * (q - 1)
e = 0x10001
d = 0x00ac879ff5a53c3cf392e2fcaafc610ddc759b861e93f880289452f5a6131432f322d30869962846e02859977532e5b37cbdfc9e6bb0bcb3746c5fbb68da270b91184e3861c48442795314bdf4ff351e2a3590657d41297b1043b5e0616d43d958d9f3b3e188247f9a5dbf5aae7314e40c7f4654be04ba9a7878c33a5de6edef93995946a22837b05208fb71725ed1c203d49a7c2d8efa43c1c52b47135050bf4092b72412a6de42cd9e996c45b57cb904f2114e4f081cc076707c2309ed618385184c0b28dd83d310b70ab6b027aa8f3034e6733e7ddb12c7517ae4ac9a2ae717819a891f22654edeb638b4269caaef5341c30d110a1c1f5ab7c6fc1049462e41

chave_publica = classes.chave_criptica(n, e)
chave_privada = classes.chave_criptica(n, d)

Alice = classes.destinatario(chave_publica)
Bob = classes.mensageiro(chave_privada)


Bob.M = "olá" # lê a mensagem salva no arquivo 'mensagem.txt'
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


Alice.c = Bob.c
Alice.decriptar()
Alice.desconversor()

#tf = time.time()

print('mensagem recuperada:\n', Alice.M)
