from flask import Flask 
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY']='enter some random passppphrase '
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT']='465'
app.config['MAIL_USERNAME']='a5a48c480dc9aa'
app.config['MAIL_PASSWORD']='ca5eadc06b74e4'

mail=Mail(app)
from app import views 
