from actor import Actor
from movie import Movie
import json
import logging


class Graph:
    movie_objects = {}
    actor_objects = {}

    def __init__(self):
        self.movie_objects, self.actor_objects = initialize_data({}, {})

    def get_movie_objects(self):
        return self.movie_objects

    def get_actor_objects(self):
        return self.actor_objects


def initialize_data(movie_objects, actor_objects):
    """
    initialize database using actor and movie data from scraped json files
    """
    # logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    data = json.load(open("data.json"))
    logger.info('load data from json and prepare to construct data structure')


    """
    actor objects initialization
    """
    for actor in data[0]:
        actor_name = data[0][actor]['name']
        actor_age = data[0][actor]['age']
        actor_total_grossing = data[0][actor]['total_gross']
        new_actor = Actor(actor_name, actor_age, [], actor_total_grossing)
        actor_objects[actor_name] = new_actor
        string_actor_act_movie = data[0][actor]['movies']
        for actor_movie in string_actor_act_movie:
            movie_existence = 0
            for movie in data[1]:
                if data[1][movie]['name'] == actor_movie:
                    movie_existence = 1
                    if movie not in movie_objects:

                        movie_name = data[1][movie]['name']
                        movie_year = data[1][movie]['year']
                        movie_grossing = data[1][movie]['box_office']

                        new_movie = Movie(movie_name, movie_year, movie_grossing, [])
                        new_movie.attend_actor.append(new_actor)
                        movie_objects[movie_name] = new_movie
                    else:
                        movie_objects[movie].attend_actor.append(new_actor)
                    break
            if movie_existence == 0:
                new_movie = Movie(actor_movie, 0, 0, [])
                new_movie.attend_actor.append(new_actor)
                movie_objects[actor_movie] = new_movie
            new_actor.act_movie.append(movie_objects[actor_movie])
    """
    movie objects initialization
    """
    for movie in data[1]:
        if movie not in movie_objects:
            movie_name = data[1][movie]['name']
            movie_year = data[1][movie]['year']
            movie_grossing = data[1][movie]['box_office']
            new_movie = Movie(movie_name, movie_year, movie_grossing, [])
            for attend_actor in data[1][movie]['actors']:
                new_actor = Actor(attend_actor, 0, [], 0)
                new_movie.attend_actor.append(new_actor)

    return movie_objects, actor_objects

if __name__ == "__main__":
    '''
    data = json.load(open("data.json"))
    
        for actor in data[0]:
        print data[0][actor]['movies']
    

    print data[0]["Bruce Willis"]['movies']
    '''
    graph = Graph()

