from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from loguru import logger

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contracts.db"
db = SQLAlchemy(app)

logger.add("app.log", rotation="50 MB")


class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Draft")
    signature_timestamp = db.Column(db.DateTime, nullable=True)


class Markup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(150), nullable=False)
    contract_id = db.Column(db.Integer, db.ForeignKey("contract.id"))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form["content"]
        new_contract = Contract(content=content)
        db.session.add(new_contract)
        db.session.commit()
        return redirect("/")

    contracts = Contract.query.all()
    return render_template("contract_management.html", contracts=contracts)


@app.route("/contract/<int:id>/sign", methods=["POST"])
def sign_contract(id):
    contract = Contract.query.get(id)
    contract.status = "Signed"
    db.session.commit()
    return redirect("/")


@app.route("/contract/<int:id>/add_markup", methods=["POST"])
def add_markup(id):
    contract = Contract.query.get(id)
    content = request.form["markup_content"]
    author = request.form["markup_author"]
    markup = Markup(content=content, author=author, contract_id=id)
    db.session.add(markup)
    db.session.commit()
    return redirect("/")


@app.route("/contract/<int:id>/delete", methods=["POST"])
def delete_contract(id):
    contract = Contract.query.get(id)
    db.session.delete(contract)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
