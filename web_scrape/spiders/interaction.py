from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
import json
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

data = json.load(open("data.json"))
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/actors/<string:actor_name>', methods=['GET'])
def get_actor_request(actor_name):
    actor_name = actor_name.replace("_", " ")
    if actor_name not in data[0]:
        return "actor is not in database"
    return jsonify(data[0][actor_name])

@app.route('/movies/<string:movie_name>', methods=['GET'])
def get_movie_request(movie_name):
    movie_name = movie_name.replace("_", " ")
    if movie_name not in data[1]:
        return "movie is not in database"
    return jsonify(data[1][movie_name])

@app.route('/actors', methods=['GET'])
def get_actor_request_additional():
    query_string = request.query_string
    actor_list = []
    if '|' in query_string:
        args = query_string.split('|')
        keys = []
        values = []
        for arg in args:
            if '=' not in arg:
                abort(404)
            key, value = arg.split('=')
            if key != "name" and key != "age":
                abort(404)
            keys.append(key)
            if key == "age":
                value = int(value)
            if key == "name":
                value = value.replace("%20", " ")
            values.append(value)
        print keys, values
        for actor in data[0]:
            if data[0][actor][keys[0]] == values[0] or data[0][actor][keys[1]] == values[1]:
                actor_list.append(data[0][actor])

    elif '&' in query_string:
        args = query_string.split('&')
        keys = []
        values = []
        for arg in args:
            if '=' not in arg:
                abort(404)
            key, value = arg.split('=')
            if key != "name" and key != "age":
                abort(404)
            keys.append(key)
            if key == "age":
                value = int(value)
            if key == "name":
                value = value.replace("%20", " ")
            values.append(value)

        for actor in data[0]:
            if data[0][actor][keys[0]] == values[0] and data[0][actor][keys[1]] == values[1]:
                actor_list.append(data[0][actor])

    return jsonify(actor_list)

@app.route('/movies', methods=['GET'])
def get_movie_request_additional():
    query_string = request.query_string
    movie_list = []
    if '|' in query_string:
        args = query_string.split('|')
        keys = []
        values = []
        for arg in args:
            if '=' not in arg:
                abort(404)
            key, value = arg.split('=')
            if key != "name" and key != "year":
                abort(404)
            keys.append(key)
            if key == "year":
                value = int(value)
            values.append(value)

        for movie in data[1]:
            if data[1][movie][keys[0]] != values[0] and data[1][movie][keys[1]] != values[1]:
                movie_list.append(data[1][movie])

    elif '&' in query_string:
        args = query_string.split('&')
        keys = []
        values = []
        for arg in args:
            if '=' not in arg:
                abort(404)
            key, value = arg.split('=')
            if key != "name" and key != "year":
                abort(404)
            keys.append(key)
            if key == "year":
                value = int(value)
            values.append(value)

        for movie in data[1]:
            if data[1][movie][keys[0]] != values[0] or data[1][movie][keys[1]] != values[1]:
                movie_list.append(data[1][movie])

    return jsonify(movie_list)

@app.route('/actors/<string:actor_name>', methods=['PUT'])
def put_actor_request(actor_name):
    actor_name = actor_name.replace("_", " ")
    data[0][actor_name]['age'] = request.json.get('age', data[0][actor_name]['age'])
    data[0][actor_name]['total_gross'] = request.json.get('total', data[0][actor_name]['total_gross'])
    data[0][actor_name]['movies'] = request.json.get('movies', data[0][actor_name]['movies'])
    return jsonify(data[0][actor_name])

@app.route('/movies/<string:movie_name>', methods=['PUT'])
def put_movie_request(movie_name):
    #movie_name = movie_name.replace("_", " ")
    data[1][movie_name]['box_office'] = request.json.get('box_office', data[1][movie_name]['box_office'])
    data[1][movie_name]['year'] = request.json.get('year', data[1][movie_name]['year'])
    data[1][movie_name]['actors'] = request.json.get('actors', data[1][movie_name]['actors'])
    return jsonify(data[1][movie_name])

@app.route('/actors', methods=['POST'])
def post_actor_request():
    name = request.json['name']
    name = {
        "json_class": "Actor",
        "name": name,
        "age": 0,
        "total_gross": 0,
        "movies": []
    }
    actor_name = request.json['name']
    data[0][actor_name] = name
    return jsonify(data[0][actor_name]), 201

@app.route('/actors', methods=['POST'])
def post_movie_request():
    name = request.json['name']
    name = {
        "json_class": "Movie",
        "name": name,
        "wiki_page": "",
        "box_office": 0,
        "year": 0,
        "actors": []
    }
    movie_name = request.json['name']
    data[1][movie_name] = name
    return jsonify(data[1][movie_name]), 201

@app.route('/actors/<string:actor_name>', methods=['DELETE'])
def delete_actor_request(actor_name):
    actor_name = actor_name.replace("_", " ")
    del data[0][actor_name]
    return jsonify({'result': True})

@app.route('/movies/<string:movie_name>', methods=['DELETE'])
def delete_movie_request(movie_name):
    movie_name = movie_name.replace("_", " ")
    del data[1][movie_name]
    return jsonify({'result': True})

if __name__ == "__main__":
    app.run()