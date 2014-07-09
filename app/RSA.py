#RSA
from random import randrange
from fractions import gcd

def readFileToList(name):
	f = open(name, "r")
	x = []
	x = f.readline()
	f.close()
	j=0
	i=1
	temp = ""
	letList = []
 	while (i < len(x)):
			if (x[i] != ',' and x[i] != 'L' and x[i] != ']'):
				temp = temp + x[i]
			if(x[i] == ',' or x[i] == ']'):
				letList.append(int(temp))
				j = j + 1
				temp = ""
			i = i + 1				
	return letList

def getVars():
	p = randNum()
	q = randNum()
	
	m = p * q
	
	a = (p-1)*(q-1)
	
	e = getE(a)
	
	d = getD(e, a)
	stringOutput = "Your public keys:\nE=" + str(e) + "\nM=" + str(m)
	stringOutput = stringOutput + "\nYour private key:\nD=" + str(d)
	return stringOutput
	
# DECRYPT
def decrypt(temp, m, d):
	#raise to powD
	temp = toD(temp, d)
	temp = modM(temp, m)
	#num to Let
	temp = toLet(temp)
	return temp
# DECRYPTION METHODS
def toD(temp, d):
	for i in range(len(temp)):
		temp[i] = pow(temp[i], d)
	return temp
def modM(temp, m):
	for i in range(len(temp)):
		temp[i] = temp[i]%m
	return temp
def toLet(temp):
	for i in range(len(temp)):
		temp[i] = getLet(temp[i])
	return temp
def getLet(x):
	alpha = ["~","~","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ",", ".","?", "'", "!", "@", "#", "$", " "]
	return alpha[x]
# ENCRYPT
def encrypt(temp, e, m):
	#put as numbers
	temp = str(temp)
	temp = temp.upper()
	e = int(e)
	m = int(m)
	word = [None] * len(temp)
	for i in range(len(temp)):
		word[i] = getNum(temp[i])
	word2 = encypher(word, e, m)
	return word2
# ENCRYPTION METHODS
def encypher(temp, e, n):
	for i in range(len(temp)):
		temp[i] = (pow(temp[i], e))% n
	return temp
				
def getD(x, y):
	temp = 0
	while(temp == 0):
		for i in range(10000):
			temp2 = i
			if(((temp2 * x) - 1) % y==0):
				temp = temp2
	return temp
	
def getE(x):
	temp = randrange(2, x)
	while (gcd(temp, x)!=1):
		temp = randrange(1, x)
	return temp
	
	
def randNum():
	temp = randrange(1, 100)
	if(is_prime(temp)):
		return temp
	else:
		return randNum()

def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
    if not num%2 or not num%3:
        return False
    for i in range(5, int(num**0.5) + 1, 6):   
        if not num%i or not num%(i + 2):
            return False
    return True
    
def getNum(x):
	alpha = ["~","~","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ",", ".","?", "'", "!", "@", "#", "$", " "]
	for i in range(len(alpha)):
		if(x==alpha[i]):
			return i
