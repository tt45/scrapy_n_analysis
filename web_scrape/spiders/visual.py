import networkx as nx
import matplotlib.pyplot as plt
import main


def draw_graph(movie_name):
    '''
    draw a graph structure given movie name
    :param movie_name:
    :return:
    '''
    movie_object = movie_objects[movie_name]
    G = nx.Graph()
    movie_name = movie_object.get_name()+ " "+movie_object.get_year()
    G.add_node(movie_name)

    for actor in movie_object.get_attend_actor():
        actor_name = actor.get_name()+" "+str(actor.get_age())
        G.add_node(actor_name)
        G.add_edge(movie_name, actor_name)


    nx.draw(G, with_labels=True)
    plt.savefig("path_graph_cities.png")
    plt.show()



if __name__ == '__main__':
    movie_objects, actor_objects = main.initialize_data()
    draw_graph("Guardians of the Galaxy Vol. 2")