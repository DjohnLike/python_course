class Author:
    # Initialisation object of class
    def __init__(self, name, age):
        self.__books_list = []
        self.__review_list = []
        self.__name = name
        self.__age = age
        self.__rating = 0

    # Getter`s argument`s data object of class
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def list_of_the_books(self):
        return self.__books_list

    @property
    def rating(self):
        return self.__rating

    # Setter`s argument`s data object of class
    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    # Classic method`s of object class
    def __average_rating(self):
        """Calculates the average of the author's rating based
        on the rating values books in the list of author books"""
        self.__rating = 0
        for book in self.__books_list:
            self.__rating += book.rating
        self.__rating /= len(self.__books_list)

    def append_book(self, book):
        self.__books_list.append(book)
        self.__average_rating()

    def pop_book(self, book):
        if book in self.__books_list:
            self.__books_list.pop(self.__books_list.index(book))
            self.__average_rating()
