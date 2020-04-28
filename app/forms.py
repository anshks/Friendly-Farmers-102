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

class AddStoragefac(FlaskForm):
    suitcond= StringField('condition', validators=[DataRequired(), Length(1, 1024)])
    size= DecimalField('size', validators=[DataRequired()])
    unit= StringField('unit', validators=[DataRequired(), Length(1, 1024)])
    price = DecimalField('Price',validators=[DataRequired()])
    lat= DecimalField('latitude', validators=[DataRequired()])
    long= DecimalField('Longitude', validators=[DataRequired()])
    typeoffarming = StringField('type of farming', validators=[DataRequired(), Length(1, 1024)])
    spaceleft = DecimalField('space left', validators=[DataRequired()])
    availability = IntegerField('available',validators=[DataRequired()]) 
    Storageprov_id = StringField('registered id of storage provider', validators=[DataRequired(), Length(1, 1024)])
    submit = SubmitField('Submit')
class AddShopInv(FlaskForm):
    svid= StringField('registered id of shop vendor', validators=[DataRequired(), Length(1, 1024)])
    item_name= StringField('item name', validators=[DataRequired(), Length(1, 1024)])
    item_price = DecimalField('Price',validators=[DataRequired()])
    units = StringField('units', validators=[DataRequired(), Length(1, 1024)])
    submit = SubmitField('Submit')
class AddLoan(FlaskForm):
    trans_id = StringField('transaction id', validators=[DataRequired(), Length(1, 1024)])
    bid = StringField('registered id of bank', validators=[DataRequired(), Length(1, 1024)])
    fid = StringField('registered id of person offered to', validators=[DataRequired(), Length(1, 1024)])
    rateoffr = DecimalField('rate offered',validators=[DataRequired()])
    date = StringField('date when offered', validators=[DataRequired(), Length(1, 1024)])
    iniamt = DecimalField('initial amount',validators=[DataRequired()])
    pendamt = DecimalField('pending amount',validators=[DataRequired()]) 
    submit = SubmitField('Submit')
class Addbank(FlaskForm):
    lat = DecimalField('latitude',validators=[DataRequired()])
    long  = DecimalField('longitude',validators=[DataRequired()])
    rateoffr = DecimalField('rate offered',validators=[DataRequired()])
    submit = SubmitField('Submit')
class Addtrans(FlaskForm):
    amount = DecimalField('amount',validators=[DataRequired()])
    method = StringField('method of transaction', validators=[DataRequired(), Length(1, 1024)])
    from_id = StringField('registered id of payer', validators=[DataRequired(), Length(1, 1024)])
    to_id = StringField('registered id of reciever', validators=[DataRequired(), Length(1, 1024)])
    identity_from = StringField('identity of person from', validators=[DataRequired(), Length(1, 1024)])
    identity_to = StringField('identity of person to', validators=[DataRequired(), Length(1, 1024)])
 
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