import datetime


class Review:
    def __init__(self, author, rating, description):
        self.__author = author
        self.__rating = Review.__rating_validate(rating)
        self.__description = description
        self.__date_of_create = datetime.datetime.now()

    # Getter`s argument`s data object of class
    @property
    def author(self):
        return self.__author

    @property
    def rating(self):
        return self.__rating

    @property
    def description(self):
        return self.__description

    @property
    def date_of_create(self):
        return self.__date_of_create

    # Setter`s argument`s data object of class
    @author.setter
    def author(self, author):
        self.__author = author

    @rating.setter
    def rating(self, rating):
        self.__rating = Review.__rating_validate(rating)

    @description.setter
    def description(self, description):
        self.__description = description

    # StaticMethods of class
    @staticmethod
    def __rating_validate(value):
        """Checking the input value for type int or float
           round value to 0 if value less 0, or round value to 10 if
           value more 10. If value not int or float raise ValueError"""
        if isinstance(value, int) or isinstance(value, float):
            if value < 0:
                return 0
            elif value > 10:
                return 10
            return value
        else:
            raise ValueError('The value must be int or float')
