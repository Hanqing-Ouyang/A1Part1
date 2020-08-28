import csv
from typing import List
from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Director):
            return False
        return (
                other.__director_full_name == self.__director_full_name
        )
        pass

    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name
        pass

    def __hash__(self):
        return hash(self.__director_full_name)
        pass

class Genre:
    pass

    def __init__(
            self, gname: str,
    ):
        self._gname: str = gname

    @property
    def genre_name(self) -> str:
        return self._gname

    def __repr__(self):
        if not self._gname:
            return f'<Genre None>'
        else:
            return f'<Genre {self._gname}>'

    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False
        return (
                other._gname == self._gname
        )

    def __lt__(self, other):
        return self._gname < other._gname

    def __hash__(self):
        return hash(self._gname)



class Actor:
    pass

    def __init__(
            self, actor_full_name: str,
    ):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self._actor_full_name=None
        else:
            self._actor_full_name=actor_full_name.strip()

        self._colleagues = []

    @property
    def actor_full_name(self):
        return self._actor_full_name

    @actor_full_name.setter
    def actor_full_name(self,value):
        if value == "" or type(value) is not str:
            self._actor_full_name = None
        else:
            self._actor_full_name=value.strip()

    def __repr__(self) -> str:
        return f'<Actor {self._actor_full_name}>'

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return (
                other._actor_full_name == self._actor_full_name
        )

    def __lt__(self, other:'Actor'):
        if not isinstance(other, Actor):
            return False
        else:
            return self._actor_full_name < other._actor_full_name

    def __hash__(self):
        return hash(self._actor_full_name)

    def add_actor_colleague(self, colleague:'Actor'):
        if isinstance(colleague, Actor):
            self._colleagues.append(colleague)
            colleague._colleagues.append(self)
        else:
            return False

    def check_if_this_actor_worked_with(self, colleague:'Actor') -> bool:
        if not isinstance(colleague, Actor):
            return False
        else:
            return colleague in self._colleagues


class Movie:
    pass

    def __init__(
            self, title:str,description:str,director:str,runtime_minutes:int
    ):
        self._title: str=title
        self._description: str=description
        self._director: str=director
        self._actors: List[Actor] = list()
        self._genres: List[Genre] = list()
        self._runtime_minutes: int= runtime_minutes

    def __init__(
            self, title:str, year:int
    ):
        self._title: str=title
        self._year: int =year
        self._actors: List[Actor] = list()
        self._genres: List[Genre] = list()


    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title):
        self._title=title.strip()

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, year):
        if year >=1900:
            self._year = year.strip()
        else:
            print("please enter a correct year")


    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description):
        self._description=description.strip()

    @property
    def director(self) -> str:
        return self._director

    @director.setter
    def director(self, director):
        self._director = director

    @property
    def runtime_minutes(self) ->int:
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self,runtime_minutes):
        try:
            val = int(runtime_minutes)
            if val < 0:  # if not a positive int print message and ask for input again
                print("Sorry, input must be a positive integer, try again")
            else:
                self._runtime_minutes = runtime_minutes
        except ValueError:
            print("That's not an int!")

    @property
    def actors(self) -> list():
        return self._actors

    @actors.setter
    def actors(self, actors):
        self._actors = actors

    @property
    def genres(self) -> list():
        return self._genres

    @genres.setter
    def genres(self, genres):
        self._genres = genres

    def __repr__(self):
        return f'<Movie {self._title}, {self._year}>'

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return (
                other._title == self._title and
                other._year == self._year
        )

    def __lt__(self, other):
        return ((self._title, self._year)< (other._title, other._year))

    def __hash__(self):
        return hash(self._title) ^ hash(self._year)

    def add_actor(self,actor:Actor):
        self._actors.append(actor)

    def remove_actor(self,actor:Actor):
        if actor in self._actors:
            self._actors.remove(actor)

    def add_genre(self,genre:Genre):
        self._genres.append(genre)

    def remove_genre(self,genre:Genre):
        if genre in self._genres:
            self._genres.remove(genre)




class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name


    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                #print(f"Movie {index} with title: {title}, release year {release_year}")
                index += 1

    @property
    def dataset_of_movies(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            index = 0
            movies=[]
            for row in movie_file_reader:
                new_movie=Movie(row['Title'],int(row['Year']))
                movies.append(new_movie)
                index += 1
            return list(movies)

    @property
    def dataset_of_actors(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            index = 0
            actors= list()
            for row in movie_file_reader:
                for a in row['Actors'].split(","):
                    temp=Actor(a.strip())
                    if temp not in actors:
                        actors.append(temp)
                index += 1
            return list(actors)

    @property
    def dataset_of_directors(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            index = 0
            directors = set()
            for row in movie_file_reader:
                directors.add(Director(row['Director']))
                index += 1
            return list(directors)

    @property
    def dataset_of_genres(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            index = 0
            genres = list()
            for row in movie_file_reader:
                for g in row['Genre'].split(","):
                    temp=Genre(g.strip())
                    if temp not in genres:
                        genres.append(temp)
                index += 1
            return list(genres)




