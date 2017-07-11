#https://en.wikipedia.org/wiki/RSA_(cryptosystem)
from tools import functions, classes

p, q = functions.rand_pq()
n = p * q
ln = functions.reduced_totient(p, q)

e = functions.coprime_finder(ln) #public key
d = functions.modular_inverse(e, ln) #private key

public_key = classes.cript_key(n, e)
private_key = classes.cript_key(n, d)
#'p', 'q' and 'ln' must also be kept secret because they can be used to calculate 'd'

#key distribution
#Suppose that Bob wants to send a secret message to Alice.
#If they decide to use RSA, Bob must know Alice's public key
#to encrypt the message and, Alice must use her private key
#to decrypt the message. To enable Bob to send his encrypted
#messages, Alice transmits her public key (n, e) to Bob via a
#reliable, but not necessarily secret route. Alice's private
#key 'd', is never distributed.

Alice = classes.messenger(private_key)
Bob = classes.receiver(public_key)

#encryption
#After Bob obtains Alice's public key, he can send a message M
#to Alice. To do it, he first turns M (strictly speaking, the
#un-padded plaintext) into an integer m (strictly speaking,
#the padded plaintext), such that 0 ≤ m < n by using an agreed-upon
#reversible protocol known as a padding scheme. He then computes the
#ciphertext 'c', using Alice's public key e, corresponding to
#'c = m^e (mod n)'. This can be done reasonably quickly, even
#for 500-bit numbers, using modular exponentiation. Bob then
#transmits c to Alice.

Bob.M = 'this is my secret messageç á ú âãttttttttttttttttt'
Bob.padding_scheme()

Bob.encript()
#encripted message
print('encripted message: ')
for k in Bob.c:
	print(k, end=',')
print()

#decryption
#Alice can recover m from c by using her private key exponent
#'d' by computing 'c^d = m (mod n). Given m, she can recover
#the original message M by reversing the padding scheme

Alice.c = Bob.c
Alice.decript()
Alice.unpadding_scheme()

print()
print('retrieved message:\n', Alice.M) #retrieved message