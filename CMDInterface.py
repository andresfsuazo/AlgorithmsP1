
from utils import *
from os import path
import json

def menu_display(func):
    def inner(current):
        func(current)
        print("0. Quit\n")
    return inner

@menu_display
def build_menu(current_menu):
    for key in current_menu:
        print("{}. {}".format(key, single_dict_key(current_menu[key])))

class CMDInterface():
    def __init__(self, rsa):
        self.current_menu = {}
        self.mainMenu = {}
        self.rsa = rsa
        self.settings = {}
        self.set_settings()
        self.msg = ""

    def set_settings(self):
        """Configure interface using an external, user editable file"""
        if path.exists('menu_settings.json'):
            self.settings = json.load(open('menu_settings.json'))

        self.mainMenu = self.settings['main_menu']

    def display_menu(self):
        self.mainMenu = self.settings['main_menu']
        self.main_menu()

    def call_me(self, arg):
        return getattr(self, arg)()

    # Main menu
    def main_menu(self):
        clear()  # Clear terminal window
        if self.rsa.keysGenerated():
            print("Keys:")
            print("e = " + str(self.rsa.e))
            print("d = " + str(self.rsa.d))
            print("n = " + str(self.rsa.n) + "\n")
        else:
            print("Keys Not Generated Yet!\n")

        print("Message: " + self.msg + "\n")

        # Set current menu to return to if any input problems
        self.current_menu = "main_menu"

        # Menu Options
        build_menu(self.mainMenu)

        choice = input(" >>  ")
        self.function_call(choice)

        return

    # Sub Menu
    def sub_menu(self, name):
        """Build a sub-menu from json file"""
        clear()  # Clear terminal window

        # Set current menu to return to if any input problems
        self.current_menu = name

        # Menu Options
        build_menu(self.settings["sub_menu"][name])

        choice = input(" >>  ")
        self.function_call(choice)

        return

    def results_page(self, results):
        clear()

        # Print Resutls line by line
        for i in results: print(i)
        print("\n")

        # Build an empty menu with only exit and back options
        build_menu({"1": {"Back": "back"}})

        while True:
            choice = input(" >>  ")
            ch = choice.lower()

            if ch == "0":
                exit_app()
                return
            elif ch == "1":
                self.back()
                return
            else:
                print("Invalid selection, please try again.\n")

    # Processing of user input
    def function_call(self, entered):
        clear()
        ch = entered.lower()
        if ch == "0":
            exit_app()
        else:
            try:
                if self.current_menu != "main_menu":
                    to_call = single_dict_key(self.settings["sub_menu"][self.current_menu][ch])
                    to_call = self.settings["sub_menu"][self.current_menu][ch][to_call]
                    self.call_me(to_call)
                else:
                    to_call = single_dict_key(self.settings["main_menu"][ch])
                    to_call = self.settings["main_menu"][ch][to_call]
                    self.call_me(to_call)
            except KeyError:
                print("Invalid selection, please try again.\n")
                self.sub_menu("home") if self.current_menu != "main_menu" else self.main_menu()
        return

    def encrypt(self):
        # If login credential accepted go to home menu
        if self.rsa.keysGenerated():
            self.msg = self.rsa.encrypt(self.msg)
        else:
            input("Generate Keys First!\npress any key to go back: ")
            self.main_menu()

        self.main_menu()

    def decrypt(self):
        # If login credential accepted go to home menu
        if self.rsa.keysGenerated():
            self.msg = self.rsa.decrypt(self.msg)
        else:
            input("Generate Keys First!\npress any key to go back: ")
            self.main_menu()

        self.main_menu()

    def setMessage(self):
        inp = ""
        while len(inp) < 1:
            inp = input("Enter Message: ")

        self.msg = inp
        self.main_menu()

    def generateKeys(self):
        self.rsa.generateKeys()
        self.main_menu()

    def back(self):
        self.sub_menu("home")
