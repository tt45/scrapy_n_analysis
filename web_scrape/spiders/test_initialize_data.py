from unittest import TestCase
import main
import unittest

class TestInitialize_data(TestCase):
    def test_graph(self):
        movie_objects, actor_objects = main.initialize_data()
        self.assertEqual(movie_objects["The Hard Way"].get_name(), "The Hard Way")
        self.assertEqual(movie_objects["The Hard Way"].get_grossing(), 65595485.0)
        self.assertEqual(movie_objects["The Hard Way"].get_year(), 1993)
        self.assertEqual(actor_objects["Donnie Yen"].get_name(), "Donnie Yen")
        self.assertEqual(actor_objects["Donnie Yen"].get_age(), 54)
        self.assertEqual(actor_objects["Donnie Yen"].get_act_movie(), [])
if __name__ == '__main__':
    unittest.main()