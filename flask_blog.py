from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Alex Jarabi',
        'title': "Blog Post 1",
        'content': 'First post comment',
        'date_posted': 'September 28, 2023'
    },
    {
        'author': 'Winnie Njeri',
        'title': "Blog Post 2",
        'content': 'Second post comment',
        'date_posted': 'September 29, 2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)