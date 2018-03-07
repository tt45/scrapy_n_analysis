from actor import Actor
from movie import Movie
import json
import logging


def initialize_data():
    """
    initialize database using actor and movie data from scraped json files
    """
    actor_data = json.load(open("actor.json"))
    movie_data = json.load(open("movie.json"))
    movie_objects = {}
    actor_objects = {}
    #logger.info('load data from json and prepare to construct data structure')

    for movie in movie_data:
        new_movie = Movie(movie["movieName"], movie["movieYear"], normalize_grossing(movie["movieGrossing"]), [])
        movie_objects[new_movie.name] = new_movie
        for actor in movie["movieStaring"]:

            for available_actor in actor_data:
                if available_actor["actorName"] == actor:

                    if available_actor["actorName"] not in actor_objects:
                        actor_objects[available_actor["actorName"]] = Actor(available_actor["actorName"], normalize_age(available_actor["actorAge"]), [], 0)
                    actor_objects[available_actor["actorName"]].act_movie.append(new_movie)
                    if new_movie.grossing != None:
                        actor_objects[available_actor["actorName"]].total_grossing+=new_movie.grossing

                    new_movie.attend_actor.append(actor_objects[available_actor["actorName"]])
                    break

    for actor in actor_data:
        if actor["actorName"] not in actor_objects:
            actor_objects[actor["actorName"]] = Actor(actor["actorName"], normalize_age(actor["actorAge"]), [], 0)

    return movie_objects, actor_objects


def normalize_grossing(raw_grossing_data):
    """
    :param raw_grossing_data
    :return: this function takes in a string of grossing and analyze them to output a formatted float grossing number
    """
    if raw_grossing_data == None:
        return
    words = raw_grossing_data.split(" ")
    ret_num = 0
    for word in words:
        for char in word:
            if char.isdigit():
                raw_digit_string = ''.join(char for char in word if (char.isdigit() or char=='.'))
                ret_num = float(raw_digit_string)
                break

    if "million" in raw_grossing_data:
        ret_num *= 1000000
    elif "billion" in raw_grossing_data:
        ret_num *= 1000000000
    return ret_num


def normalize_age(raw_age_data):
    """
    :param raw_age_data:
    :return: this function takes a string and return a int for age
    """
    num_string = ''.join(char for char in raw_age_data if char.isdigit())
    return int(num_string)

if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    movie_objects, actor_objects = initialize_data()
    max = 0
    name = ""
    for movie in movie_objects:
        if max < len(movie_objects[movie].get_attend_actor()):
            max = len(movie_objects[movie].get_attend_actor())
            name = movie_objects[movie].get_name()
    print name, max