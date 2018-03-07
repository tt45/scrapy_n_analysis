
import main
import sys
import operator
import logging

if __name__ == '__main__':
    """
    run this function and user can interact with the database for information
    """
    logger = logging.getLogger(__name__)
    movie_objects, actor_objects = main.initialize_data()
    welcome_message = '''
        Query starts here. Type in number for relative question
        1. Find how much a movie has grossed
        2. List which movies an actor has worked in
        3. List which actors worked in a movie
        4. List the top X actors with the most total grossing value
        5. List the oldest X actors
        6. List all the movies for a given year
        7. List all the actors for a given year
                    '''
    print welcome_message
    user_choice = input()
    logger.info('start receive input and do relative functions')
    if user_choice == 1:
        movie_name = raw_input('Enter the movie name ')
        print "The movie has grossed",movie_objects[movie_name].get_grossing()
    elif user_choice == 2:
        actor_name = raw_input('Enter the actor name ')
        print "The actor has acted "
        for movie in actor_objects[actor_name].get_act_movie():
            print movie.get_name()
    elif user_choice == 3:
        movie_name = raw_input('Enter the movie name')
        print "Actors worked in this movie"
        for actor in movie_objects[movie_name].attend_actor:
            print actor.name
    elif user_choice == 4:
        num = input('How many actors ')
        actor_dic = {}
        for actor in actor_objects:
            actor_dic[actor_objects[actor].get_name()] = actor_objects[actor].get_total_grossing()
        sorted_actor_dic = sorted(actor_dic.items(), key=operator.itemgetter(1))
        sorted_actor_dic.reverse()
        for i in range(num):
            print sorted_actor_dic[i][0], sorted_actor_dic[i][1]
    elif user_choice == 5:
        num = input('How many actors ')
        actor_dic = {}
        for actor in actor_objects:
            actor_dic[actor_objects[actor].get_name()] = actor_objects[actor].get_age()
        sorted_actor_dic = sorted(actor_dic.items(), key=operator.itemgetter(1))
        sorted_actor_dic.reverse()
        for i in range(num):
            print sorted_actor_dic[i][0], sorted_actor_dic[i][1]
    elif user_choice == 6:
        year = raw_input('Enter the year ')
        for movie in movie_objects:
            if year in movie_objects[movie].get_year():
                print movie_objects[movie].get_name()
    elif user_choice == 7:
        age = input('Enter the actor\'s age ')
        for actor in actor_objects:
            if age == actor_objects[actor].age:
                print actor_objects[actor].get_name()
    else:
        print "False input"
        exit
