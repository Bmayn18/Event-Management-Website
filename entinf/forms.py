from . import db
from wtforms import *
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, DateField, TimeField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo, NumberRange

#Create new event
class CreateEventForm(FlaskForm):
  name = StringField('Event Name', validators=[InputRequired(), Length (max=100)])
  external_link = StringField('Artists Page', validators=[InputRequired(), Length (max=255)])
  artist = StringField('Artist Name', validators=[InputRequired(), Length (max=100)])
  genre = SelectField(
    u'Genre',
    choices=[('Choose', 'Choose...'), 
    ('Pop', 'Pop'), 
    ('Rock', 'Rock'), 
    ('Metal', 'Metal'), 
    ('Country', 'Country'), 
    ('Hip Hop', 'Hip Hop'), 
    ('Other', 'Other')], validators=[InputRequired()])
  date = DateField('Date', format='%Y-%m-%d')
  start_time = TimeField('Start Time', format='%H:%M')
  capacity = IntegerField('Capacity', validators=[InputRequired()])
  image = StringField('Event Cover Image (must be image address)', validators=[InputRequired(), Length (max=400)])
  description = TextAreaField('Description', [InputRequired(), Length (max=200)]) #, none = None)])
  price = StringField('Price', validators=[InputRequired()])
  venue = SelectField(
    u'Venue', 
    choices=[('Choose', 'Choose...'), 
    ('Suncorp stadium', 'Suncorp Stadium'), 
    ('Riverstage', 'Riverstage'), 
    ('Gabba', 'Gabba'), 
    ('Metricon Stadium', 'Metricon Stadium'), 
    ('The Tivoli Theatre', 'The Tivoli Theatre'), 
    ('Fortitude Music Hall', 'Fortitude Music Hall'), 
    ('Southbank', 'Southbank'), 
    ('Brightside brisbane', 'Brightside brisbane')], validators=[InputRequired()])
  submit = SubmitField("Filter")
  submit = SubmitField("Create")

#Edit event
class EditEventForm(FlaskForm):
  name = StringField('Event Name', validators=[Length (max=100)])
  external_link = StringField('Artists Page', validators=[Length (max=255)])
  artist = StringField('Artist Name', validators=[Length (max=100)])
  genre = SelectField(
    u'Genre',
    choices=[('Choose', 'Choose...'), 
    ('Pop', 'Pop'), 
    ('Rock', 'Rock'), 
    ('Metal', 'Metal'), 
    ('Country', 'Country'), 
    ('Hip Hop', 'Hip Hop'), 
    ('Other', 'Other')], validators=[InputRequired()])
  date = DateField('Date', format='%Y-%m-%d')
  start_time = TimeField('Start Time', format='%H:%M')
  capacity = IntegerField('Capacity')
  image = StringField('Event Cover Image (please ensure 1:1 aspect ratio)', validators=[Length (max=400)])
  description = TextAreaField('Description', [Length (max=200)]) #, none = None)])
  price = StringField('Price')
  status = SelectField(u'Status', choices=[('open', 'open'), ('sold out', 'sold out'), ('cancelled', 'cancelled'), ('unpublished', 'unpublished')], validators=[InputRequired()])
  venue = SelectField(
    u'Venue', 
    choices=[('Choose', 'Choose...'), 
    ('Suncorp stadium', 'Suncorp Stadium'), 
    ('Riverstage', 'Riverstage'), 
    ('Gabba', 'Gabba'), 
    ('Metricon Stadium', 'Metricon Stadium'), 
    ('The Tivoli Theatre', 'The Tivoli Theatre'), 
    ('Fortitude Music Hall', 'Fortitude Music Hall'), 
    ('Southbank', 'Southbank'), 
    ('Brightside brisbane', 'Brightside brisbane')], validators=[InputRequired()])
  submit = SubmitField("Create")

#Drop down menu options
class FilterForm(FlaskForm):
  genre = SelectField(u'Genre', 
  choices=[('Choose', 'Choose...'), 
  ('Pop', 'Pop'), 
  ('Rock', 'Rock'), 
  ('Metal', 'Metal'), 
  ('Country', 'Country'), 
  ('Hip Hop', 'Hip Hop'), 
  ('Other', 'Other')], validators=[InputRequired()])
  venue = SelectField(u'Venue', 
  choices=[('Choose', 'Choose...'), 
  ('Suncorp stadium', 'Suncorp Stadium'), 
  ('Riverstage', 'Riverstage'), 
  ('Gabba', 'Gabba'), 
  ('Metricon Stadium', 'Metricon Stadium'), 
  ('The Tivoli Theatre', 'The Tivoli Theatre'), 
  ('Fortitude Music Hall', 'Fortitude Music Hall'), 
  ('Southbank', 'Southbank'), 
  ('Brightside Brisbane', 'Brightside Brisbane')], validators=[InputRequired()])
  submit = SubmitField("Filter")
    
#Create booking
class BookingForm(FlaskForm):
  ticket_number = IntegerField('Number of Tickets', validators=[InputRequired()])
  submit = SubmitField('Purchase')


#User login
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name'), Length (max=20)])
    password=PasswordField("Password", validators=[InputRequired('Enter user password'), Length (max=20)])
    submit = SubmitField("Login")

#User register
class RegisterForm(FlaskForm):
    username = StringField("User Name", validators=[InputRequired(), Length (max=20)])
    firstname = StringField("First Name", validators=[InputRequired(), Length (max=100)])
    lastname = StringField("Last Name", validators=[InputRequired(), Length (max=100)])
    emailid = EmailField("Email Address", validators=[Email("Please enter a valid email")])
    phone = IntegerField("Phone number", validators=[InputRequired(), NumberRange (min=0, max=9999999999, message="please provide a valid phone number")])
    state = SelectField(u'State', choices=[('QLD', 'QLD'),('NSW', 'NSW'),('VIC', 'VIC'),('SA', 'SA'),
                                          ('WA', 'WA'),('TAS', 'TAS'),('NT', 'NT'),('ACT', 'ACT')], validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired(), Length (max=100)])
    suburb = StringField("Suburb", validators=[InputRequired()])
    postcode = IntegerField("Postcode", validators=[InputRequired(), NumberRange (min=1000, max=9999, message="Postcode should be 4 digits")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match"), Length (max=20, min=8)])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired(), Length (max=200)])
  submit = SubmitField('Create')

