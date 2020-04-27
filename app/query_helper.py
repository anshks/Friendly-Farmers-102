import sqlite3, geopy
from app import ( app )
from flask import ( current_app, g )
from math import ( ceil )
from geopy.geocoders import ( Nominatim )
nom = Nominatim()

def address_to_latlong(address):
	result = nom.geocode(address)
	lat = result.latitude
	long = result.longitude
	return [lat, long]

def latlong_to_address(lat,long):
	address = nom.reverse(str(lat) + ',' + str(long))
	return address

# Basic database helper methods
# Establishing connection with db
def get_db():
    """
    get database connection
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config['DATABASE_PATH'])
    return db

# Executing queries
def query_db(query, args=(), one=False):
    """
    execute a database query
    :param query: query string
    :param args: optional query arguments
    :param one: limit result to 1
    :return: query result
    """
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# Inserting queries
def insert(table, fields=(), values=()):
    """
    insert new row into an existing table
    :param table: target table
    :param fields: field names
    :param values: row values
    :return: id of the newly created row
    """
    # g.db is the database connection
    db = get_db()
    cur = db.cursor()
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (
        table,
        ', '.join(fields),
        ', '.join(['?'] * len(values))
    )
    print('Executing insert query for', table, '\n')
    cur.execute(query, values)
    db.commit()
    id = cur.lastrowid
    cur.close()
    print('Inserted the query for', table, '\n')
    return id

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
        create_the_databse();
        print('\n\n> Created the database')
        print(query_db("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';"), '\n')
        check_farmer()
        check_banks()
        check_transporters()
        check_authorities()
        check_shopvendor()
def create_the_databse():
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
    insertintotransporters()
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

# pagination

class Pagination:

    def __init__(self, page: int, total_count: int, per_page: int = None):
        self.page = page
        self.total_count = total_count
        conf_per_page = current_app.config['PER_PAGE'] if current_app.config['PER_PAGE'] is not None else 15
        self.per_page = conf_per_page if per_page is None else per_page

    @property
    def pages(self) -> int:
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self) -> bool:
        return self.page > 1

    @property
    def has_next(self) -> bool:
        return True if self.page < self.pages else False

    def iter(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or (num > self.page - left_current - 1):
                if num < self.page + right_current or num > self.pages - right_edge:
                    if last + 1 != num:
                        yield None
                    yield num
                    last = num


# special queries

def printalltables(table):
    alltables= query_db("Select * from "+table)
    print(alltables)
    return alltables

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
    insert('shopvendor', ('svid','lat','long','authorized'), ('SV_191',28.605133,77.202709,1))
    insert('shopvendor', ('svid','lat','long','authorized'), ('SV_192',28.604116,77.204254,1))
    insert('shopvendor', ('svid','lat','long','authorized'), ('SV_193',28.598012,77.204812,0))

def insertintocrop():
    insert('crop', ('cid','cname','units','typeoffarming','quantity','price'), ('C_101','rice','kg','commercial farming',1.6,30))
    insert('crop', ('cid','cname','units','typeoffarming','quantity','price'), ('C_103','cotton','kg','Extensive farming',34.2,10))
    insert('crop', ('cid','cname','units','typeoffarming','quantity','price'), ('C_102','Chicken','kg','poultry farming',39.7,120))
    
def insertintotransporters():
    insert('transporter', ('tid','tname','price','mintwht','maxtwht','resavl','authorized','lat','long'), ('T_101','Hardik Kapoor',1800.00, 100, 1000, 1000, 1,28.593113,77.202516))
    insert('transporter', ('tid','tname','price','mintwht','maxtwht','resavl','authorized','lat','long'), ('T_102','Raunaq Jha',4200.00, 1000, 5000, 5000, 1,28.593867,77.193418))
    insert('transporter', ('tid','tname','price','mintwht','maxtwht','resavl','authorized','lat','long'), ('T_103','Randeep Singh',1300.00, 10, 500, 500, 0,28.594018,77.198825))    

def insertintostorageprov():
    insert('storageprov', ('spid','sname','contact','lat','long','authorized'), ('SP_101', 'Madhav Thakur', 9999999999, 28.615268, 77.193353, 1))
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

def farmer_nearby_crop_price(crop_name,lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("select price from crop where cname='{}' and cid in (select cid from landcrop where lid in (select lid from land as L where L.lat between {} AND {} and L.long between {} and {}))").format(crop_name,lat_min,lat_max,lon_min,lon_max)
    result = query_db(
        s
        )
    return result

def farmer_available_lrates():
    return query_db("select distinct rateoffr from bank")

def farmer_nearby_transport_fac(lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("select * from transporter where transporter.lat between {} and {} and transporter.long between {} and {}").format(lat_min,lat_max,lon_min,lon_max)
    result = query_db(
        s
        )
    return result

def farmer_nearby_storage_fac(lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("select * from storagefacloc as D where D.lat between {} and {} and D.long between {} and {}").format(lat_min,lat_max,lon_min,lon_max)
    result = query_db(
        s
        )
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

    s = "select count(*) from bankfloan as l where l.bid='{}'".format(BID);
    # print(s)
    result = query_db(
        s
        )
    return result

def bank_number_of_online_trans():
    s = "select count(*) from transactions as t1 where t1.method='Online' ";
    # print(s)
    result = query_db(
        s
        )
    return result

def bank_rate_offr(lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("select bank.rateoffr from bank where bank.lat between {} and {} and bank.long between {} and {}").format(lat_min,lat_max,lon_min,lon_max)
    result = query_db(
        s
        )
    return result

def bank_total_pending(BID):
    s = ("select SUM(pendamt) from bankloan,loan where bankloan.bid='{}' and loan.lid=bankloan.lid").format(BID)
    result = query_db(
        s
        )
    return result

def bank_total_lgiven():
    s = "select SUM(iniamt) from loan;"
    result = query_db(
        s
        )
    return result

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
    s = ("select authorized from transporters as T where  T.tid ='{}'").format(TID)
    result = query_db(
        s
        )
    return result
def trans_prices_offer(weight):
    s = ("select tid,Price*{} from (SELECT tid,Price from transporters where mintwht <= {} and maxtwht >= {})").format(weight,weight,weight)
    result = query_db(
        s
        )
    return result
def trans_resources_left():
    return
def trans_dist():
    return
def trans_res_wieght_transport(TID):
    s = ("select maxtwht from transporters as A where A.tid='{}'").format(TID)
    result = query_db(
        s
        )
    return result
def check_transporters():
    print("transporters check a")
    print(trans_check_auth_req("T_101"))
    print("done")
    print("transporters check b")
    print(trans_prices_offer(20))
    print("done")
    print("transporter check c")
    print(trans_resources_left())
    print("done")
    print("transporter check d")
    print(trans_dist())
    print("done")
    print("transporters check e")
    print(trans_res_wieght_transport("T_101"))
    print("done")

def shopvend_priceofcrop_in_mylocality(crop_name,lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("select item_price from shop_inv where item_name='{}' and svid in ( select svid from shopvendor as A where A.lat between {} and {} and A.long between {} and {})").format(crop_name,lat_min,lat_max,lon_min,lon_max)
    result = query_db(
        s
        )
    return result
def shopvend_check_auth(SVID):
    s = ("select authorized from shopvendor where svid='{}'").format(SVID)
    result = query_db(
        s
        )
    return result
def shopvend_rates_nearby_forloan(lat,long):
    lat_max = lat + 20
    lat_min = lat - 20
    lon_min = long - 20
    lon_max = long + 20
    s = ("Select bank.rateoffr from bank where bank.lat between {} and {} and bank.long between {} and {}").format(lat_min,lat_max,lon_min,lon_max)

    result = query_db(
        s
        )
    return result
def shopvend_inv(SVID):
    s = ("select * from shop_inv where shop_inv.svid='{}'").format(SVID)
    result = query_db(
        s
        )
    return result
def shopvend_printstate():
    return
def count_nonauth(name):
    s = "select count(*) from {} as b where b.authorized=0".format(name)
    res = query_db(s)
    return res[0][0]
def auth_number_non_auth_units():
    ans = count_nonauth("bank")
    ans += count_nonauth("farmer")
    ans += count_nonauth("shopvendor")
    ans += count_nonauth("storageprov")
    return ans;
def auth_no_pend_auth():
    s = "select  count(authorized) from (select authorized from shopvendors union all select authorized from storageprov union all select authorized from transporters) where authorized=0"
    res = query_db(s)
    return res;
def auth_total_inc_trans():
    s = "select SUM(transactions.amount) from transactions where transactions.method!='Complete'"
    res = query_db(s)
    return res;
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
    return res;

def check_authorities():
    print("auth a")
    print(auth_number_non_auth_units())
    print("done")
    print("auth b")
    print(auth_no_pend_auth())
    print("done")
    print("auth c")
    print(auth_total_inc_trans());
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
    print("shopvendor e")
    print(shopvend_printstate())
    print("done")
    return
def get_avg_mark_per_degree():
    """
    Get weighted average mark across all exams that belong to a specific degree.
    """
    avg_mark_per_degree = query_db(
        "select degree, round((sum(mark * ects) * 1.0) / sum(ects), 1) from exam "
        "join lecture using (shortcut) group by degree")
    return avg_mark_per_degree


def get_lecturer_with_lowest_avg_mark():
    """
    Get lecturer with best (=lowest) average marks.
    """
    best_lecturer = query_db(
        "select lecturer, min(average) from execution join "
        "(select shortcut, avg(mark) as average from exam group by shortcut) temp "
        "using(shortcut);")

    return best_lecturer


def get_semester_with_lowest_avg_mark(title):
    best_semester = query_db(
        "select semester, avg(mark) from exam join lecture using(shortcut)"
        "where lecture.name =? group by semester limit 1;", [title])

    return best_semester
