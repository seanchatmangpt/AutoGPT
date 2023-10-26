
from flask import Flask, request, render_template
from ddd.services.InterviewService import InterviewService
from ddd.repositories.InterviewRepo import InterviewRepo
from ddd.entities.Interview import Interview

app = Flask(__name__)
repo = InterviewRepo()
service = InterviewService(repo)

@app.route('/interview', methods=['GET'])
def get_Interviews():
    entities = [entity for entity in repo.data.values()]
    return render_template('Interview.html', entities=entities)

@app.route('/Interview/create', methods=['POST'])
def create_Interview():
    # Logic to create a Interview
    entity = Interview()  # Initialize with proper parameters from request
    service.create(entity)
    return redirect('/interview')

@app.route('/Interview/update/<id>', methods=['POST'])
def update_Interview(id):
    # Logic to update a Interview
    entity = Interview()  # Initialize with proper parameters from request
    service.update(id, entity)
    return redirect('/interview')

@app.route('/Interview/delete/<id>', methods=['POST'])
def delete_Interview(id):
    service.delete(id)
    return redirect('/Interview')
    