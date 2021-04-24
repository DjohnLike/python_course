class Book:
    # Set defaults class arguments
    __default_title = 'Book Title'
    __default_author = []
    __default_description = 'Book Description'
    __default_year = 'Book create year'
    __default_genre = []
    __default_review_list = []

    # Initialisation object of class
    def __init__(self, title=__default_title, author=__default_author,
                 description=__default_description, year=__default_year,
                 genre=__default_genre,):
        # initialisation list`s
        self.__author = []
        self.__genre = []
        self.__review_list = []

        self.__title = title
        self.__author.append(author)
        self.__description = description
        self.__year = year
        self.__genre.append(genre)


    # Static method`s of class


    # Getter`s argument`s data object of class
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def description(self):
        return self.__description

    @property
    def year(self):
        return  self.__year

    @property
    def genre(self):
        return self.__genre

    @property
    def review_list(self):
        return self.__review_list

    # Setter`s argument`s data object of class
    @title.setter
    def title(self, title):
        self.__title = title

    def append_author(self, author):
        self.__author.append(author)

    @description.setter
    def description(self, description):
        self.__description = description

    @year.setter
    def year(self, year):
        self.__year = year

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @review_list.setter
    def review_list(self, review_list):
        self.__review_list = review_list


