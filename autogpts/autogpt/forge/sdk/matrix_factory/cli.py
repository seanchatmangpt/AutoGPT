import argparse
from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from faker import Faker

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contracts.db"
db = SQLAlchemy(app)


class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Draft")
    signature_timestamp = db.Column(db.DateTime, nullable=True)

    markups = db.relationship("Markup", backref="contract", lazy=True)


class Markup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(150), nullable=False)
    contract_id = db.Column(db.Integer, db.ForeignKey("contract.id"))


def add_mock_contract(num=1):
    fake = Faker()
    for _ in range(num):
        contract_content = fake.text()
        contract = Contract(content=contract_content, status="Draft")

        markup_content = fake.sentence()
        markup_author = fake.name()

        markup = Markup(content=markup_content, author=markup_author, contract=contract)

        db.session.add(contract)
        db.session.add(markup)

    db.session.commit()


def main():
    parser = argparse.ArgumentParser(
        description="CLI to add mock contracts to the database."
    )
    parser.add_argument(
        "--number", type=int, default=1, help="Number of mock contracts to add."
    )
    args = parser.parse_args()

    with app.app_context():
        db.create_all()
        add_mock_contract(args.number)
        print(f"Added {args.number} mock contracts to the database.")


if __name__ == "__main__":
    main()
