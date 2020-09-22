import random


def isPrime(N):  # Function to check prime number
    if N > 1:
        for i in range(2, N):
            if (N % i) == 0:
                return False
        else:
            return True
    else:
        return False


def GCD(a, b):
    if (b == 0):
        return a
    else:
        return GCD(b, a % b)


class Encryption:  # Encryption Class
    def __init__(self):  # Constructor
        with open("initialize.txt", 'rt') as f:
            for lines in f:
                self.publickey, self.privatekey = lines.split(' ')  # initializing keys
        self.privatekey = int(self.privatekey)
        self.publickey = int(self.publickey)
        self.Signature = "Signature"
        self.GeneratedSign = ""
        self.Authenticated = ""
        self.Encrypted = ""
        self.Decrypted = ""
        self.user = None
        self.Data = ""
        self.seeds = []

    def Seeds(self):  # Generating prime numbers
        Primes = [i for i in range(50) if isPrime(i)]
        self.seeds.append(random.choice(Primes))
        self.seeds.append(random.choice(Primes))

    def User(self):  # Function to check user or owner
        In = input("Are you a User or Owner: ")
        if In == "User":
            self.user = 0
        elif In == "Owner":
            self.user = 1
        else:
            self.User()

    def Encrypt(self):  # function for encryption
        for i in self.Data:
            self.Encrypted += chr(ord(i) + self.publickey)  # Encrypt data with public key
        print("Encryption Successful.")
        print("Encrypted Data :", self.Encrypted)

    def Decrypt(self):  # Function for decryption
        if len(self.Encrypted) == 0:
            print("No Text Encrypted yet.")
            return
        for i in self.Encrypted:
            self.Decrypted += chr(ord(i) - self.publickey)
        print("Decryption Successful.")
        print("Decrypted Data :", self.Decrypted)

    def GenerateSignature(self):  # Function for Digital Signature
        for i in self.Signature:
            self.GeneratedSign += chr(ord(i) + self.privatekey)

    def AuthenticateSignature(self):  # Function to Autheticate Signature
        for i in self.GeneratedSign:
            self.Authenticated += chr(ord(i) - self.privatekey)
            if self.Authenticated == self.Signature:
                return True
            else:
                return False

    def GenerateKeys(self):  # Finding Private Key with RSA
        self.Seeds()
        n = self.seeds[0] * self.seeds[1]
        Qn = (self.seeds[0] - 1) * (self.seeds[1] - 1)
        i = 0
        self.publickey = random.randint(1, Qn)
        while True:
            if GCD(self.publickey, Qn) == 1:
                break
            else:
                self.publickey = random.randint(1, Qn)
        while True:
            private = (1 + (i * Qn)) / self.publickey
            if private.is_integer():
                return private
            else:
                i += 1

    def FindPublickey(self):  # Similarly Finding public Key with RSA
        n = self.seeds[0] * self.seeds[1]
        Qn = (self.seeds[0] - 1) * (self.seeds[1] - 1)
        i = 0
        while True:
            public = (1 + (i * Qn)) / self.privatekey
            if public.is_integer():
                print(public)
                return public
            else:
                i += 1

    def Program(self):  # Driver Program
        self.User()
        if not self.user:
            self.GenerateSignature()
            print("Digital Signature:", self.GeneratedSign)
            Key = int(input("Enter the Public Key:"))
            if Key == self.publickey:
                while True:
                    print("Press 1 to Encrypt Message.")
                    print("Press 2 to Authenticate Signature.")
                    print("Press 3 to Quit.")
                    In = int(input("Enter:"))
                    if In == 1:
                        self.Data = input("Enter Text:")
                        self.Encrypt()
                    elif In == 2:
                        Pkey = int(input("Enter Key to Authenticate:"))
                        if Pkey == self.privatekey:
                            if self.AuthenticateSignature():
                                print("Signature Authenticated.")
                                print("Signature :", self.Authenticated)
                            else:
                                print("Authentication failed.")
                        else:
                            print("Invalid Key.")
                    elif In == 3:
                        break
            else:
                print("Invalid Key.")
        else:
            print("Generating a public-private keyPair:")
            self.GenerateKeys()
            print("Public key:", self.publickey)  # Key Generation using RSA
            print("private key:", self.privatekey)
            while True:
                print("Press 1 to Decrypt Message.")
                print("Press 2 to Generate Signature.")
                print("Press 3 to Quit.")
                In = int(input("Enter:"))
                if In == 1:
                    key = int(input("Enter Key to Decrypt:"))
                    if key == self.publickey:
                        self.Decrypt()
                    else:
                        print("Invalid Key.")
                elif In == 2:
                    self.Signature = input("Enter Signature:")
                    self.GenerateSignature()
                    print("Signature Generated.")
                    print("Signature :", self.GeneratedSign)
                elif In == 3:
                    break


if __name__ == '__main__':
    obj = Encryption()
    obj.Program()
