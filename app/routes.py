from app import ( app, )
import random
from flask import ( render_template, redirect, url_for, flash, g )
from app.forms import ( AddStorageProvider, AddTransporter, AddCrop, AddShopVendor, AddFarmer, AddLand, AddLectureForm, AddExecutionForm, AddExamForm )
from app.query_helper import ( query_db, insert, Pagination )

def stats():
    bank_rateoff = []
    crop_price1 = []
    for i in range(3):
        bank.append(bank_rateoff(i))
        crop_price1.append(crop_price(i))
    crop_sum1 = crop_sum()
    shopvendor_auth1 = shopvendor_auth()
    storage_auth1 = storage_provider_auth()
    #SVID nikalde form se yaha
    SVID = ""
    shop_inv1 = shop_inv(SVID)
    #display yeha se shuru hai

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/farmer', methods=('GET', 'POST'))
def add_farmer():
    form = AddFarmer()
    if form.validate_on_submit():
        print('\n\nIncoming Data: ', (form.name.data, form.contact.data, float(form.lat.data), float(form.long.data), 0))
        store_length= query_db('Select COUNT(*) from farmer')
        print('Total records before a farmer was added: ', store_length[0][0])
        new_id= 'F_'+str(int(store_length[0][0])+1)
        print('New ID allocated to the transporter is: ', new_id)
        insert('farmer', ('fid', 'fname', 'fcontact', 'lat', 'long', 'authorized'), (new_id, form.name.data, form.contact.data, float(form.lat.data), float(form.long.data), 0))
        print('All records for the farmers are: ')
        print(query_db("Select * from farmer"))
        flash("Successfully added new farmer {}!".format(form.name.data))
        return redirect(url_for('add_farmer'))
    return render_template('farmer.html', title="Farmers", form=form)

@app.route('/shopvendor', methods=('GET', 'POST'))
def add_shopvendor():
    form = AddShopVendor()
    if form.validate_on_submit():
        print('\n\nIncoming Data: ', (form.name.data, form.contact.data, float(form.lat.data), float(form.long.data), 0))
        store_length= query_db('Select COUNT(*) from shopvendor')
        print('Total records before a shopvendor was added: ', store_length[0][0])
        new_id= 'SV_'+str(int(store_length[0][0])+1)
        print('New ID allocated to the transporter is: ', new_id)
        insert('shopvendor', ('svid', 'svname', 'scontact', 'lat', 'long', 'authorized'), (new_id, form.name.data, form.contact.data, float(form.lat.data), float(form.long.data), 0))
        print('All records for the shopvendor are: ')
        print(query_db("Select * from shopvendor"))
        flash("Successfully added new shopvendor {}!".format(form.name.data))
        return redirect(url_for('add_shopvendor'))
    return render_template('shopvendor.html', title="Shop Vendor", form=form)

@app.route('/register-land', methods=('GET', 'POST'))
def add_registerland():
    form = AddLand()
    if form.validate_on_submit():
        print('\n\nIncoming Data: ', (form.areaocc.data, float(form.lat.data), float(form.long.data)))
        store_length= query_db('Select COUNT(*) from land')
        print('Total records before a land was added: ', store_length[0][0])
        new_id= 'LD_'+str(int(store_length[0][0])+1)
        print('New ID allocated to the transporter is: ', new_id)
        insert('land', ('lid', 'areaocc', 'lat', 'long'), (new_id, float(form.areaocc.data), float(form.lat.data), float(form.long.data)))
        print('All records for the land are: ')
        print(query_db("Select * from land"))
        flash("Successfully added new land {}!".format(new_id))
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
        insert('crop', ('cid', 'cname', 'units', 'typeoffarming', 'quantity', 'price'), (new_id, form.name.data, int(form.units.data), form.farming.data, float(form.quantity.data), float(form.price.data)))
        print('All records for the crop are: ')
        print(query_db("Select * from crop"))
        flash("Successfully added new crop {}!".format(new_id))
        return redirect(url_for('add_crop'))
    return render_template('crop.html', title="Crop", form=form)

@app.route('/transporter', methods=('GET', 'POST'))
def add_transporter():
    form = AddTransporter()
    if form.validate_on_submit():
        store_length= query_db('Select COUNT(*) from transporter')
        print('Total records before a transporter was added: ', store_length[0][0])
        new_id= 'T_'+str(int(store_length[0][0])+1)
        print('New ID allocated to the transporter is: ', new_id)
        insert('transporter', ('tid', 'tname', 'price', 'mintwht' , 'maxtwht', 'lat', 'long', 'resavl', 'authorized'), (new_id, form.tname.data, float(form.price.data), float(form.mintwht.data), float(form.maxtwht.data), float(form.lat.data), float(form.long.data), float(form.resavl.data), 0))
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
        insert('storageprov', ('spid','sname','contact','lat','long','authorized'), (new_id, form.name.data, form.contact.data, float(form.lat.data), float(form.long.data), 0))
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