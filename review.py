import datetime


class Review:

    __default_max_value = 10

    # Initialisation object of class
    def __init__(self, user, rating, description):
        self.__user = user
        self.__rating = Review.__rating_validate(rating)
        self.__description = description
        self.__date_of_create = datetime.datetime.now()

    # Override magic methods
    def __repr__(self):
        return f'<{self.__user}: {self.__description}>'

    # Getter`s argument`s data object of class
    @property
    def user(self):
        return self.__user

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
    @user.setter
    def user(self, author):
        self.__user = author

    @rating.setter
    def rating(self, rating):
        self.__rating = Review.__rating_validate(rating)

    @description.setter
    def description(self, description):
        self.__description = description

    # ClassMethods of class
    @classmethod
    def set_max_value(cls, value):
        cls.__default_max_value = value

    # StaticMethods of class
    @staticmethod
    def __rating_validate(value):
        """Checking the input value for type int or float
           round value to 0 if value less 0, or round value to __default_max_value if
           value more __default_max_value. If value not int or float raise ValueError"""
        if isinstance(value, int) or isinstance(value, float):
            if value < 0:
                return 0
            elif value > Review.__default_max_value:
                return Review.__default_max_value
            return value
        else:
            raise ValueError('The value must be int or float')
