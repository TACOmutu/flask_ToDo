from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
#import sqlite3

app = Flask(__name__)

#データベース設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tasks_db(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    is_done = db.Column(db.Boolean, default=False)


#初期処理
@app.route('/', methods=['GET'])
def index():
    tasks = Tasks_db.query.all()
    return render_template('index.html', tasks=tasks)


#POST専用
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('title')
    if task:
        task = Tasks_db(title=task)
        db.session.add(task)
        db.session.commit()
    
    return redirect(url_for('index'))

#更新
@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle(task_id):
    task = Tasks_db.query.get(task_id)
    #反転をしている
    task.is_done = not task.is_done
    db.session.commit()
    return redirect(url_for('index'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
