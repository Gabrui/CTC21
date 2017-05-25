import math

def update(var, new_var, q):
	aux = new_var
	new_var = var - q * new_var
	var = aux
	return var, new_var

#calculates the greatest common divisor of 'a' and 'b'
def GCD(a, b):
	while b != 0:
		r = a % b
		a = b
		b = r
	return a

#calculates the largest common multiple of 'a' and 'b'
def LCM(a, b):
	return (a * b) // GCD(a, b)

#calculates 'c = m^e (mod n)'
def modular_exponentiation(x, e, n):
	if e == 0:
		return 1
	mul = 1
	if e % 2 == 1:
		mul = x
	return (mul * modular_exponentiation((x * x) % n, e // 2, n)) % n