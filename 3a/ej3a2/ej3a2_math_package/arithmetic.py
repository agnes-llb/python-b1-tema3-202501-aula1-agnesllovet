# arithmetic.py
import math

def power(base: float, exponent: float) -> float:
	# Write your code here
	if (isinstance(base, int) != True and isinstance(base, float) != True ):
		raise ValueError ("El parametre d'entrada base no es un nuemro")
	if (isinstance(exponent, int) != True and isinstance(exponent, float) != True ):
		raise ValueError ("El parametre d'entrada exponent no es un nuemro")
	return (math.pow(base, exponent))
	pass

def square_root(num_1: float) -> float:
	# Write your code here
	if (isinstance(num_1, int) != True and isinstance(num_1, float) != True ):
		raise ValueError ("El parametre d'entrada no es un numero")
	return (math.sqrt(num_1))
	pass


