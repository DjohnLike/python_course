class Book:
    # Set defaults class arguments
    __default_title = 'Book Title'
    __default_author = []
    __default_description = 'Book Description'
    __default_year = 'Book create year'
    __default_genre = []
    __default_review_list = []

    # Initialisation object of class
    def __init__(self, title, author,
                 description, year,
                 genre, edition):
        # Initialisation list`s
        self.__author = []
        self.__genre = []
        self.__review_list = []
        # Initialisation arguments data objet
        self.__title = title
        self.__author.append(author)
        self.__description = description
        self.__year = year
        self.__genre.append(genre)
        self.__edition = edition
        self.__rating_of_the_book = 0

    # Override magic methods
    def __eq__(self, other):
        if self.__author == other.__author and self.__title == other.__title and \
                self.__year == other.__year and self.__edition == other.__edition:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.__title}, {self.__author}, {self.__year}, {self.edition}'

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

    @property
    def edition(self):
        return self.__edition

    @property
    def rating_of_the_book(self):
        return float(f'{self.__rating_of_the_book:.3}')

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

    @edition.setter
    def edition(self, edition):
        self.__edition = edition

    # Classic method`s of object class

    def __average_rating(self):
        self.__rating_of_the_book = 0
        for review in self.__review_list:
            self.__rating_of_the_book += review.rating
        self.__rating_of_the_book /= len(self.__review_list)

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
        self.__average_rating()

    def pop_review(self, review):
        """Pop Review object of review list book
           If review not instance in list review, return None"""
        if review in self.__review_list:
            self.__review_list.pop(self.__review_list.index(review))
            self.__average_rating()

    def append_genre(self, genre):
        """Append genre to genre list book"""
        self.__genre.append(genre)

    def pop_genre(self, genre):
        """Pop genre of genre list book
           If genre not instance in list review, return None"""
        if genre in self.__genre:
            return self.__genre.pop(self.__genre.index(genre))
