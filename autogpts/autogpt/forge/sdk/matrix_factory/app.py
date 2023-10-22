from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'
if __name__ == '__main__':
    app.run()
from flask import jsonify
from flask import jsonify

@app.route('/items', methods=['GET'])
def test():
    if not hasattr(app, 'datastore'):
        app.datastore = []
    return jsonify(app.datastore)
from flask import request

@app.route('/items', methods=['POST'])
def create():
    item = request.json
    app.datastore.append(item)
    return (jsonify(item), 201)

@app.route('/items/<int:index>', methods=['PUT'])
def update(index):
    item = request.json
    app.datastore[index] = item
    return jsonify(item)

@app.route('/items/<int:index>', methods=['DELETE'])
def delete(index):
    item = app.datastore.pop(index)
    return jsonify(item)