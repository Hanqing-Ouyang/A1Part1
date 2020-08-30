from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.user import User, Review, Movie
from domainmodel.movie import TestMovieMethods
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

def main():

    movie = Movie("Moana", 2016)
    review_text = "This movie was very enjoyable."
    rating = 8
    review = Review(movie, review_text, rating)
    review2 = Review("Moana", " Moana ", 0)
    print(review2)
    assert repr(review2.movie)== "<Movie None, None>"
    assert repr(review2.review_text) == "'Moana'"
    assert repr(review2.rating) == "None"

    review3= Review(23, 23, -5)
    print(review3)
    assert repr(review3.movie) == "<Movie None, None>"
    assert repr(review3.review_text) == "None"
    assert repr(review3.rating) == "None"
    print(movie)
    assert repr(movie) == "<Movie Moana, 2016>"
    print(review.movie)
    assert repr(review.movie) == "<Movie Moana, 2016>"
    print("Review: {}".format(review.review_text))
    assert repr(review.review_text) == "'This movie was very enjoyable.'"
    assert type(review_text)== str

    print("Rating: {}".format(review.rating))
    assert repr(review.rating) == "8"
    print(review.timestamp)
    #assert repr(review.datetime)


if __name__ == "__main__":
        main()