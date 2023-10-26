
from flask import Flask, request, render_template
from ddd.services.CandidateService import CandidateService
from ddd.repositories.CandidateRepo import CandidateRepo
from ddd.entities.Candidate import Candidate

app = Flask(__name__)
repo = CandidateRepo()
service = CandidateService(repo)

@app.route('/candidate', methods=['GET'])
def get_Candidates():
    entities = [entity for entity in repo.data.values()]
    return render_template('Candidate.html', entities=entities)

@app.route('/Candidate/create', methods=['POST'])
def create_Candidate():
    # Logic to create a Candidate
    entity = Candidate()  # Initialize with proper parameters from request
    service.create(entity)
    return redirect('/candidate')

@app.route('/Candidate/update/<id>', methods=['POST'])
def update_Candidate(id):
    # Logic to update a Candidate
    entity = Candidate()  # Initialize with proper parameters from request
    service.update(id, entity)
    return redirect('/candidate')

@app.route('/Candidate/delete/<id>', methods=['POST'])
def delete_Candidate(id):
    service.delete(id)
    return redirect('/Candidate')
    