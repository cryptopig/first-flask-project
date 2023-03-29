from datetime import datetime
from flask import Flask, render_template, flash, url_for, redirect
app = Flask(__name__)
from forms import RegistrationForm, LoginForm

from flask_sqlalchemy import SQLAlchemy


app.config["SECRET_KEY"] = 'ab9c32a070313d1343395f1cc4d5a669'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'

db = SQLAlchemy(app)

# defines the user object and its attributes
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Posts', backref = 'author', lazy = True)
    # backref allows program basically adds an author attribute
    # lazy = True means that SQLAlchemy will load all data at once, so the post attribute can get all posts created by a user at once

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
# defines a post object and its attributes  
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) # checks id of the user who authored the post. It's non-nullable becuse all posts must have an author.

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"




# list of dicts
posts = [
    {
        'author': 'Hog Rider',
        'title': 'title 1',
        'content': 'hello',
        'date': '21 march 2023'
    },
    {
        'author': 'Hog Rider',
        'title': 'title 2',
        'content': 'hello 2',
        'date': '2 2 march 2023'
    }
]


# defines what a certain webpage will display
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

# about page
@app.route("/about")
def about():
    return render_template('about.html', title = ' About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created! Thanks for signing up, {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Registration', form = form)


@app.route("/login", methods = ['GET', 'POST  '])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        if form.username.data == "admin@blog.com" or "admin" and form.password.data == "password":
            flash(f'You have successfully logged in as admin!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Sorry, try again.', 'danger')
    return render_template('login.html', title = 'Log In', form = form)


if '__name__' == '__main__':
    app.run(debug=True)
    print("Running application. ")