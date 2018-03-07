from unittest import TestCase
import graph
import unittest

class MyTestCase(unittest.TestCase):


    def test_something(self):
        self.assertEqual(movie_objects["Striking Distance"].get_name(), "Striking Distance")
        self.assertEqual(movie_objects["Striking Distance"].get_grossing(), 24107867)
        self.assertEqual(movie_objects["Striking Distance"].get_year(), 1993)
        self.assertEqual(actor_objects["David Dukes"].get_name(), "David Dukes")
        self.assertEqual(actor_objects["David Dukes"].get_age(), 55)
        self.assertEqual(actor_objects["David Dukes"].get_act_movie(), [])




if __name__ == '__main__':
    graph = graph.Graph()
    movie_objects, actor_objects = graph.get_movie_objects(), graph.get_actor_objects()
    unittest.main()
