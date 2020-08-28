from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.user import User, Review, Movie
from domainmodel.movie import TestMovieMethods
from domainmodel.actor import Actor
from domainmodel.director import Director

def main():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    print(f'number of unique movies: {len(movie_file_reader.dataset_of_movies)}')
    assert len(movie_file_reader.dataset_of_movies)== 1000
    print(f'number of unique actors: {len(movie_file_reader.dataset_of_actors)}')
    assert len(movie_file_reader.dataset_of_actors) == 1985

    print(f'number of unique directors: {len(movie_file_reader.dataset_of_directors)}')
    assert len(movie_file_reader.dataset_of_directors) ==644
    print(f'number of unique genres: {len(movie_file_reader.dataset_of_genres)}')
    assert len(movie_file_reader.dataset_of_genres) ==20

    print(movie_file_reader.dataset_of_movies)
    print(movie_file_reader.dataset_of_actors)
    print(movie_file_reader.dataset_of_directors)
    print(movie_file_reader.dataset_of_genres)


if __name__ == "__main__":
    main()