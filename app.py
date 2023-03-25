from flask import Flask, render_template
app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts = posts)

# about page
@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

if '__name__' == '__main__':
    app.run(debug=True)
    print("Running application. ")