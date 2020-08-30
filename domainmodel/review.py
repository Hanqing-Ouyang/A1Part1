from datetime import datetime
from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie

class Review:
    pass
    def __init__(
        self, movie: Movie, review_text: str, rating: int
    ):
        if not isinstance(movie, Movie):
            self._movie= Movie("None",None)
        else:
            self._movie = movie
        if type(review_text) is str:
            self._review_text = review_text.strip()
        else:
            self._review_text =None

        if rating <= 10 and rating >= 1:
            self._rating = rating
        else:
            self._rating = None

        self._timestamp = datetime.now()

    @property
    def movie(self) -> Movie:
        return self._movie

    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie

    @property
    def rating(self) -> int:
        return self._rating

    @rating.setter
    def rating(self, rating):
        if rating <= 10 and rating >= 1:
            self._rating = rating
        else:
            self._rating = None

    @property
    def review_text(self) -> str:
        return self._review_text

    @review_text.setter
    def review_text(self, review_text):
        if type(review_text) is  str:
            self._review_text = review_text.strip()

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if isinstance(timestamp, datetime):
            self._timestamp = timestamp

    def __repr__(self):
        return f'<Review {self._movie}, {self._review_text}, {self._rating}, {self._timestamp}>'

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return (
                other._movie == self._movie and
                other._review_text == self._review_text and
                other._rating == self._rating and
                other._timestamp == self._timestamp
        )

class TestReviewMethods:

    def test_init(self):
        movie = Movie("Moana", 2016)
        review_text = "This movie was very enjoyable."
        rating = 8
        review = Review(movie, review_text, rating)

        print(review.movie)
        print("Review: {}".format(review.review_text))
        print("Rating: {}".format(review.rating))