from flask import Flask, render_template, request, redirect
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


@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST':
        todo_name = request.form['name']
        todo_des = request.form['des']
        data = TodoL(name=todo_name, des=todo_des)
        db.session.add(data)
        db.session.commit()

    alltodo = TodoL.query.all()
    return render_template('todo.html',alltodo=alltodo)

@app.route('/delete/<int:sno>')
def delete(sno):
    del_data = TodoL.query.filter_by(sno=sno).first()
    db.session.delete(del_data)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    upd_data = TodoL.query.get_or_404(sno)  # Retrieve the existing task based on sno
    
    if request.method == 'POST':
        upd_data.name = request.form['name']  # Update the name
        upd_data.des = request.form['des']    # Update the description
        db.session.commit()                   # Commit the changes
        return redirect('/')
    
    return render_template('update.html', todo=upd_data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5555, debug=True)