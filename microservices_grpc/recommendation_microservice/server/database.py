from recommendpb.recommend_pb2 import BookGenre, BookRecommendation

books_by_genre = {
    BookGenre.SCIENCE_FICTION: [
        BookRecommendation(book_id="1984", title="Nineteen Eighty Four"),
        BookRecommendation(book_id="3498", title="Dune"),
        BookRecommendation(book_id="1101", title="The time machine"),
        BookRecommendation(book_id="1019", title="Frankenstein")
    ],
    BookGenre.FANTASY: [
        BookRecommendation(book_id="8493", title="The lord of the rings"),
        BookRecommendation(book_id="0912", title="A game of thrones"),
    ],
    BookGenre.MYSTERY: [
        BookRecommendation(book_id="6543", title="Gone girl"),
        BookRecommendation(
            book_id="7543", title="The girl with the dragon tatoo"),
        BookRecommendation(book_id="0934", title="The hound of baskervilles"),
    ],
    BookGenre.ROMANCE: [
        BookRecommendation(book_id="9043", title="The notebook"),
        BookRecommendation(book_id="2482", title="Prbook_ide and Prejudice"),
    ],
    BookGenre.BIOGRAPHY: [
        BookRecommendation(book_id="3894", title="The diary of a young girl"),
        BookRecommendation(book_id="3423", title="Satya ke prayog"),
        BookRecommendation(book_id="0934", title="Long walk to freedom"),
    ],
}
