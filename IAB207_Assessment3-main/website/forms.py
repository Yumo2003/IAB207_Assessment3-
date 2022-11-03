from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

#Create new event
class EventForm(FlaskForm):
  eventName = StringField('Event Name', validators=[InputRequired()])
  venueLocation = StringField('Venue Location', validators=[InputRequired()])
  musicGenre = StringField('Music Genre', validators=[InputRequired()])
  #startDate = StringField('Start Date', validators=[InputRequired()])
  #endDate = StringField('End Date', validators=[InputRequired()])
  #startTime = StringField('Start Time', validators=[InputRequired()])
  #endTime = StringField('End Time', validators=[InputRequired()])
  ticketPrice = StringField('Ticket Price', validators=[InputRequired()])
  totalTickets = StringField('Total Tickets', validators=[InputRequired()])
  

  image = FileField('Upload Cover Image', validators=[
  FileRequired(message='Image cannot be empty'),
  FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
  description = TextAreaField('Description', validators=[InputRequired()])
  overview = TextAreaField('Overview', validators=[InputRequired()])
  

  submit = SubmitField("Submit")



    
#User login
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

#User register
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")

#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')


class PurchaseTickets(FlaskForm):
  numofTickets = StringField('Number of tickets', [InputRequired()])
  submit = SubmitField('Purchase Tickets')