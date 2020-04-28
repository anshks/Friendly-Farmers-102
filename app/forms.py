from flask_wtf import ( FlaskForm )
from wtforms import ( DecimalField, StringField, IntegerField, SubmitField, SelectField )
from wtforms.validators import ( DataRequired, Length, ValidationError )
from app.query_helper import ( query_db )

class AddFarmer(FlaskForm):
    name= StringField('Name', validators=[DataRequired(), Length(1, 1024)])
    contact= IntegerField('Contact', validators=[DataRequired()])
    lat= DecimalField('Lat', validators=[DataRequired()])
    long= DecimalField('Long', validators=[DataRequired()])
    submit= SubmitField('Submit')

class AddShopVendor(FlaskForm):
    name= StringField('Name', validators=[DataRequired(), Length(1, 1024)])
    contact= IntegerField('Contact', validators=[DataRequired()])
    lat= DecimalField('Lat', validators=[DataRequired()])
    long= DecimalField('Long', validators=[DataRequired()])
    submit= SubmitField('Submit')

class AddLand(FlaskForm):
    areaocc= DecimalField('Areaocc', validators=[DataRequired()])
    lat= DecimalField('Lat', validators=[DataRequired()])
    long= DecimalField('Long', validators=[DataRequired()])
    submit= SubmitField('Submit')

class AddTransporter(FlaskForm):
    tname= StringField('tname', validators= [DataRequired()])
    price= DecimalField('price', validators= [DataRequired()])
    mintwht= DecimalField('mintwht', validators= [DataRequired()])
    maxtwht= DecimalField('maxtwht', validators= [DataRequired()])
    lat= DecimalField('lat', validators= [DataRequired()])
    long= DecimalField('long', validators= [DataRequired()])
    resavl= DecimalField('resavl', validators= [DataRequired()])
    submit= SubmitField('Submit')

class AddCrop(FlaskForm):
    name= StringField('Name', validators=[DataRequired(), Length(1, 1024)])
    units= IntegerField('Units', validators=[DataRequired()])
    farming= StringField('Farming', validators=[DataRequired()])
    quantity= DecimalField('Quantity', validators=[DataRequired()]) #kg's
    price= DecimalField('Price', validators=[DataRequired()])
    submit= SubmitField('Submit')

class AddStorageProvider(FlaskForm):
    name= StringField('Name', validators=[DataRequired(), Length(1, 1024)])
    contact= IntegerField('Contact', validators=[DataRequired()])
    lat= DecimalField('Lat', validators=[DataRequired()])
    long= DecimalField('Long', validators=[DataRequired()])
    submit= SubmitField('Submit')

class AddLectureForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 1024)])
    shortcut = StringField('Shortcut', validators=[DataRequired(), Length(1, 64)])
    ects = IntegerField('ECTS', default=1, validators=[DataRequired()])
    submit = SubmitField('Submit')
    def validate_shortcut(self, shortcut):
        if len(query_db("select * from lecture where shortcut= ? ", (shortcut.data,))) > 0:
            raise ValidationError("Shortcut {} already exists!".format(shortcut.data))

class AddExecutionForm(FlaskForm):
    shortcut = SelectField('Shortcut', coerce=str, validators=[DataRequired()])
    lecturer = StringField('Lecturer', validators=[DataRequired()])
    semester = IntegerField('Semester', default=1, validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddExamForm(FlaskForm):
    executions = SelectField('Execution', coerce=str, validators=[DataRequired()])
    n_tries = IntegerField('Try', default=1, validators=[DataRequired()])
    mark = IntegerField('Grade', validators=[DataRequired()])
    degree = SelectField('Degree', default='b', choices=[('b', 'Bachelor'), ('m', 'Master')])
    kind = SelectField('Kind', coerce=int, default=0, choices=[(0, 'written'), (1, 'oral')])
    submit = SubmitField('Submit')