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
                 genre=__default_genre):
        # initialisation list`s
        self.__author = []
        self.__genre = []
        self.__review_list = []

        self.__title = title
        self.__author.append(author)
        self.__description = description
        self.__year = year
        self.__genre.append(genre)

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
        return self.__year

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

    @description.setter
    def description(self, description):
        self.__description = description

    @year.setter
    def year(self, year):
        self.__year = year

    # Classic method`s of object class
    def append_author(self, author):
        """Append Author object to author list book"""
        self.__author.append(author)

    def pop_author(self, author):
        """Pop Author object of author list book
        If Author not instance in list author, return None"""
        if author in self.__author:
            return self.__author.pop(self.__author.index(author))

    def append_review(self, review):
        """Append Review object to review list book"""
        self.__review_list.append(review)

    def pop_review(self, review):
        """Pop Review object of review list book
           If review not instance in list review, return None"""
        if review in self.__review_list:
            return self.__review_list.pop(self.__review_list.index(review))

    def append_genre(self, genre):
        """Append genre to genre list book"""
        self.__genre.append(genre)

    def pop_genre(self, genre):
        """Pop genre of genre list book
           If genre not instance in list review, return None"""
        if genre in self.__genre:
            return self.__genre.pop(self.__genre.index(genre))

