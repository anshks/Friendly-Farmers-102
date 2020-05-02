import sqlite3, math
from app import ( app )
from math import ( ceil )
from app.database import (get_db, query_db, insert)
from app.geocoding import (address_to_latlong, latlong_to_address)
from app.plot import (barGraph, pieChart, stdev_quantity, stdev_rate)

# Initiliaze the database
def init_db():
    """
    initialize a database
    created a database schema according to schema.sql
    """
    with app.app_context():
        print('\n\n> Checking if the geopy module is working, entered (lat, long) as (10, 10)')
        print(latlong_to_address(10, 10))
        db = get_db()
        print('\n\n> Started with the creating the database')
        with app.open_resource('schema.sql', mode='r') as f:
            store= f.read()
            db.cursor().executescript(store)
        db.commit()
        print('\n\n> Created the database')
        print(query_db("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';"), '\n')
        create_the_databse();
        check_farmer()
        check_banks()
        check_transporter()
        check_authorities()
        check_shopvendor()
        bank_rtf = []
        crop_price1 = []
        for i in range(3):
            bank_rtf.append(bank_rateofff(i))
            crop_price1.append(crop_price(i))
        crop_sum1 = crop_sum()
        shopvendor_auth1 = shopvendor_auth()
        storage_auth1 = storage_provider_auth()
        #SVID nikalde form se yaha
        SVID = "SV_191"
        shop_inv1 = shop_inv(SVID)
        #display yeha se shuru hai

def create_the_databse():
    query_db("CREATE INDEX IF NOT EXISTS idx_farmer ON farmer (fid);")
    query_db("CREATE INDEX IF NOT EXISTS idx_land ON land (lid);")
    query_db("CREATE INDEX IF NOT EXISTS idx_crop ON crop (cid);")
    query_db("CREATE INDEX IF NOT EXISTS idx_shopvendor ON shopvendor (svid);")
    query_db("CREATE INDEX IF NOT EXISTS idx_transporter ON transporter (tid);")
    query_db("CREATE INDEX IF NOT EXISTS idx_storageprov ON storageprov (spid);")
    query_db("CREATE INDEX IF NOT EXISTS idx_transactions ON transactions (transid);")
    query_db("CREATE INDEX IF NOT EXISTS idx_bank ON bank (bid);")
    query_db("CREATE INDEX IF NOT EXISTS idx_loan ON loan (lid);")
    query_db("CREATE INDEX IF NOT EXISTS idx_storagefacloc ON storagefacloc (sid);")
    query_db("CREATE INDEX IF NOT EXISTS idx_farmer ON farmer (fid);")
    insertintotrasaction()
    insertintoloan()
    printalltables('loan')
    printalltables('transactions')
    insertintofarmer()
    insertintoland()
    printalltables('farmer')
    printalltables('land')
    insertintocrop()
    insertintoshopv()
    printalltables('crop')
    printalltables('shopvendor')
    insertintotransporter()
    insertintostorageprov()
    printalltables('transporter')
    printalltables('storageprov')
    insertintosvcrop()
    insertintoloantrans()
    insertintobankfloan()
    printalltables('svcrop')
    printalltables('loantrans')
    printalltables('bankfloan')
    insertintotranscrop()
    insertintoshopinv()
    printalltables('transcrop')
    printalltables('shop_inv')
    insertintolandcrop()
    insertintofarmerland()
    insertintofspt()
    printalltables('landcrop')
    printalltables('farmerland')
    printalltables('fspt')
    insertintoftt()
    printalltables('ftt')
    insertintobank()
    insertintofsvt()
    insertintostoragefacloc()
    insertintospstorage()
    insertintostoragecrop()
    printalltables('bank')
    printalltables('fsvt')
    printalltables('storagefacloc')
    printalltables('spstorage')
    printalltables('storagecrop')

# Print Table Query
def printalltables(table):
    alltables= query_db("Select * from "+table)
    print(alltables)
    return alltables

# Insert Queries
def insertintotrasaction():
    insert('transactions', ('transid', 'amount', 'method'), ('TR_101', 15000.00, 'Online'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_102', 120000.00, 'Cash'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_103', 100000.00, 'Online'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_104', 800000.00, 'Online'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_105', 200000.00, 'Cash'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_106', 100000.00, 'Online'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_107', 400000.00, 'Cash'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_108', 500000.00, 'Online'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_109', 600000.00, 'Cash'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_110', 200000.00, 'Cash'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_111', 400000.00, 'Online'))
    insert('transactions', ('transid', 'amount', 'method'), ('TR_112', 180000.00, 'Cash'))

def insertintoloan():
    insert('loan', ('lid', 'rateoffr', 'dateoffr', 'offrto', 'iniamt', 'pendamt'), ('L_1586', 10.35, '22-04-10', 'F_102', 13500.00, 11000.00))
    insert('loan', ('lid', 'rateoffr', 'dateoffr', 'offrto', 'iniamt', 'pendamt'), ('L_2000', 8.00, '10-04-10', 'F_104', 50000.00, 49000.00))
    insert('loan', ('lid', 'rateoffr', 'dateoffr', 'offrto', 'iniamt', 'pendamt'), ('L_2314', 9.35, '18-04-10', 'F_105', 20500.00, 20500.00))

def insertintofarmer():
    insert('farmer', ('fid', 'fname', 'fcontact', 'authorized','lat','long'), ('F_102','Ramu',9997712345,1,28.613459,77.176208))
    insert('farmer', ('fid', 'fname', 'fcontact', 'authorized','lat','long'), ('F_104','Sahu',9412345678,0,28.603212,77.188439))
    insert('farmer', ('fid', 'fname', 'fcontact', 'authorized','lat','long'), ('F_105','Sid',7771122333,1,28.596580,77.181745))

def insertintoland():
    insert('land', ('lid', 'areaocc', 'lat', 'long'), ('LD_1321',44.12,28.605548,77.199597))
    insert('land', ('lid', 'areaocc', 'lat', 'long'), ('LD_5412',12.89,28.603212,77.203631))
    insert('land', ('lid', 'areaocc', 'lat', 'long'), ('LD_3498',23.01,28.598238,77.207236))

def insertintoshopv():
    insert('shopvendor', ('svid','svname','scontact','lat','long','authorized'), ('SV_191','Shop Benndor', 9898989898, 28.605133,77.202709,1))
    insert('shopvendor', ('svid','svname','scontact','lat','long','authorized'), ('SV_192','Shop Vendoe', 9898989898, 28.604116,77.204254,1))
    insert('shopvendor', ('svid','svname','scontact','lat','long','authorized'), ('SV_193','Shop LOL', 9898989898, 28.598012,77.204812,0))

def insertintocrop():
    insert('crop', ('cid','cname','units','typeoffarming','quantity','price'), ('C_101','rice','kg','commercial farming',1.6,30))
    insert('crop', ('cid','cname','units','typeoffarming','quantity','price'), ('C_103','cotton','kg','Extensive farming',34.2,10))
    insert('crop', ('cid','cname','units','typeoffarming','quantity','price'), ('C_102','Chicken','kg','poultry farming',39.7,120))
    
def insertintotransporter():
    insert('transporter', ('tid','tname','price','mintwht','maxtwht','resavl','authorized','lat','long'), ('T_101','Hardik Kapoor',1800.00, 100, 1000, 1000, 1,28.593113,77.202516))
    insert('transporter', ('tid','tname','price','mintwht','maxtwht','resavl','authorized','lat','long'), ('T_102','Raunaq Jha',4200.00, 1000, 5000, 5000, 1,28.593867,77.193418))
    insert('transporter', ('tid','tname','price','mintwht','maxtwht','resavl','authorized','lat','long'), ('T_103','Randeep Singh',1300.00, 10, 500, 500, 0,28.594018,77.198825))    

def insertintostorageprov():
    insert('storageprov', ('spid','sname','contact','lat','long','authorized'), ('SP_101', 'Madhav Thakur', 9999999999, 28.615268, 77.193353, 0))
    insert('storageprov', ('spid','sname','contact','lat','long','authorized'), ('SP_102', 'Rajesh Prasad', 9999999888, 28.615155, 77.198460, 1))
    insert('storageprov', ('spid','sname','contact','lat','long','authorized'), ('SP_103', 'Astha Malik', 9997879333, 28.613949, 77.202237, 1))

def insertintosvcrop():
    insert('svcrop', ('svid','cid','amount_bought'), ('C_101','SV_191',100))
    insert('svcrop', ('svid','cid','amount_bought'), ('C_101','SV_192',232))
    insert('svcrop', ('svid','cid','amount_bought'), ('C_102','SV_193',111))
    insert('svcrop', ('svid','cid','amount_bought'), ('C_103','SV_192',111))
    insert('svcrop', ('svid','cid','amount_bought'), ('C_102','SV_191',123))

def insertintoloantrans():
    insert('loantrans', ('lid','transid'), ('L_1586','TR_104'))
    insert('loantrans', ('lid','transid'), ('L_2000','TR_105'))
    insert('loantrans', ('lid','transid'), ('L_2314','TR_106'))

def insertintobankfloan():
    insert('bankfloan', ('lid','bid','fid'), ('L_1586','B_101','F_102'))
    insert('bankfloan', ('lid','bid','fid'), ('L_2000','B_103','F_104'))
    insert('bankfloan', ('lid','bid','fid'), ('L_2314','B_104','F_105'))
    
def insertintotranscrop():
    insert('transcrop', ('tid','cid'), ('T_101','C_101'))
    insert('transcrop', ('tid','cid'), ('T_102','C_102'))
    insert('transcrop', ('tid','cid'), ('T_103','C_103'))
   
def insertintoshopinv():
    insert('shop_inv', ('svid','item_name','item_price','units'), ('SV_191','rice',150.00,100))
    insert('shop_inv', ('svid','item_name','item_price','units'), ('SV_191','Chicken',250.00,123))
    insert('shop_inv', ('svid','item_name','item_price','units'), ('SV_192','rice',100.00,232))
    insert('shop_inv', ('svid','item_name','item_price','units'), ('SV_192','cotton',80.00,111))
    insert('shop_inv', ('svid','item_name','item_price','units'), ('SV_193','rice',300.00,111))

def insertintolandcrop():
    insert('landcrop', ('cid','lid'), ('C_101','LD_1321'))
    insert('landcrop', ('cid','lid'), ('C_102','LD_5412'))
    insert('landcrop', ('cid','lid'), ('C_103','LD_3498'))

def insertintofarmerland():
    insert('farmerland', ('fid','lid'), ('F_102','LD_1321'))
    insert('farmerland', ('fid','lid'), ('F_104','LD_5412'))
    insert('farmerland', ('fid','lid'), ('F_105','LD_3498'))

def insertintofspt():
    insert('fspt', ('transid','fid','spid'), ('TR_101','F_102','SP_101'))
    insert('fspt', ('transid','fid','spid'), ('TR_102','F_104','SP_102'))
    insert('fspt', ('transid','fid','spid'), ('TR_103','F_105','SP_103'))
    
def insertintoftt():
    insert('ftt', ('transid','fid','tid'), ('TR_110','F_102','T_101'))
    insert('ftt', ('transid','fid','tid'), ('TR_111','F_104','T_102'))
    insert('ftt', ('transid','fid','tid'), ('TR_112','F_105','T_103'))

def insertintobank():
    insert('bank', ('bid', 'lat', 'long', 'rateoffr', 'authorized'), ("B_101", 28.614929, 77.217944, 1500, 1))
    insert('bank', ('bid', 'lat', 'long', 'rateoffr', 'authorized'), ("B_103", 28.614062, 77.220604, 2309, 0))
    insert('bank', ('bid', 'lat', 'long', 'rateoffr', 'authorized'), ("B-104", 28.610445, 77.222106, 3400, 1))

def insertintostoragefacloc():
    insert('storagefacloc', ('sid', 'suitcond', 'size', 'unit', 'price', 'lat', 'long', 'typeoffarming', 'spaceleft', 'availability'), ('S_145', 'dry', 146, 'kg', 150, 28.600122, 77.210691, 'poultry', 23, 1))
    insert('storagefacloc', ('sid', 'suitcond', 'size', 'unit', 'price', 'lat', 'long', 'typeoffarming', 'spaceleft', 'availability'), ('S_132', 'room temperature', 2345, 'litre', 450, 28.599218, 77.215326, 'poultry', 300, 0))
    insert('storagefacloc', ('sid', 'suitcond', 'size', 'unit', 'price', 'lat', 'long', 'typeoffarming', 'spaceleft', 'availability'), ('S_123', 'cold', 560, 'kg', 786, 28.594508, 77.215540, 'wheat', '20', 1))

def insertintofsvt():
    insert('fsvt', ('transid', 'fid', 'svid'), ('TR_101', 'F_102', 'SV_191'))
    insert('fsvt', ('transid', 'fid', 'svid'), ('TR_102', 'F_104', 'SV_192'))
    insert('fsvt', ('transid', 'fid', 'svid'), ('TR_103', 'F_105', 'SV_193'))

def insertintospstorage():
    insert('spstorage', ('sid', 'spid'), ('S_145', 'SP_101'))
    insert('spstorage', ('sid', 'spid'), ('S_132', 'SP_102'))
    insert('spstorage', ('sid', 'spid'), ('S_123', 'SP_103'))

def insertintostoragecrop():
    insert('storagecrop', ('sid', 'cid'), ('S_145', 'C_101'))
    insert('storagecrop', ('sid', 'cid'), ('S_132', 'C_102'))
    insert('storagecrop', ('sid', 'cid'), ('S_123', 'C_103'))

# Queries related to the stakeholders
def farmer_nearby_crop_price(crop_name, lat, long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("select price from crop where cname='{}' and cid in (select cid from landcrop where lid in (select lid from land as L where L.lat between {} AND {} and L.long between {} and {}))").format(crop_name,lat_min,lat_max,lon_min,lon_max)
    result = query_db(s)
    return result

def farmer_available_lrates():
    return query_db("select distinct rateoffr from bank")

def farmer_nearby_transport_fac(lat, long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("select * from transporter where transporter.lat between {} and {} and transporter.long between {} and {}").format(lat_min,lat_max,lon_min,lon_max)
    result = query_db(s)
    return result

def farmer_nearby_storage_fac(lat, long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("select * from storagefacloc as D where D.lat between {} and {} and D.long between {} and {}").format(lat_min,lat_max,lon_min,lon_max)
    result = query_db(s)
    return result

def check_farmer():
    print("Farmer : 1 -> nearby price rates of crops")
    print(farmer_nearby_crop_price("rice",30,70))
    print("done")
    print("Farmer : 2 -> available loan rates")
    print(farmer_available_lrates())
    print("done")
    print("Farmer : 3 -> nearby transport facilities")
    print(farmer_nearby_transport_fac(20,70))
    print("done")
    print("Farmer : 4 -> nearby Storage Facilites")
    print(farmer_nearby_storage_fac(20,70))
    print("done")

def bank_no_loan_giv(BID):
    s = "select count(*) from bankfloan as l where l.bid='{}'".format(BID)
    result = query_db(s)
    return result

def bank_number_of_online_trans():
    s = "select count(*) from transactions as t1 where t1.method='Online' "
    result = query_db(s)
    return result

def bank_rate_offr(lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("select bank.rateoffr from bank where bank.lat between {} and {} and bank.long between {} and {}").format(lat_min,lat_max,lon_min,lon_max)
    result = query_db(s)
    return result

def bank_total_pending(BID):
    s = ("select SUM(loan.pendamt) from bankfloan, loan where bankfloan.bid='{}' and loan.lid=bankfloan.lid;").format(BID)
    result = query_db(s)
    return result

def bank_total_lgiven():
    s = "select SUM(iniamt) from loan;"
    result = query_db(s)
    return result
def farmer_removing_land(lid):
    s = "DELETE FROM farmerland WHERE lid='{}';".format(lid)
    s1 = "DELETE FROM landcrop WHERE lid='{}';".format(lid)
    getresult(s)
    getresult(s1)
def farmer_removing_crop(lid,cid):
    s = "DELETE FROM landcrop WHERE lid='{}' and cid='{}';".format(lid,cid)
    getresult(s)
def shopvendor_removing_crop(svid,cid):
    s = "DELETE FROM svcrop WHERE cid='{}' and svid={};".format(cid,svid)
    getresult(s)
def storage_removing_crop(sid,cid):
    s = "DELETE FROM storagecrop WHERE sid='{}' and cid='{}';".formate(sid,cid)
    getresult(s)
def shopvendor_removing_item(item_name,svid):
    s = "DELETE FROM shop_inv WHERE svid='{}' and item_name='{}';".format(svid,item_name)
    getresult(s)
def transporter_removing_crop(tid,cid):
    s = "DELETE FROM transcrop WHERE tid='{}' and cid='{}';".format(tid,cid)
    getresult(s)
def storageprovider_removing_storage_loc(sid,spid):
    s = "DELETE FROM transcrop WHERE sid='{}' and spid='{}';".format(sid,spid)
    getresult(s)
def check_banks():
    print("banks : 1 -> number of loans that have been given out")
    print(bank_no_loan_giv("B_101"))
    print("done")
    print("banks : 2 -> number of online trans")
    print(bank_number_of_online_trans())
    print("done")
    print("banks : 3 -> rates offered by local banks")
    print(bank_rate_offr(20,70))
    print("done")
    print("banks : 4 -> total amount of all pending loans")
    print(bank_total_pending("B_101"))
    print("done")
    print("bank : 5 -> total amount of loans given")
    print(bank_total_lgiven())
    print("done")

def trans_check_auth_req(TID):
    s = ("select authorized from transporter as T where  T.tid ='{}'").format(TID)
    result = query_db(s)
    return result

def trans_prices_offer(weight):
    s = ("select tid,Price*{} from (SELECT tid,Price from transporter where mintwht <= {} and maxtwht >= {})").format(weight,weight,weight)
    result = query_db(s)
    return result

def trans_resources_left(tname):
    s = ("select SUM(resavl) from transporter as A where A.tname='{}'").format(tname)
    result = query_db(s)
    return result

def trans_res_wieght_transport(TID):
    s = ("select maxtwht from transporter as A where A.tid='{}'").format(TID)
    result = query_db(s)
    return result

def check_transporter():
    print("transporter check a")
    print(trans_check_auth_req("T_101"))
    print("done")
    print("transporter check b")
    print(trans_prices_offer(20))
    print("done")
    print("transporter check c")
    print(trans_resources_left('Raunaq Jha'))
    print("done")
    print("transporter check d -> distance in meteres")
    print(trans_dist('F_104', 'F_102'))
    print("done")
    print("transporter check e")
    print(trans_res_wieght_transport("T_101"))
    print("done")

def shopvend_priceofcrop_in_mylocality(crop_name,lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("select item_price from shop_inv where item_name='{}' and svid in ( select svid from shopvendor as A where A.lat between {} and {} and A.long between {} and {})").format(crop_name,lat_min,lat_max,lon_min,lon_max)
    result = query_db(s)
    return result

def shopvend_check_auth(SVID):
    s = ("select authorized from shopvendor where svid='{}'").format(SVID)
    result = query_db(s)
    return result

def shopvend_rates_nearby_forloan(lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("Select bank.rateoffr from bank where bank.lat between {} and {} and bank.long between {} and {}").format(lat_min,lat_max,lon_min,lon_max)

    result = query_db(s)
    return result

def shopvend_inv(SVID):
    s = ("select * from shop_inv where shop_inv.svid='{}'").format(SVID)
    result = query_db(s)
    return result

def count_nonauth(name):
    s = "select count(*) from {} as b where b.authorized=0".format(name)
    res = query_db(s)
    return res[0][0]

def auth_number_non_auth_units():
    ans = count_nonauth("bank")
    ans += count_nonauth("farmer")
    ans += count_nonauth("shopvendor")
    ans += count_nonauth("storageprov")
    return ans

def auth_no_pend_auth():
    s = "select  count(authorized) from (select authorized from shopvendors union all select authorized from storageprov union all select authorized from transporter) where authorized=0"
    res = query_db(s)
    return res

def auth_total_inc_trans():
    s = "select SUM(transactions.amount) from transactions where transactions.method!='Complete'"
    res = query_db(s)
    return res

def auth_rates_off_loc(crop_name,lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = "select c.cid, c.cname, c.units, c.price from crop c inner join landcrop lc on c.cid=lc.cid inner join land l on lc.lid=l.lid inner join farmerland fl on l.lid=fl.lid inner join farmer f on fl.fid=f.fid where f.lat between {} and {} and f.long between {} and {} and c.cname='{}'".format(lat_min,lat_max,lon_min,lon_max,crop_name)
    res = query_db(s)
    return res

def auth_no_inc_trans(lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = " Select count(*) from shopvendor as A where A.lat between {} and {} and A.long between {} and {} ".format(lat_min,lat_max,lon_min,lon_max)
    res = query_db(s)
    return res

def check_authorities():
    print("auth a")
    print(auth_number_non_auth_units())
    print("done")
    print("auth b")
    print(auth_no_pend_auth())
    print("done")
    print("auth c")
    print(auth_total_inc_trans())
    print("done")
    print("auth d")
    print(auth_rates_off_loc("rice",20,70))
    print("done")
    print("auth e")
    print(auth_no_inc_trans(20,70))
    print("done")
    return

def check_shopvendor():
    print("shopvendor a")
    print(shopvend_priceofcrop_in_mylocality("rice",20,70))
    print("done")
    print("shopvendor b")
    print(shopvend_check_auth("SV_191"))
    print("done")
    print("shopvendor c")
    print(shopvend_rates_nearby_forloan(20,70))
    print("done")
    print("shopvendor d")
    print(shopvend_inv("SV_191"))
    print("done")
    return

# Returning lat long from the function
def return_latlong_fromid(id= ''):
    try:
        if id.find('F_')!=-1:
            s = ("select A.lat, A.long from farmer as A where A.fid='{}'").format(id)
            result = query_db(s)
            return result
        elif id.find('LD_')!=-1:
            s = ("select A.lat, A.long from land as A where A.lid='{}'").format(id)
            result = query_db(s)
            return result
        elif id.find('SV_')!=-1:
            s = ("select A.lat, A.long from shopvendor as A where A.svid='{}'").format(id)
            result = query_db(s)
            return result
        elif id.find('SP_')!=-1:
            s = ("select A.lat, A.long from storageprov as A where A.spid='{}'").format(id)
            result = query_db(s)
            return result
    except Exception as e:
        print(e)
        return (0, 0)

# Returning distance between 2 pair of (lat, long)
def trans_dist(idA= '', idB= ''):
    origin1= return_latlong_fromid(idA)
    origin1= origin1[0]
    print('Origin 1 is: ', origin1)
    origin2= return_latlong_fromid(idB)
    origin2= origin2[0]
    print('Origin 2 is: ', origin2)
    R = 6.3781*(10**6)
    lat1, lat2, lon1, lon2= origin1[0], origin2[0], origin1[1], origin2[1]
    φ1 = lat1 * math.pi/180
    φ2 = lat2 * math.pi/180
    Δφ = (lat2-lat1) * math.pi/180
    Δλ = (lon2-lon1) * math.pi/180
    a = math.sin(Δφ/2) * math.sin(Δφ/2) + math.cos(φ1) * math.cos(φ2) * math.sin(Δλ/2) * math.sin(Δλ/2); 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R*c
    return d

def getresult(s):
    return query_db(s)

def storage_provider_auth():
    s = ("select count(*) from storageprov where authorized=0")
    result = getresult(s)
    l = [0,0]
    l[0] = result[0][0]
    s = ("select count(*) from storageprov  where authorized=1")
    result = getresult(s)
    l[1] = result[0][0]
    pieChart(["authorized","not_authorized"],l,"storage_provider_auth")
    return "storage_provider_auth_pie.png"

def shopvendor_auth():
    s = ("select count(*) from shopvendor where authorized=0")
    result = getresult(s)
    l = [0,0]
    l[0] = result[0][0]
    s = ("select count(*) from shopvendor where authorized=1")
    result = getresult(s)
    l[1] = result[0][0]
    total = l[0] + l[1]
    pieChart(["authorized","unauthorized"], l, "shopvendor_auth")
    return "shopvendor_auth_pie.png"

def crop_sum():
    s = ("select cname from crop")
    res = getresult(s)
    ret = []
    for i in res:
        c_name = i[0]
        s = ("select sum(quantity) from crop where cname='{}'").format(c_name)
        res1 = getresult(s)
        ret.append([c_name,res1[0][0]])
    Xs = []
    Ys = [[]]
    for i in ret:
        Xs.append(i[0])
        Ys[0].append(i[1])
    print(Xs,Ys)
    barGraph(Xs,Ys[0],"Crop_name","quantity_sum","crop_quantity")
    return "crop_quantity_bar.png"

def crop_price(index):
    s = ("select cname from crop")
    res = getresult(s)
    ret = []
    for i in res:
        c_name = i[0]
        s = stdev_quantity(c_name)
        add = []
        s = ("select sum(price) from crop where cname='{}'").format(c_name)
        res1 = getresult(s)
        s = ("select count(*) from crop where cname='{}'").format(c_name)
        res2 = getresult(s)
        len2 = res2[0][0]
        mean1 = res1[0][0]/res2[0][0]
        add.append(c_name)
        s = ("select quantity from crop where cname='{}'").format(c_name)
        res1 = getresult(s)
        stdev = 0
        for j in res1:
            stdev += (j[0] - mean1)**2/(len2)
        stdev = stdev**(0.5)
        add.append(stdev)
        add.append(mean1)
        add.append(stdev**2)
        ret.append(add)
    Xs = []
    Ys = [[],[],[],[]]
    print(Ys)
    for i in ret:
        print(i)
        Xs.append(i[0])
        Ys[0].append(i[1])
        Ys[1].append(i[2])
        Ys[2].append(i[3])
    ylabel = ""
    if(index == 0):
        ylabel = "stdev"
    elif(index == 1):
        ylabel = "mean"
    else:
        ylabel = "variance"
    barGraph(Xs,Ys[index],"bid",ylabel,"crop_price_" + ylabel)
    return "crop_price_" + ylabel + "_bar.png"

def shop_inv(SVID):
    s = ("select item_name,units from shop_inv where svid='{}'").format(SVID)
    res = getresult(s)
    Xs = []
    Ys = []
    for i in res:
        sum1 = 0
        cnt = 0
        for j in res:
            if(j[0] == i[0]):
                sum1 += j[1]
                cnt += 1
        Ys.append(sum1)
        Xs.append(i[0])
    pieChart(Xs,Ys,"shopvendor_item_mean")
    return "shopvendor_item_mean_pie.png"

def bank_rateofff(index):
    s = ("select bid from bank")
    res = getresult(s)
    ret = []
    for i in res:
        bank_id = i[0]
        s = stdev_rate(bank_id)
        add = []
        s = ("select sum(rateoffr) from bank where bid='{}'").format(bank_id)
        res1 = getresult(s)
        s = ("select count(*) from bank where bid='{}'").format(bank_id)
        res2 = getresult(s)
        len2 = res2[0][0]
        mean1 = res1[0][0]/res2[0][0]
        add.append(bank_id)
        s = ("select rateoffr from bank where bid='{}'").format(bank_id)
        res1 = getresult(s)
        stdev = 0
        for j in res1:
            stdev += (j[0] - mean1)**2/(len2)
        stdev = stdev**(0.5)
        add.append(stdev)
        add.append(mean1)
        add.append(stdev**2)
        ret.append(add)
    Xs = []
    Ys = [[],[],[],[]]
    print(Ys)
    for i in ret:
        Xs.append(i[0])
        # print(i)
        Ys[0].append(i[1])
        Ys[1].append(i[2])
        Ys[2].append(i[3])
    ylabel = ""
    if(index == 0):
        ylabel = "stdev"
    elif(index == 1):
        ylabel = "mean"
    else:
        ylabel = "variance"
    barGraph(Xs,Ys[index],"bid",ylabel,"bank_rateoff_" + ylabel)
    return "bank_rateoff_" + ylabel + "_bar.png"