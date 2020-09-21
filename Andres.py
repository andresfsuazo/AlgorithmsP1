import random

def isPrime(p, k):
    """Checks if an integer is a prime number using Fermat's Little Theorem"""

    prime = True

    while k>0:

        check = random.randint(1, p - 1)

        if not isRelativelyPrime(check, p):
            return False

        if pow(check, p-1, p) != 1:
            prime = False

        k -= 1

    return prime

def randomPrime(min, max):
    "Return a random prime number between input min and max"
    p = 6
    while not isPrime(p, 30):
        p = random.randint(min, max)

    return p

def gcd(a, b):
    "Returns greatest common divisor"
    if a == 0:
        return b

    return gcd(b % a, a)

def extendedgcd(a,b):
    """Extended Euclidean Algorithm"""
    if b == 0:
        return (1, 0, a)

    (x, y, d) = extendedgcd(b, a % b)
    return y, x - a // b * y, d

def isRelativelyPrime(e,r):
    """Returns true if q and p are relatively prime"""
    return gcd(e, r) == 1

def isMI(a, b):
    """Returns true if b is the multiplicative inverse of a"""
    pass

def encrypt(e, n, value):
    #C = M^e mod n

    #Divide message into character and convert to ascii
    msg = [ord(i) for i in value]
    print("Before encrypt: " + str(msg))

    #Encrypt each character and create a space separated string
    msg = [str((pow(i,e) % n)) + " " for i in msg]
    msg = "".join(msg)
    print("After encrypt: " + msg)
    return msg

def decrypt(d, n, value):
    #M = C^d mod n

    #Divide string into separate integers
    msg = [int(i) for i in value.split(" ")[:-1]]
    print("Before decrypt: " + str(msg))

    #Decrypt list of integers and merge into single message
    msg = [str((pow(i,d) % n)) + " " for i in msg]
    msg = "".join(msg)
    print("After decrypt: " + msg)
    return msg

def getKeys():

    primeMin = 1000
    primeMax = 100000

    p = randomPrime(primeMin, primeMax)
    q = randomPrime(primeMin, primeMax)

    n = p*q

    print("p = {}\nq = {}\nn = {}".format(p,q,n))

    fn = (p-1) * (q-1)

    d, e = 1, 1

    # e has to be relatively prime fn && less than fn
    found = False
    while not found:
        e = random.randint(1, fn-1)
        if isRelativelyPrime(e, fn):
            found = True

    print("e = {}".format(e))

    # d has to be the multiplicative inverse of e && less than fn
    found = False
    while not found:
        d = random.randint(0, fn - 1)
        if isMI(d, fn):
            found = True
    print("d = {}".format(d))

#Test values for encrypt/decrypt
a = encrypt(5,119,"Hello")
decrypt(77,119,a)