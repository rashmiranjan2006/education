
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/live-classes')
def live_classes():
    return render_template('live-classes.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/stories')
def stories():
    return render_template('stories.html')

@app.route('/teachers')
def teachers():
    return render_template('teachers.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/yes')
def yes():
    return render_template('yes.html')

if __name__ == '__main__':
    app.run(debug=True)
