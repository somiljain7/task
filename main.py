
from flask import Flask,redirect, url_for,request
from wtforms import Form,BooleanField,StringField,Password_field,Validators
import pandas as pd
import re 
regex_pass="^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{9,}$"  
df=pd.read_csv('userinfo.csv')
app=Flask(__name__)

class Registration(Form):
    name=StringField('name',[validators.Length(min=3,max=25),validators.InputRequired()])
    email=StringField('email',[validators.Length,validators.DataRequired(),validators.Email()])
    password=Password_field('password',[validators.DataRequired(),validators.Regexp(regex_pass)])
  

class Login(Form):
    email = StringField('Email',
            validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

@app.route('/success')
def success():
    return 'successful'

@app.route('/fail')
def success():
    return 'failure'

@app.route('/api/sign_up', methods=['GET', 'POST'])
def signup():
    form = Registration(request.form)
    if request.method == 'POST' and form.validate():

        df=df.append({'name':[form.name.data],'email':[form.email.data],'password':[form.password.data]},ignore_index=True)        
        df.to_csv('userinfo.csv')
        flash('Thanks for registering')
    return render_template('signup.html', form=form)
@app.route('/api/sign_in', methods=['GET', 'POST'])
def login():
    form = Registration(request.form)
    if request.method == 'GET':
        if((df['email']==[form.email.data] & df['password']==[form.password.data]).any()):
            return redirect(url_for('success'))    
        else:
            return redirect(url_for('fail'))

if __name__=='__main__':
    app.run(port=5000)
       
