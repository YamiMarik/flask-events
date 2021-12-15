
# IMPORTS
from datetime import datetime
import os
import calendar
from flask import Flask, render_template, url_for, redirect
from flask_wtf.recaptcha import validators
from wtforms import StringField, IntegerField, DateField, DateTimeField, SubmitField, ValidationError
from flask_sqlalchemy import SQLAlchemy
from calendar import HTMLCalendar
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


#  SQL DATABASE SETUP
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


# MODELS
class events(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(64), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    event_start = db.Column(db.DateTime, nullable=False)
    event_end = db.Column(db.DateTime, nullable=False)

    def __init__(self, event_name, event_date, event_start, event_end):
        self.event_name = event_name
        self.event_date = event_date
        self.event_start = event_start
        self.event_end = event_end

    def __repr__(self):
        return f"Event created !"


# FORMS
class EventForm(FlaskForm):
    name = StringField("Event Name", validators=[DataRequired()])
    date = DateField("Event Date in yyyy-mm-dd", format='%Y-%m-%d',
                     validators=[DataRequired()])
    start = DateTimeField("Event start time in hh:mm", format='%H:%M',
                          validators=[DataRequired()])
    end = DateTimeField("Event end time in hh:mm", format='%H:%M',
                        validators=[DataRequired()])
    submit = SubmitField("Add event")

# ROUTES
@app.route('/', methods=['GET', 'POST'])  # http://127.0.0.1:5000/
def index():
    eventform = EventForm()
    if eventform.validate_on_submit():
        new_event = events(event_name=eventform.name.data, event_date=eventform.date.data,
                           event_start=eventform.start.data, event_end=eventform.end.data)
        db.session.add(new_event)
        db.session.commit()
    event_list = events.query.all()
    return render_template('events.html', eventform=eventform, event_list=event_list)


if __name__ == '__main__':
    app.run(debug=True)
