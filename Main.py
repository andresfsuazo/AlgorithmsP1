from RSA import RSA
from CMDInterface import CMDInterface

def main():
    rsa = RSA()
    UI = CMDInterface(rsa)
    UI.display_menu()


if __name__ == '__main__':
    main()
