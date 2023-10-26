
from flask import Flask, request, render_template
from ddd.services.PythonSystemService import PythonSystemService
from ddd.repositories.PythonSystemRepo import PythonSystemRepo
from ddd.entities.PythonSystem import PythonSystem

app = Flask(__name__)
repo = PythonSystemRepo()
service = PythonSystemService(repo)

@app.route('/pythonsystem', methods=['GET'])
def get_PythonSystems():
    entities = [entity for entity in repo.data.values()]
    return render_template('PythonSystem.html', entities=entities)

@app.route('/PythonSystem/create', methods=['POST'])
def create_PythonSystem():
    # Logic to create a PythonSystem
    entity = PythonSystem()  # Initialize with proper parameters from request
    service.create(entity)
    return redirect('/pythonsystem')

@app.route('/PythonSystem/update/<id>', methods=['POST'])
def update_PythonSystem(id):
    # Logic to update a PythonSystem
    entity = PythonSystem()  # Initialize with proper parameters from request
    service.update(id, entity)
    return redirect('/pythonsystem')

@app.route('/PythonSystem/delete/<id>', methods=['POST'])
def delete_PythonSystem(id):
    service.delete(id)
    return redirect('/PythonSystem')
    