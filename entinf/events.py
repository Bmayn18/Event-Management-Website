from flask import request, render_template, Blueprint, session, redirect, url_for, flash, get_flashed_messages
from .forms import CreateEventForm, CommentForm, FilterForm, EditEventForm, BookingForm
from .models import Event, Comment, Booking
from . import db
from flask_login import login_required, current_user
from datetime import date

bp = Blueprint('events', __name__, url_prefix = '/events')

@bp.route("/<id>", methods=['GET', 'POST'])
def details(id):
    event = Event.query.filter_by(id = id).first()

    cform = CommentForm()
    pform = BookingForm()
    if pform.validate_on_submit():
        event_id = id
        user_id = current_user.id
        price = event.price
        ticket_number = pform.ticket_number.data
        event.ticketcount = event.ticketcount - ticket_number
        booking = Booking(event_id = event_id, user_id = user_id, price = price, ticket_number = ticket_number)
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for("events.history"))
    return render_template("events/details.html", event = event, form = cform, pform = pform)

@bp.route("/eventslist", methods = ['GET', 'POST'])
def eventslist():
    filterForm = FilterForm()
    events = Event.query.all()
    if filterForm.validate_on_submit():
        genrevalue = filterForm.genre.data
        venuevalue = filterForm.venue.data
        print(venuevalue)
        print(genrevalue)
        if genrevalue == 'Choose' and venuevalue != 'Choose':
            print(2)
            events = Event.query.filter_by(venue = venuevalue).all()
        elif venuevalue == 'Choose' and genrevalue != 'Choose':
            print(1)
            events = Event.query.filter_by(genre = genrevalue).all()
        elif venuevalue != 'Choose' and genrevalue != 'Choose':
            print(3)
            events = Event.query.filter_by(venue = venuevalue, genre = genrevalue).all()


    return render_template("events/events.html", events = events, form = filterForm)

@bp.route("/history", methods = ['GET'])
@login_required
def history():
    if (current_user.is_authenticated == False):
        return redirect(url_for('auth.login'))

    booked_events=[]

    created_events = Event.query.filter_by(userid = current_user.id).all()
    bookings = Booking.query.filter_by(user_id = current_user.id).all()
    for booking in bookings:
        booked_events.append(Event.query.filter_by(id = booking.event_id).first())


    return render_template("events/history.html", events = created_events, bookings = booked_events)
    

@bp.route("/create", methods = ['GET', 'POST'])
@login_required
def create():
    eventform = CreateEventForm()
    if eventform.validate_on_submit():
        newevent = Event(
            name = eventform.name.data,
            external_link = eventform.external_link.data,
            artist = eventform.artist.data,
            genre = eventform.genre.data,
            date = eventform.date.data,
            start_time = eventform.start_time.data,
            capacity = eventform.capacity.data,
            image = eventform.image.data,
            description = eventform.description.data,
            price = eventform.price.data,
            venue = eventform.venue.data
        )
        today = date.today()
        if newevent.date < today:
            flash('Date must be set to a later date.')
            return redirect(url_for('events.create'))

        newevent.ticketcount = newevent.capacity
        newevent.userid = current_user.id
        db.session.add(newevent)
        db.session.commit()
        print(newevent.start_time)
        return redirect(url_for("events.create"))
    print(eventform.errors)
    return render_template("events/create.html", form = eventform)

@bp.route('/editevent/<id>', methods = ['GET', 'POST'])
def editevent(id):
    editform = EditEventForm()
    event = Event.query.filter_by(id = id).first()

    if editform.validate_on_submit():

        nameupdate = editform.name.data
        if nameupdate != None:
            event.name = nameupdate

        linkupdate = editform.external_link.data
        if linkupdate != None:
            event.external_link = linkupdate

        artistupdate = editform.external_link.data
        if artistupdate != None:
            event.artist = artistupdate

        genreupdate = editform.genre.data
        if genreupdate != None:
            event.genre = genreupdate

        dateupdate = editform.date.data
        if dateupdate != None:
            event.date = dateupdate

        timeupdate = editform.start_time.data
        if timeupdate != None:
            event.start_time = timeupdate

        ticketssold = event.capacity - event.ticketcount
        amountupdate = editform.capacity.data - ticketssold
        if amountupdate != None and amountupdate > 0:
            event.ticketcount = amountupdate

        capacityupdate = editform.capacity.data
        if capacityupdate != None:
            event.capacity = capacityupdate

        imageupdate = editform.image.data
        if imageupdate != None:
            event.image = imageupdate

        descriptionupdate = editform.description.data
        if descriptionupdate != None:
            event.description = descriptionupdate

        priceupdate = editform.price.data
        if priceupdate != None and float(priceupdate) > -1.00: 
            event.price = editform.price.data
        
        statusupdate = editform.status.data
        if statusupdate != 'Open':
            event.status = statusupdate

        venueupdate = editform.venue.data
        if venueupdate != 'Choose...':
            event.venue = venueupdate
        
        db.session.commit()
        return redirect(url_for('events.details', id=event.id))
    print(editform.errors)

    return render_template('events/editevent.html', events = event, form = editform)

    

@bp.route('/<event>/comment', methods = ['GET', 'POST'])
@login_required
def comment(event):  
    form = CommentForm()
    event_obj = Event.query.filter_by(id = event).first()  
    if form.validate_on_submit():
        comment = Comment(
        text = form.text.data,  
        event = event_obj,
        user = current_user
        )
    db.session.add(comment) 
    db.session.commit() 
    print('Your comment has been added', 'success') 
    return redirect(url_for('events.details', id = event))