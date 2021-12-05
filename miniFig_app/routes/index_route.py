from flask import render_template,redirect
from miniFig_app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blindbox')
def blindbox():
    id = "BLINDBOX"
    return redirect(f'/display_minifig/{id}')
