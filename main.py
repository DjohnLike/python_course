from book import Book
from author import Author
from review import Review


def main():
    author_1 = Author('Ivan', '29')
    book_1 = Book('My Book', author_1, 'The book about computers', '2017', 'Computer since', 1)
    book_2 = Book('My Book N2', author_1, 'The book about computers', '2021', 'Computer since', 2)

    review_1 = Review('User 1', 8, 'This book about computers')
    review_2 = Review('User 2', 3, 'This book not interesting')
    review_3 = Review('User 3', 5, 'Description review - 1')
    review_4 = Review('User 4', 7, 'Description review - 2')

    book_1.append_review(review_1)
    book_1.append_review(review_2)
    book_2.append_review(review_3)
    book_2.append_review(review_4)

    author_1.append_book(book_1)
    author_1.append_book(book_2)

    print(author_1.rating)
    print(book_1.review_list)
    print(book_1.count_review)


if __name__ == '__main__':
    main()
