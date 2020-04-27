DROP TABLE IF EXISTS farmer;
CREATE TABLE IF NOT EXISTS farmer
(
  fid               string not null,
  fname             string not null,
  fcontact          integer(10) not null,
  lat               decimal not null,
  long              decimal not null,
  authorized        boolean default false,
  primary key ( fid )
);

DROP TABLE IF EXISTS land;
CREATE TABLE IF NOT EXISTS land
(
  lid               string not null,
  areaocc           decimal not null,
  lat               decimal not null,
  long              decimal not null,
  primary key ( lid )
);

DROP TABLE IF EXISTS farmerland;
CREATE TABLE IF NOT EXISTS farmerland
(
  fid              string not null,
  lid              string not null,
  primary key ( fid , lid ),
  foreign key ( fid ) references farmer ( fid ),
  foreign key ( lid ) references land ( lid )
);

DROP TABLE IF EXISTS crop;
CREATE TABLE IF NOT EXISTS crop
(
  cid               string not null,
  cname             string not null,
  units             string not null,
  typeoffarming     string not null,
  quantity          decimal not null,
  price             decimal not null,
  primary key (cid)
);

DROP TABLE IF EXISTS landcrop;
CREATE TABLE IF NOT EXISTS landcrop
(
  cid               string not null,
  lid               string not null,
  primary key ( cid , lid ),
  foreign key ( lid ) references land ( lid ),
  foreign key ( cid ) references crop ( cid )
);

DROP TABLE IF EXISTS shopvendor;
CREATE TABLE IF NOT EXISTS shopvendor
(
  svid              string not null,
  lat               decimal not null,
  long              decimal not null,
  authorized        boolean default false,
  primary key (svid)
);

DROP TABLE IF EXISTS svcrop;
CREATE TABLE IF NOT EXISTS svcrop
(
  svid              string not null,
  cid               string not null,
  amount_bought     decimal not null,
  primary key ( svid , cid )
  foreign key ( svid ) references shopvendor ( svid ), 
  foreign key ( cid ) references crop ( cid )
);

DROP TABLE IF EXISTS storagecrop;
CREATE TABLE IF NOT EXISTS storagecrop
(
  sid               string not null,
  cid               string not null,
  primary key ( sid , cid ),
  foreign key ( sid ) references storageprov ( sid ),
  foreign key ( cid ) references crop ( cid )
);

DROP TABLE IF EXISTS shop_inv;
CREATE TABLE IF NOT EXISTS shop_inv
(
  svid              string not null,
  item_name         string not null,
  item_price        decimal not null,
  units             decimal not null,
  primary key ( svid , item_name ),
  foreign key ( svid ) references shopvendor ( svid )
);

DROP TABLE IF EXISTS transporter;
CREATE TABLE IF NOT EXISTS transporter
(
  tid               string not null,
  tname             string not null,
  price             decimal not null,
  mintwht           decimal not null,
  maxtwht           decimal not null,
  lat               decimal not null,
  long              decimal not null,
  resavl            decimal not null,
  authorized        boolean default false,
  primary key (tid)
);

DROP TABLE IF EXISTS ftt;
CREATE TABLE IF NOT EXISTS ftt
(
  transid            string not null,
  fid                string not null,
  tid                string not null,
  primary key (transid),
  foreign key (fid) references farmer (fid),
  foreign key (tid) references transporters (tid)
);

DROP TABLE IF EXISTS fsvt;
CREATE TABLE IF NOT EXISTS fsvt
(
  transid            string not null,
  fid                string not null,
  svid               string not null,
  primary key (transid),
  foreign key (fid) references farmer (fid),
  foreign key (svid) references shopvendor (svid)
);

DROP TABLE IF EXISTS transcrop;
CREATE TABLE IF NOT EXISTS transcrop
(
  tid                string not null,
  cid                string not null,
  primary key (tid,cid),
  foreign key (tid) references transporters (tid),
  foreign key (cid) references crop (cid)
);

DROP TABLE IF EXISTS fspt;
CREATE TABLE IF NOT EXISTS fspt
(
  transid            string not null,
  fid                string not null,
  spid               string not null,
  primary key (transid),
  foreign key (fid) references farmer (fid),
  foreign key (spid) references storageprov (spid) 
);

DROP TABLE IF EXISTS storageprov;
CREATE TABLE IF NOT EXISTS storageprov
(
  spid               string not null,
  sname              string not null,
  contact            integer(10) not null,
  lat                decimal not null,
  long               decimal not null,
  authorized         boolean default false,
  primary key (spid)
);

DROP TABLE IF EXISTS spstorage;
CREATE TABLE IF NOT EXISTS spstorage
(
  sid                string not null,
  spid               string not null,
  primary key (sid),
  foreign key (sid) references storagefacloc (sid),
  foreign key (spid) references storageprov (spid) 
);

DROP TABLE IF EXISTS transactions;
CREATE TABLE IF NOT EXISTS transactions
(
  transid            string not null,
  amount             decimal not null,
  method             string not null,
  primary key (transid)
);

DROP TABLE IF EXISTS bank;
CREATE TABLE IF NOT EXISTS bank
(
  bid                string not null,
  lat                decimal not null,
  long               decimal not null,
  rateoffr           decimal not null,
  authorized         boolean default false,
  primary key (bid)
);

DROP TABLE IF EXISTS bankfloan;
CREATE TABLE IF NOT EXISTS bankfloan
(
  lid                string not null,
  bid                string not null,
  fid                string not null,
  primary key (lid),
  foreign key (bid) references bank (bid),
  foreign key (fid) references farmer(fid)
);

DROP TABLE IF EXISTS loan;
CREATE TABLE IF NOT EXISTS loan
(
  lid                string not null,
  rateoffr           decimal not null,
  dateoffr           date not null,
  offrto             string not null,
  iniamt             decimal not null,
  pendamt            decimal not null,
  primary key (lid)
);

DROP TABLE IF EXISTS storagefacloc;
CREATE TABLE IF NOT EXISTS storagefacloc
(
  sid                string not null,
  suitcond           string not null,
  size               decimal not null,
  unit               string not null,
  price              decimal not null,
  lat                decimal not null,
  long               decimal not null,
  typeoffarming      string not null,
  spaceleft          decimal not null,
  availability       boolean default false,
  primary key (sid)
);

DROP TABLE IF EXISTS loantrans;
CREATE TABLE IF NOT EXISTS loantrans
(
  lid                string not null,
  transid            string not null,
  primary key (lid, transid),
  foreign key (lid) references loan (lid),
  foreign key (transid) references trasaction (transid)
);