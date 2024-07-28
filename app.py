from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Setting up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'     #Setting Up the Database URI
app.config['SQLAlchemy_TRACK_MODIFICATION'] = False               #Disabling SQLAlchemy Track Modifications
db = SQLAlchemy(app)                                              #Initializing SQLAlchemy,sets up the connection between Flask and the database


# Making the table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))
    complete = db.Column(db.Boolean)



@app.route('/')
@app.route('/home')
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

@app.route('/add', methods=["POST"])
def add():
    task = request.form.get("task")
    new_todo = Todo(task=task, complete= False) #A new Todo object is created
    db.session.add(new_todo) #adds the new to-do item to the current database session
    db.session.commit() #saving the new to-do item to the database
    return redirect(url_for("home"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)