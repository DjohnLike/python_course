class User:
    def __init__(self):
        self.__name = ''
        self.__passwd = ''

    # Getter`s argument`s data object of class
    @property
    def name(self):
        return self.__name

    @property
    def passwd(self):
        return  self.__passwd

    # Setter`s argument`s data object of class
    @name.setter
    def name(self, name):
        self.__name = name

    @passwd.setter
    def passwd(self, passwd):
        self.__passwd = passwd
