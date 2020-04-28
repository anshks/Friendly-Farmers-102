from app import ( app, )
import random
from flask import ( render_template, redirect, url_for, flash, g )
from app.forms import ( password,authorize_farmer,authorize_bank,authorize_transporter,authorize_shopvendor,rateoffr_bank,price_transporter,item_price,Addtrans,Addbank,AddLoan,AddShopInv,AddStoragefac,AddStorageProvider, AddTransporter, AddCrop, AddShopVendor, AddFarmer, AddLand, AddLectureForm, AddExecutionForm, AddExamForm )
from app.query_helper import ( update_authorized_farmer,update_authorized_bank,update_authorized_transporter,update_authorized_shopvendor,update_authorized_shopvendor,update_rateoffr_bank,update_price_transporter,update_price_shopvendor,shop_inv, storage_provider_auth, shopvendor_auth, crop_sum, crop_price, bank_rateofff, query_db, insert, Pagination )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/statistics', methods=('GET', 'POST'))
def stats():
    bank= []
    crop_price1= []
    for i in range(3):
        bank.append(bank_rateofff(i))
        crop_price1.append(crop_price(i))
    crop_sum1= crop_sum()
    shopvendor_auth1= shopvendor_auth()
    storage_auth1= storage_provider_auth()
    print('Generated the files --->', bank, crop_price)
    return render_template('statistics.html', title="Statistics")

@app.route('/farmer', methods=('GET', 'POST'))
def add_farmer():
    form = AddFarmer()
    if form.validate_on_submit():
        print('\n\nIncoming Data: ', (form.name.data, int(form.contact.data), float(float(form.lat.data)), float(float(form.long.data)), 0))
        store_length= query_db('Select COUNT(*) from farmer')
        print('Total records before a farmer was added: ', store_length[0][0])
        new_id= 'F_'+str(int(store_length[0][0])+1)
        print('New ID allocated to the transporter is: ', new_id)
        insert('farmer', ('fid', 'fname', 'fcontact', 'lat', 'long', 'authorized'), (new_id, form.name.data, int(form.contact.data), float(float(form.lat.data)), float(float(form.long.data)), 0))
        print('All records for the farmers are: ')
        print(query_db("Select * from farmer"))
        flash("Successfully added new farmer {}!".format(form.name.data))
        return redirect(url_for('add_farmer'))
    return render_template('farmer.html', title="Farmers", form=form)

@app.route('/shopvendor', methods=('GET', 'POST'))
def add_shopvendor():
    form = AddShopVendor()
    if form.validate_on_submit():
        print('\n\nIncoming Data: ', (form.name.data, int(form.contact.data), float(float(form.lat.data)), float(float(form.long.data)), 0))
        store_length= query_db('Select COUNT(*) from shopvendor')
        print('Total records before a shopvendor was added: ', store_length[0][0])
        new_id= 'SV_'+str(int(store_length[0][0])+1)
        print('New ID allocated to the transporter is: ', new_id)
        insert('shopvendor', ('svid', 'svname', 'scontact', 'lat', 'long', 'authorized'), (new_id, form.name.data, int(form.contact.data), float(float(form.lat.data)), float(float(form.long.data)), 0))
        print('All records for the shopvendor are: ')
        print(query_db("Select * from shopvendor"))
        flash("Successfully added new shopvendor {}!".format(form.name.data))
        return redirect(url_for('add_shopvendor'))
    return render_template('shopvendor.html', title="Shop Vendor", form=form)

@app.route('/register-land', methods=('GET', 'POST'))
def add_registerland():
    form = AddLand()
    if form.validate_on_submit():
        print('\n\nIncoming Data: ', (float(form.areaocc.data), float(float(form.lat.data)), float(float(form.long.data))))
        store_length= query_db('Select COUNT(*) from land')
        print('Total records before a land was added: ', store_length[0][0])
        new_id= 'LD_'+str(int(store_length[0][0])+1)
        print('New ID allocated to the transporter is: ', new_id)
        insert('land', ('lid', 'areaocc', 'lat', 'long'), (new_id, float(float(form.areaocc.data)), float(float(form.lat.data)), float(float(form.long.data))))
        print('All records for the land are: ')
        print(query_db("Select * from land"))
        flash("Successfully added new land {}!".format(new_id))
        insert('landcrop',('cid','lid'),(form.Crop_id.data,new_id))
        insert('farmerland',('fid','lid'),(form.Farmer_id.data,new_id))
        return redirect(url_for('add_registerland'))
    return render_template('registerland.html', title="Land", form=form)

@app.route('/crop', methods=('GET', 'POST'))
def add_crop():
    form = AddCrop()
    if form.validate_on_submit():
        store_length= query_db('Select COUNT(*) from crop')
        print('Total records before a crop was added: ', store_length[0][0])
        new_id= 'C_'+str(int(store_length[0][0])+1)
        print('New ID allocated to the transporter is: ', new_id)
        insert('crop', ('cid', 'cname', 'units', 'typeoffarming', 'quantity', 'price'), (new_id, form.name.data, int(float(form.units.data)), form.farming.data, float(float(form.quantity.data)), float(float(form.price.data))))
        print('All records for the crop are: ')
        print(query_db("Select * from crop"))
        insert('landcrop',('lid','cid'),(form.land_id.data,new_id))
        flash("Successfully added new crop {}!".format(new_id))

        return redirect(url_for('add_crop'))
    return render_template('crop.html', title="Crop", form=form)

@app.route('/addfacility',methods=('GET','POST'))
def add_storagefac():
    form = AddStoragefac()
    if form.validate_on_submit():
        length = query_db('Select COUNT(*) from storagefacloc')
        new_id = 'S_' + str(int(length[0][0]) + 1)
        insert('storagefacloc',('sid', 'suitcond', 'size', 'unit', 'price', 'lat', 'long', 'typeoffarming', 'spaceleft', 'availability'),
            (new_id,form.suitcond.data,float(form.size.data),form.unit.data,float(form.price.data),float(form.lat.data),float(form.long.data),form.typeoffarming.data,float(float(form.spaceleft.data)),form.availability.data))
        insert('spstorage',('sid','spid'),(new_id,form.Storageprov_id.data))
        flash("Successfully added")
        return redirect(url_for('add_storagefac'))
    return render_template('storagefac.html',title="storage facility location",form = form)
@app.route('/addshopinv',methods=('GET','POST'))
def add_shop_inv():
    form = AddShopInv()
    if form.validate_on_submit():
        length = query_db(('Select COUNT(*) from shop_inv where svid=\'{}\' and item_name=\'{}\'').format(form.svid.data,form.item_name.data))
        if(length[0][0] == 0):
            insert('shop_inv',('svid','item_name','item_price','units'),(form.svid.data,form.item_name.data,float(form.item_price.data),float(form.units.data)))
        else:
            update_shopinv_amount(float(form.units.data),form.svid.data,form.item_name.data)    
        flash("Successfully added")
        return redirect(url_for('add_shop_inv'))
    return render_template('shop_inv.html',title="shop inventory",form=form)
@app.route('/Govermentlogin',methods=('GET','POST'))
def login():
    form = password()
    if(form.validate_on_submit()):
        if(form.passw.data == 'dbms'):
            flash("login complete")
            return redirect(url_for('update_queries'))
        return redirect(url_for('login'))
    return render_template('login.html',title="Govermentlogin",form=form)
@app.route('/Govermentchecked',methods=('GET','POST'))
def update_queries():
    form = authorize_farmer()
    form1 = authorize_bank()
    form2 = authorize_transporter()
    form3 = authorize_shopvendor()
    form4 = rateoffr_bank()
    form5 = price_transporter()
    form6 = item_price()
    if(form.validate_on_submit() and form.submit1.data):
        update_authorized_farmer(1,form.fid.data)
        flash("Successfully changed")
        print(form.fid.data)
        return redirect(url_for('update_queries'))
    if(form1.validate_on_submit() and form1.submit2.data):
        update_authorized_bank(1,form1.bid.data)
        flash("Successfully changed")
        print(form1.bid.data)
        return redirect(url_for('update_queries'))
    if(form2.validate_on_submit() and form2.submit3.data):
        update_authorized_transporter(1,form2.transid.data)
        flash("Successfully changed")
        print(form2.transid.data)
        return redirect(url_for('update_queries'))
    if(form3.validate_on_submit() and form3.submit4.data):
        update_authorized_shopvendor(1,form3.svid.data)
        flash("Successfully changed")
        print(form3.svid.data)
        return redirect(url_for('update_queries'))
    if(form4.validate_on_submit() and form4.submit5.data):
        update_rateoffr_bank(float(form4.rateoffr.data),form4.bid.data)
        flash("Successfully changed")
        print(float(form4.rateoffr.data),form4.bid.data)
        return redirect(url_for('update_queries'))
    if(form5.validate_on_submit() and form5.submit6.data):
        update_price_transporter(float(form5.price.data),form5.transid.data)
        flash("Successfully changed")
        print(float(form5.price.data),form5.transid.data)
        return redirect(url_for('update_queries'))
    if(form6.validate_on_submit() and form6.submit7.data):
        update_price_shopvendor(float(form6.price.data),form6.cropid.data)
        flash("Successfully changed")
        return redirect(url_for('update_queries'))
    return render_template('gov.html',title="shop inventory",form=form,form1=form1,form2=form2,form3=form3,form4=form4,form5=form5,form6=form6)
@app.route('/addloan',methods=('GET','POST'))
def add_loan():
    form = AddLoan()
    if form.validate_on_submit():
        length = query_db('Select COUNT(*) from loan')
        new_id= 'L_'+str(int(length[0][0])+1)
        insert('loan',('lid', 'rateoffr', 'dateoffr', 'offrto', 'iniamt', 'pendamt'),(new_id,float(form.rateoffr.data),form.date.data,form.fid.data,float(form.iniamt.data),float(form.pendamt.data)))
        insert('loantrans',('lid','transid'),(new_id,form.trans_id.data))
        insert('bankfloan',('lid','bid','fid'),(new_id,form.bid.data,form.fid.data))
        flash("Successfully added")
        return redirect(url_for('add_loan'))
    return render_template('loan.html',title="loan",form=form)
@app.route('/addbank',methods=('GET','POST'))
def add_bank():
    form = Addbank()
    if(form.validate_on_submit()):
        length = query_db('select count(*) from bank')
        new_id = 'B_' + str(int(length[0][0]) + 1)
        insert('bank',('bid', 'lat', 'long', 'rateoffr'),(new_id,float(form.lat.data),float(form.long.data),float(form.rateoffr.data)))
        flash("Successfully added")
        return redirect(url_for('add_bank'))
    return render_template('bank.html',title="bank",form=form)
@app.route('/addtrans',methods=('GET','POST'))
def add_trans():
    form = Addtrans()
    if(form.validate_on_submit()):
        length = query_db('select count(*) from transactions')
        new_id = 'TR_' + str(int(length[0][0])+1)
        insert('transactions',('transid', 'amount', 'method'),(new_id,float(form.amount.data),form.method.data))
        if(form.identity_from.data == 'Farmer'):
            if(form.identity_to.data == 'transporter'):
                insert('ftt',('transid','fid','tid'),(new_id,form.from_id.data,form.to_id.data))
            if(form.identity_to.data == 'shopvendor'):
                insert('fsvt',('transid','fid','svid'),(new_id,form.from_id.data,form.to_id.data))    
            if(form.identity_to.data == 'storage provider'):
                insert('fspt',('transid','fid','spid'),(new_id,form.from_id.data,form.to_id.data))
        else:
            if(form.identity_from.data == 'transporter'):
                insert('ftt',('transid','fid','tid'),(new_id,form.to_id.data,form.from_id.data))
            if(form.identity_from.data == 'shopvendor'):
                insert('fsvt',('transid','fid','svid'),(new_id,form.to_id.data,form.from_id.data))    
            if(form.identity_from.data == 'storage provider'):
                insert('fspt',('transid','fid','spid'),(new_id,form.to_id.data,form.from_id.data))
                return redirect(url_for('add_trans'))
        flash("Successfully added")
    return render_template('trans.html',title="trans",form=form)
@app.route('/transporter', methods=('GET', 'POST'))
def add_transporter():
    form = AddTransporter()
    if form.validate_on_submit():
        store_length= query_db('Select COUNT(*) from transporter')
        print('Total records before a transporter was added: ', store_length[0][0])
        new_id= 'T_'+str(int(store_length[0][0])+1)
        print('New ID allocated to the transporter is: ', new_id)
        insert('transporter', ('tid', 'tname', 'price', 'mintwht' , 'maxtwht', 'lat', 'long', 'resavl', 'authorized'), (new_id, form.tname.data, float(float(form.price.data)), float(form.mintwht.data), float(form.maxtwht.data), float(float(form.lat.data)), float(float(form.long.data)), float(form.resavl.data), 0))
        print('All records for the transporter are: ')
        print(query_db("Select * from transporter"))
        flash("Successfully added new transporter {}!".format(new_id))
        return redirect(url_for('add_transporter'))
    store_length= query_db('Select COUNT(*) from transporter')
    print('Total records before loading transporter: ', store_length[0][0])
    return render_template('transporter.html', title="Transporter", form=form)

@app.route('/storage-provider', methods=('GET', 'POST'))
def add_storage_provider():
    form = AddStorageProvider()
    if form.validate_on_submit():
        store_length= query_db('Select COUNT(*) from storageprov')
        print('Total records before a storageprov was added: ', store_length[0][0])
        new_id= 'SP_'+str(int(store_length[0][0])+1)
        print('New ID allocated to the storageprov is: ', new_id)
        insert('storageprov', ('spid','sname','contact','lat','long','authorized'), (new_id, form.name.data, int(form.contact.data), float(float(form.lat.data)), float(float(form.long.data)), 0))
        print('All records for the storageprov are: ')
        print(query_db("Select * from storageprov"))
        flash("Successfully added new storageprov {}!".format(new_id))
        return redirect(url_for('add_storage_provider'))
    store_length= query_db('Select COUNT(*) from storageprov')
    print('Total records before loading storageprov: ', store_length[0][0])
    return render_template('storageprov.html', title="Storageprov", form=form)

@app.route('/exams/', defaults={'page': 1}, methods=('GET', 'POST'))
@app.route('/exams/page/<int:page>', methods=('GET', 'POST'))
def view_exams(page):
    total_count = query_db(
        "select count(shortcut) from exam", one=True)[0]
    pagination = Pagination(page, total_count, per_page=3)
    exams = query_db( "select shortcut, name, semester, n_tries, mark, degree,kind " "from exam join lecture using (shortcut) order by shortcut,semester,n_tries limit ?,?", ((page - 1) * pagination.per_page, pagination.per_page))
    next_page = url_for('view_exams', page=page + 1) if pagination.has_next else None
    prev_page = url_for('view_exams', page=page - 1) if pagination.has_prev else None
    return render_template('view_exams.html', exams=exams, next_page=next_page, prev_page=prev_page, title="Exams" )

@app.route('/add_exam', methods=('GET', 'POST'))
def add_exam():
    form = AddExamForm()
    executions = query_db("select shortcut, semester from execution")
    form.executions.choices = [('?'.join(map(str, k)), "{} in semester {}".format(*k)) for k in executions]

    if form.validate_on_submit():
        shortcut, semester = form.executions.data.split('?')
        if len(query_db("select 1 from exam where shortcut=? and semester=? and n_tries=?", (shortcut, semester, form.n_tries.data))) > 0:
            flash("Exam already exists!")
            return redirect(url_for('add_exam'))
        insert('exam', ('shortcut', 'semester', 'n_tries', 'mark', 'degree', 'kind'), (shortcut, semester, form.n_tries.data, form.mark.data, form.degree.data, form.kind.data))
        flash("Successfully added exam {}!".format(shortcut))
        return redirect(url_for('view_exams'))
    return render_template('add_exam.html', title="Exams", form=form )

@app.route('/execution', methods=('GET', 'POST'))
def add_execution():
    form = AddExecutionForm()
    lectures = query_db("select shortcut,name from lecture")
    form.shortcut.choices = [(k[0], k[1]) for k in lectures]

    if form.validate_on_submit():
        # insert
        insert('execution', ('shortcut', 'lecturer', 'semester'), (form.shortcut.data, form.lecturer.data, form.semester.data))
        flash("Successfully added execution!")
        return redirect(url_for('add_execution'))
    return render_template('add_execution.html', title="Executions", form=form)

# administration
@app.teardown_appcontext
def close_connection(exception):
    """
    after each request close active database connection
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.after_request
def add_header(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response