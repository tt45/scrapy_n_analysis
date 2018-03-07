import graph
import networkx as nx
import matplotlib.pyplot as plt
import operator
import numpy as np

def draw_graph_first(actor_objects):
    '''
    Who are the "hub" actors in your dataset? That is, which actors have the most connections with other actors? Two actors have a connection if they have acted in the same movie together.
    :param actor_objects:
    :return:
    '''
    font = {'family': 'normal',
            'weight': 'bold',
            'size': 5}

    plt.rc('font', **font)
    actor_movie_dict = {}
    for actor in actor_objects:
        actor_movie_dict[actor_objects[actor].get_name()] = len(actor_objects[actor].get_act_movie())
    sorted_actor_dic = sorted(actor_movie_dict.items(), key=operator.itemgetter(1))
    sorted_actor_dic.reverse()
    x_pos = np.arange(10)
    x_name = []
    y_pos = []
    for i in range(10):
        x_name.append(sorted_actor_dic[i][0])
        y_pos.append(sorted_actor_dic[i][1])

    plt.bar(x_pos, y_pos, align='center')
    plt.xlim(xmin=-0.5, xmax=9.5)
    plt.xticks(x_pos, x_name)
    plt.show()

def draw_graph_second(actor_objects):
    '''
    Is there an age group that generates the most amount of money? What does the correlation between age and grossing value look like?
    :param actor_objects:
    :return:
    '''
    x_pos = np.arange(10)
    y_pos = np.zeros((10,), dtype=np.int)
    x_name = ('0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-100')
    for actor in actor_objects:
        y_pos[actor_objects[actor].get_age()//10]+=actor_objects[actor].get_total_grossing()
    plt.bar(x_pos, y_pos, align='center')
    plt.xticks(x_pos, x_name)
    plt.xlim(xmin=0)
    plt.show()


if __name__ == '__main__':
    graph = graph.Graph()
    actor_objects = graph.actor_objects
    movie_objects = graph.movie_objects


    draw_graph_first(actor_objects)
    #draw_graph_second(actor_objects)
