import unittest
import os
import tempfile
from interaction import app
import json

class MyTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_post_get_page(self):
        self.app.post('/actors', data=json.dumps({"name":"Bruce Willis"}),headers={'content-type':'application/json'})
        response = self.app.get('/actors/Bruce%20Willis')
        self.assertEqual(response.status_code, 200)

        self.app.post('/movies', data=json.dumps({"name": "Armageddon"}),headers={'content-type': 'application/json'})
        response = self.app.get('/movies/Armageddon')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/actors?age=20|age=30')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/actors?age=20&age=30')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/movies?year=1920|year=1930')
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/movies?year=1920&year=1930')
        self.assertEqual(response.status_code, 200)

    def test_put_page(self):
        self.app.put('/actors/Bruce%20Willis', data=json.dumps({"age":"10"}),headers={'content-type':'application/json'})
        response = self.app.get('/actors/Bruce%20Willis')
        assert b"10" in response.data

        self.app.put('/movies/Color%20of%20Night', data=json.dumps({"year":"2018"}), headers={'content-type':'application/json'})
        response = self.app.get('/movies/Color%20of%20Night')
        assert b"2018" in response.data



    def test_delete_page(self):
        self.app.delete('/actors/Bruce%20Willis')
        response = self.app.get('/actors/Bruce%20Willis')
        assert b"562709189" not in response.data

        self.app.delete('/movies/North')
        response = self.app.get('/movies/North')
        assert b"https://en.wikipedia.org/wiki/North_(1994_film)" not in response.data

if __name__ == '__main__':
    unittest.main()

