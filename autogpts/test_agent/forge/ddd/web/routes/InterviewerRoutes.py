
from flask import Flask, request, render_template
from ddd.services.InterviewerService import InterviewerService
from ddd.repositories.InterviewerRepo import InterviewerRepo
from ddd.entities.Interviewer import Interviewer

app = Flask(__name__)
repo = InterviewerRepo()
service = InterviewerService(repo)

@app.route('/interviewer', methods=['GET'])
def get_Interviewers():
    entities = [entity for entity in repo.data.values()]
    return render_template('Interviewer.html', entities=entities)

@app.route('/Interviewer/create', methods=['POST'])
def create_Interviewer():
    # Logic to create a Interviewer
    entity = Interviewer()  # Initialize with proper parameters from request
    service.create(entity)
    return redirect('/interviewer')

@app.route('/Interviewer/update/<id>', methods=['POST'])
def update_Interviewer(id):
    # Logic to update a Interviewer
    entity = Interviewer()  # Initialize with proper parameters from request
    service.update(id, entity)
    return redirect('/interviewer')

@app.route('/Interviewer/delete/<id>', methods=['POST'])
def delete_Interviewer(id):
    service.delete(id)
    return redirect('/Interviewer')
    