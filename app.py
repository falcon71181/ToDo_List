from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class TodoL(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    des = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.name}"


@app.route('/')
def home():
    data = TodoL.query.all()
    return render_template('todo.html',data=data)

@app.route('/show')
def show():
    return 'SUCCESS'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)