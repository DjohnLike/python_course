from book import Book
from author import Author
from review import Review


def main():
    book = Book('My book', 'Ivan', 'This`s book about of our life', '1992', ['autobiography', 'comedy'])

    print(book.author)

    book.append_author('Lolita')

    print(book.author)

    book.pop_author('Ivan')

    print(book.author)

    book.pop_author('Lolita')

    print(book.author)

if __name__ == '__main__':
    main()
