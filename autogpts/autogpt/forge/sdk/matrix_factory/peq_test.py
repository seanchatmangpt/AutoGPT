import os

from peq import Peq  # Ensure that the Peq class is available

if os.path.exists("demo_app.py"):
    os.remove("demo_app.py")

app = """from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run()"""

# Initialize the Peq class with the demo_app.py
peq = Peq("demo_app.py", app)

# Replace the 'hello' function to be the 'read' function for our CRUD API
peq["read"] = '''
from flask import jsonify

@app.route('/items', methods=['GET'])
def read():
    if not hasattr(app, 'datastore'):
        app.datastore = []  # Initialize an in-memory datastore
    return jsonify(app.datastore)
'''
#
# # 2. Create a new item
peq["create"] = '''
from flask import request

@app.route('/items', methods=['POST'])
def create():
    item = request.json
    app.datastore.append(item)
    return jsonify(item), 201
'''
#
peq["update"] = '''
@app.route('/items/<int:index>', methods=['PUT'])
def update(index):
    item = request.json
    app.datastore[index] = item
    return jsonify(item)
'''
#
peq["delete"] = '''
@app.route('/items/<int:index>', methods=['DELETE'])
def delete(index):
    item = app.datastore.pop(index)
    return jsonify(item)
'''

peq["add_mock_items"] = '''
from flask import jsonify

@app.route('/add_mock_items', methods=['POST'])
def add_mock_items():
    if not hasattr(app, 'datastore'):
        app.datastore = []  # Initialize an in-memory datastore if not already present

    mock_items = [
        {"id": 1, "name": "item1", "description": "This is item 1"},
        {"id": 2, "name": "item2", "description": "This is item 2"},
        {"id": 3, "name": "item3", "description": "This is item 3"}
    ]

    app.datastore.extend(mock_items)
    return jsonify(mock_items), 201
'''

# Save these changes back to the demo_app.py
# The 'demo_app.py' now has been transformed to a CRUD API

# You can now run the modified demo_app.py to start the CRUD API
