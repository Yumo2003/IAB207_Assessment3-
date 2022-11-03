from email.policy import default
from msilib import datasizemask
from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__= 'users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')


class purchasedTickets(db.Model):  
    __tablename__ = "purchasedTickets"
    user_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    numPurchasedTickets = db.Column(db.Integer)


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    venueLocation = db.Column(db.String(100))
    Genre = db.Column(db.String(50))
    startTime = db.Column(db.DateTime, default=datetime(year=1,month=1,day=1))
    endTime = db.Column(db.DateTime, default=datetime(year=1,month=1,day=1))
    startDate = db.Column(db.DateTime, default=datetime(year=1,month=1,day=1))
    endDate = db.Column(db.DateTime, default=datetime(year=1,month=1,day=1))
    ticketPrice = db.Column(db.Integer)
    numTicket = db.Column(db.Integer)
    overview = db.Column(db.String(50))
    image = db.Column(db.String(400))
    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='events')
    
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))


    def __repr__(self):
        return "<Comment: {}>".format(self.text)


