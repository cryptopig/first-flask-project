from flask import Flask, render_template, flash, url_for, redirect
app = Flask(__name__)
from forms import RegistrationForm, LoginForm

app.config["SECRET_KEY"] = f'ab9c32a070313d1343395f1cc4d5a669'

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
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created! Thanks for signing up, {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Registration', form = form)


@app.route("/login", methods = ['GET', 'POST'])
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