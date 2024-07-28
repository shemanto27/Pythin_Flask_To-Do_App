from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Setting up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'     #Setting Up the Database URI
app.config['SQLAlchemy_TRACK_MODIFICATION'] = False               #Disabling SQLAlchemy Track Modifications
db = SQLAlchemy(app)                                              #Initializing SQLAlchemy,sets up the connection between Flask and the database


# Making the table
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)



@app.route('/')
@app.route('/home')
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)