from book import Book
from author import Author
from review import Review


def main():
    book = Book('My book', 'Ivan', 'This`s book about of our life', '1992', 'autobiography', 1)
    review = Review('Ivan', 10, 'Very interesting')
    review_1 = Review('Janis', 10, 'Interesting')
    review_2 = Review('Elise', 6, 'Hmm...')

    book.append_review(review)
    book.append_review(review_1)
    book.append_review(review_2)
    print(book.review_list)
    print(book.rating_of_the_book)

    book.pop_review(review_2)
    print(book.review_list)

    print(book.rating_of_the_book)

if __name__ == '__main__':
    main()
