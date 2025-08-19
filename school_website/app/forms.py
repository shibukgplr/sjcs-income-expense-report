from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class MessageForm(FlaskForm):
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Update Message')

class NewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Add News')

class TopperForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    percentage = FloatField('Percentage', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Add Topper')

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Add Event')

class TeacherForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    qualifications = StringField('Qualifications', validators=[DataRequired()])
    photo = FileField('Photo', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Add Teacher')

class GalleryForm(FlaskForm):
    caption = StringField('Caption')
    photo = FileField('Photo', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Add Image')
