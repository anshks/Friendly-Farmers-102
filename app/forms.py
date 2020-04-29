from flask_wtf import ( FlaskForm )
from wtforms import ( DecimalField, StringField, IntegerField, SubmitField, SelectField )
from wtforms.validators import ( DataRequired, Length, ValidationError )
from app.query_helper import ( query_db )

class password(FlaskForm):
    passw= StringField('password', validators=[ Length(1, 1024)])
    submit= SubmitField('Submit')

class authorize_farmer(FlaskForm):
    fid= StringField('farmerid', validators=[Length(1, 1024)])
    submit1= SubmitField('Submit')
    
class authorize_bank(FlaskForm):
    bid= StringField('bank id', validators=[Length(1, 1024)])
    submit2= SubmitField('Submit')

class authorize_transporter(FlaskForm):
    transid= StringField('transporter id', validators=[ Length(1, 1024)])
    submit3= SubmitField('Submit')

class authorize_shopvendor(FlaskForm):
    svid= StringField('shopvendor id', validators=[ Length(1, 1024)])
    submit4= SubmitField('Submit')    

class rateoffr_bank(FlaskForm):
    rateoffr= DecimalField('new rate offered', validators=[])
    bid= StringField('bank id', validators=[ Length(1, 1024)])
    submit5= SubmitField('Submit') 

class price_transporter(FlaskForm):
    price= DecimalField('new price', validators=[])
    transid= StringField('transporter id', validators=[Length(1, 1024)])
    submit6= SubmitField('Submit')  

class item_price(FlaskForm):
    price = DecimalField('new price offered ', validators=[])
    cropid= StringField('shopvendor id', validators=[Length(1, 1024)])
    submit7= SubmitField('Submit') 

class authorize_storageprov(FlaskForm):
    spid= StringField('storage provider id', validators=[ Length(1, 1024)])
    submit8= SubmitField('Submit')

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
    Crop_id = StringField('Crop_id', validators=[DataRequired(), Length(1, 1024)])
    Farmer_id = StringField('Farmer id', validators=[DataRequired(), Length(1, 1024)])
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
    land_id = StringField('Land id', validators=[DataRequired()])
    submit= SubmitField('Submit')

class AddStorageProvider(FlaskForm):
    name= StringField('Name', validators=[DataRequired(), Length(1, 1024)])
    contact= IntegerField('Contact', validators=[DataRequired()])
    lat= DecimalField('Lat', validators=[DataRequired()])
    long= DecimalField('Long', validators=[DataRequired()])
    Storageprov_id = StringField('Storage provider id', validators=[DataRequired(), Length(1, 1024)])
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
    submit = SubmitField('Submit')
    
class viewLoanBID(FlaskForm):
    bid= StringField('Bank ID', validators=[Length(1, 1024)])
    submit1= SubmitField('Submit')

class viewUniqueRateoffr(FlaskForm):
    submit2= SubmitField('View the unique loans offered from various banks')

class viewOnlineTranscarions(FlaskForm):
    submit3= SubmitField('View number of online transcations')

class viewPendingAmount(FlaskForm):
    bid= StringField('Bank ID', validators=[Length(1, 1024)])
    submit4= SubmitField('View pending amount for the bank')

class viewTotalLoanLend(FlaskForm):
    submit5= SubmitField('View total amount of loan pending')