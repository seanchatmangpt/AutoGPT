# Import the necessary modules
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Create the database model
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)

# Create the form for creating entries
@app.route('/create', methods=['GET', 'POST'])
def create_entry():
    if request.method == 'POST':
        # Get the data from the form
        name = request.form['name']
        age = request.form['age']
        
        # Create a new entry in the database
        entry = Entry(name=name, age=age)
        db.session.add(entry)
        db.session.commit()
        
        # Redirect to the home page
        return redirect('/')
    
    # Render the template for creating entries
    return render_template('create.html')

# Create the form for updating entries
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_entry(id):
    # Get the entry from the database
    entry = Entry.query.get_or_404(id)
    
    if request.method == 'POST':
        # Update the entry with the data from the form
        entry.name = request.form['name']
        entry.age = request.form['age']
        
        # Save the changes to the database
        db.session.commit()
        
        # Redirect to the home page
        return redirect('/')
    
    # Render the template for updating entries
    return render_template('update.html', entry=entry)

# Run the application
if __name__ == '__main__':
    app.run()