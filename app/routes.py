import random
from flask import ( 
    render_template, 
    redirect, 
    url_for, 
    flash, 
    g )
from app import ( app, )
from app.database import (query_db, insert)
from app.forms import  (password,
                        viewTotalLoanLend,
                        viewPendingAmount,
                        viewOnlineTranscarions,
                        viewLoanBID,
                        authorize_storageprov,
                        authorize_farmer,
                        authorize_bank,
                        authorize_transporter,
                        authorize_shopvendor,
                        rateoffr_bank,
                        price_transporter,
                        item_price,
                        Addtrans,
                        Addbank,
                        AddLoan,
                        AddShopInv,
                        AddStoragefac,
                        AddStorageProvider, 
                        viewUniqueRateoffr,
                        AddTransporter, 
                        AddCrop, 
                        AddShopVendor, 
                        AddFarmer, 
                        AddLand)
from app.query_helper import (bank_number_of_online_trans,
                              bank_total_lgiven,
                              farmer_available_lrates,
                              bank_no_loan_giv,
                              shop_inv, 
                              storage_provider_auth, 
                              shopvendor_auth, 
                              crop_sum, 
                              crop_price, 
                              bank_rateofff, 
                              bank_total_pending)
from app.update import (
    update_authorized_storageprov, 
    update_shopinv_amount, 
    update_authorized_farmer,
    update_authorized_bank,
    update_authorized_transporter,
    update_authorized_shopvendor,
    update_rateoffr_bank,
    update_price_transporter,
    update_price_shopvendor,
)

# Creating the index route
@app.route('/')
def index():
    return render_template('index.html', enablecenter='home')

# Displaying statistics
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
    form7 = authorize_storageprov()
    if(form.validate_on_submit() and form.submit1.data):
        update_authorized_farmer(1,form.fid.data)
        flash("Successfully Changed Farmer")
        print(form.fid.data)
        return redirect(url_for('update_queries'))
    elif(form1.validate_on_submit() and form1.submit2.data):
        update_authorized_bank(1,form1.bid.data)
        flash("Successfully Changed Bank")
        print(form1.bid.data)
        return redirect(url_for('update_queries'))
    elif(form2.validate_on_submit() and form2.submit3.data):
        update_authorized_transporter(1,form2.transid.data)
        flash("Successfully Changed Transporter")
        print(form2.transid.data)
        return redirect(url_for('update_queries'))
    elif(form3.validate_on_submit() and form3.submit4.data):
        update_authorized_shopvendor(1,form3.svid.data)
        flash("Successfully Changed Shop Vendor")
        print(form3.svid.data)
        return redirect(url_for('update_queries'))
    elif(form4.validate_on_submit() and form4.submit5.data):
        update_rateoffr_bank(float(form4.rateoffr.data),form4.bid.data)
        flash("Successfully Changed Bank")
        print(float(form4.rateoffr.data),form4.bid.data)
        return redirect(url_for('update_queries'))
    elif(form5.validate_on_submit() and form5.submit6.data):
        update_price_transporter(float(form5.price.data),form5.transid.data)
        flash("Successfully Changed the price of the Transporter")
        print(float(form5.price.data),form5.transid.data)
        return redirect(url_for('update_queries'))
    elif(form7.validate_on_submit() and form7.submit8.data):
        update_authorized_storageprov(1,form7.spid.data)
        flash("Successfully Changed Storage Provider")
        print(form7.spid.data)
        return redirect(url_for('update_queries'))
    return render_template('gov.html',title="Government Portal",form=form,form1=form1,form2=form2,form3=form3,form4=form4,form5=form5,form6=form6,form7=form7)

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
        flash("Successfully Added")
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

# Helper page: (Generating links for the link/<string:page>)
@app.route('/info', methods=('GET', 'POST'))
def view_pre_info():
    return render_template('pre_info.html')

@app.route('/info/<string:page>', methods=('GET', 'POST'))
def view_info(page):
    all_values = query_db("select * from {}".format(page))
    total_count = query_db("select COUNT(*) from {}".format(page))[0][0]
    print('--------------> Display info for:', page)
    print('--------------> Total values are:', all_values)
    print('--------------> Total data is:', total_count)
    return render_template('info.html', display= all_values, name_of_table= page)

@app.route('/select', methods=('GET', 'POST'))
def view_select_queries():
    form1, noofloangiven = viewLoanBID(), 0
    if(form1.validate_on_submit() and form1.submit1.data):
        flash("ID Checked: "+form1.bid.data)
        noofloangiven= bank_no_loan_giv(form1.bid.data)[0][0]
        print('--------------> Checked for the BID:', form1.bid.data)
        print('--------------> Number of loans given are: ', noofloangiven)
        return render_template('select.html', title="Select Queries", form1=form1, noofloangiven= noofloangiven)
    form4, pendingamountvalue = viewPendingAmount(), 0
    if(form4.validate_on_submit() and form4.submit4.data):
        flash("ID Checked: "+form4.bid.data)
        pendingamountvalue= bank_total_pending(form4.bid.data)[0][0]
        print('--------------> Checked for the BID:', form4.bid.data)
        print('--------------> The pending amount is: ', pendingamountvalue)
        return render_template('select.html', title="Select Queries", form4=form4, pendingamountvalue= pendingamountvalue)
    form2, unique_rates= viewUniqueRateoffr(), 0
    if(form2.validate_on_submit() and form2.submit2.data):
        unique_rates= farmer_available_lrates()
        return render_template('select.html', title="Select Queries", form2=form2, unique_rates= unique_rates)
    form3, bank_number_of_online_tran= viewOnlineTranscarions(), 0
    if(form3.validate_on_submit() and form3.submit3.data):
        bank_number_of_online_tran= bank_number_of_online_trans()[0][0]
        return render_template('select.html', title="Select Queries", form3=form3, bank_number_of_online_tran= bank_number_of_online_tran)
    form5, bank_total_lgive= viewTotalLoanLend(), 0
    if(form5.validate_on_submit() and form5.submit5.data):
        bank_total_lgive= bank_total_lgiven()[0][0]
        return render_template('select.html', title="Select Queries", form5=form5, bank_total_lgive= bank_total_lgive)
    return render_template('select.html', title="Select Queries", form1=form1, noofloangiven= noofloangiven, form2=form2, unique_rates= unique_rates, form3=form3, bank_number_of_online_tran= bank_number_of_online_tran, form4=form4, pendingamountvalue= pendingamountvalue, form5=form5, bank_total_lgive= bank_total_lgive)

# Closing the db in case connection is lost 
@app.teardown_appcontext
def close_connection(exception):
    """
    after each request close active database connection
    """
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

#Setting the headers
@app.after_request
def add_header(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response