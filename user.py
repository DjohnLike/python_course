class User:
    def __init__(self, name):
        self.__name = name

    # Getter`s argument`s data object of class
    @property
    def name(self):
        return self.__name

    # Setter`s argument`s data object of class
    @name.setter
    def name(self, name):
        self.__name = name