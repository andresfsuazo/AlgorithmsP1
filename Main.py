from RSA import RSA
from RSA import *
from CMDInterface import CMDInterface

def main():
    rsa = RSA()
    UI = CMDInterface(rsa)
    UI.display_menu()

def test():
    rsa = RSA()
    rsa.e = 3
    rsa.d = 2011
    rsa.n = 3127
    message = "hello"

    print("Test known values e={}, d={}, n={}".format(rsa.e, rsa.d, rsa.n))
    print("Message to encrypt/decrypt: " + message)

    enc = rsa.encrypt(message)
    print("Encrypted message: " + enc)
    dec = rsa.decrypt(enc)
    print("Decrypted message: " + dec)

def test2():
    rsa = RSA()
    rsa.e = 3
    rsa.d = 2011
    rsa.n = 3127
    message = "hello"

    print("Test known values e={}, d={}, n={}".format(rsa.e, rsa.d, rsa.n))
    print("Message: " + message)

    enc = rsa.encrypt(message)
    print("Encrypted message: " + enc)
    dec = rsa.decrypt(enc)
    print("Decrypted message: " + dec)

    sig = "andres"
    print("Signature: " + sig)
    dec2 = rsa.decrypt(sig, True)
    print("Generated Signature: " + dec2)
    auth = rsa.encrypt(dec2, True)
    print("After Authentication: " + auth)

if __name__ == '__main__':
    main()
