from app import app, mail
from flask import render_template, request, redirect, url_for, flash 
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField 
from wtforms.validators import DataRequired,Email 
from flask_mail import Message


class ContactForm(FlaskForm):
    Name = StringField('Name',validators=[DataRequired()])
    Email=StringField('Email',validators=[DataRequired(),Email()])
    subject=StringField('subject',validators=[DataRequired()])
    text_area=StringField('text_area',validators=[DataRequired()])
    #msg = Message("First Email", sender=("deanmorgan","Deanmorgan303@gmail.com"),recipients=[""])
    #msg.body = 'this is working'
    #mail.send(msg) 