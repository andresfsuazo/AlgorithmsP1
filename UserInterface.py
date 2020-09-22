from os import path
import abc
import json

"""
Interface for both terminal use and Graphical Interface
"""


class UserInterface(metaclass=abc.ABCMeta):

    @classmethod
    def version(cls):
        """User interface version"""
        return "1.0"

    def __init__(self, rsa):
        self.mainMenu = ""
        self.rsa = rsa
        self.settings = {}
        self.set_settings()

    def set_settings(self):
        """Configure interface using an external, user editable file"""
        if path.exists('menu_settings.json'):
            self.settings = json.load(open('menu_settings.json'))

        self.mainMenu = self.settings['main_menu']

    @abc.abstractmethod
    def display_menu(self):
        """Start the display that the user will interact with"""
        pass

    @abc.abstractmethod
    def encrypt(self):
        """Send Login information to server and wait for confirmation"""
        raise NotImplementedError

    @abc.abstractmethod
    def decrypt(self):
        """Send account information for a new account to server and wait for confirmation"""
        raise NotImplementedError

    @abc.abstractmethod
    def setMessage(self):
        """Gets account information from server"""
        raise NotImplementedError

    @abc.abstractmethod
    def enterMessage(self):
        """Add account information in server"""
        raise NotImplementedError

    @abc.abstractmethod
    def generateKeys(self):
        """Add account information in server"""
        raise NotImplementedError