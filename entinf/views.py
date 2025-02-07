from flask import request, render_template, Blueprint, session, request, redirect, url_for
from entinf import events
from .models import Event

mainbp = Blueprint('main', __name__)

@mainbp.route("/")
def index():
    events = Event.query.all()
    
    return render_template("index.html", events = events)
    
    #image_file = url_for('static', filename=path)
    
    #return render_template("index.html", image_file = image_file)

@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        event = "%" + request.args['search'] + '%'
        events = Event.query.filter(Event.description.like(event)).all()
        return render_template('index.html', events = events)
    else:
        return redirect(url_for('main.index'))





