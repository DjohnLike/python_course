from book import Book
from author import Author
from review import Review


def main():
    book = Book('My book', 'Ivan', 'This`s book about of our life', '1992', 'autobiography', 1)
    book_1 = Book('My book', 'Ivan', 'This`s book about of our life', '1992', 'autobiography', 1)

    print(book.author)

    print(book == book_1)

    print(book)

if __name__ == '__main__':
    main()
