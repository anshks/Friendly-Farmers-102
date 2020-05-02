from app.database import query_db

# Update Queries
def update_authorized_farmer(val, farmer_id):
    s = ('update farmer set authorized = {} where fid = "{}"').format(val, farmer_id)
    query_db(s)

def update_contact_farmer(contact_no, farmer_id):
    s= ('update farmer set fcontact={} where fid ="{}"').format(contact_no, farmer_id)
    query_db(s)

def update_shopinv_amount(units,svid,item_name):
    quant = units
    s = ('select units from shop_inv where svid ="{}" and item_name="{}"').format(svid,item_name)
    res = query_db(s)
    quant += res[0][0]
    s= ('update shop_inv set item_units={} where svid ="{}" and item_name="{}"').format(quant,svid,item_name)
    query_db(s)

def  update_authorized_bank(val, bank_id):
    s = ('update bank set authorized = {} where bid = "{}"').format(val, bank_id)
    query_db(s)

def update_rateoffr_bank(rate, bank_id):
    s = ('update bank set rateoffr = {} where bid = "{}"').format(rate, bank_id)
    query_db(s)

def update_authorized_transporter(val, transporter_id):
    s = ('update transporter set authorized = {} where tid = "{}"').format(val, transporter_id)
    query_db(s)

def update_resavl_transporter(resval_val, transporter_id):
    s = ('update transporter set resavl ={} where tid = "{}"').format(resval_val, transporter_id)
    query_db(s)

def update_mintht_maxtht( transporter_id, mintht1=0, maxtht1=0 ):
    s = ('update transporter set mintwht={}, maxtwht = {} where tid = "{}"').format(mintht1, maxtht1, transporter_id)
    query_db(s)

def update_price_transporter(p1, transporter_id):
    s = ('update transporter set price = {} where tid = "{}"').format(p1, transporter_id)
    query_db(s)

def update_authorized_shopvendor(val, sv_id):
    s = ('update shopvendor set (authorized) = ({}) where svid="{}"').format(val, sv_id)
    query_db(s)
    print('--------->',query_db('select * from shopvendor where svid="{}"'.format(sv_id)))

def update_lat_long_shopvendor(lat_a, long_a, sv_id):
    s = ('update shopvendor set lat = {}, long = {} where svid = "{}"').format(lat_a, long_a, sv_id)
    query_db(s)

def update_price_shopvendor(price1, crop_id):
    s = ( 'update crop set price = {} where cid = "{}"').format(price1, crop_id)
    query_db(s)

def update_item_price(item_price_val, shop_inv_id):
    s = ('update shop_inv set item_price = {} where svid = "{}"').format(item_price_val, shop_inv_id)
    query_db(s)

def update_authorized_storageprov(val, sp_id):
    s = ('update storageprov set authorized = {} where spid = "{}"').format(val, sp_id)
    query_db(s)