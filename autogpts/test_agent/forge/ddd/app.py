
from flask import Flask, render_template
from web.routes.InterviewRoutes import app as interview_app
from web.routes.CandidateRoutes import app as candidate_app
from web.routes.InterviewerRoutes import app as interviewer_app
from web.routes.PythonSystemRoutes import app as pythonsystem_app

app = Flask(__name__)

app.register_blueprint(interview_app, url_prefix='/interview')
app.register_blueprint(candidate_app, url_prefix='/candidate')
app.register_blueprint(interviewer_app, url_prefix='/interviewer')
app.register_blueprint(pythonsystem_app, url_prefix='/pythonsystem')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    