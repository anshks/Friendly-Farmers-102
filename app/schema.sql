DROP TABLE IF EXISTS farmer;
DROP TABLE IF EXISTS land;
DROP TABLE IF EXISTS farmerland;
DROP TABLE IF EXISTS crop;
DROP TABLE IF EXISTS landcrop;
DROP TABLE IF EXISTS shopvendors;
DROP TABLE IF EXISTS svcrop;
DROP TABLE IF EXISTS storagecrop;
DROP TABLE IF EXISTS shopinv;
DROP TABLE IF EXISTS transporters;
DROP TABLE IF EXISTS ftt;
DROP TABLE IF EXISTS fsvt;
DROP TABLE IF EXISTS transcrop;
DROP TABLE IF EXISTS fspt;
DROP TABLE IF EXISTS storageprov;
DROP TABLE IF EXISTS spstorage;
DROP TABLE IF EXISTS trasaction;
DROP TABLE IF EXISTS bankfloan;
DROP TABLE IF EXISTS loan;
DROP TABLE IF EXISTS storagefacloc;
DROP TABLE IF EXISTS bank;
DROP TABLE IF EXISTS loantrans;

CREATE TABLE IF NOT EXISTS farmer
(
  fid           string not null,
  fname         string not null,
  fcontact      integer(10) not null,
  faddress      string not null,
  authorized    boolean default false,
  primary key (fid)
);

CREATE TABLE IF NOT EXISTS land
(
  lid             string not null,
  areaocc         decimal not null,
  lat             decimal not null,
  long            decimal not null,
  primary key (lid)
);

CREATE TABLE IF NOT EXISTS farmerland
(
  fid             string not null,
  lid             string not null,
  primary key (fid, lid)
);

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

CREATE TABLE IF NOT EXISTS landcrop
(
  cid             string not null,
  lid             string not null,
  primary key (cid, lid)
);

CREATE TABLE IF NOT EXISTS shopvendors
(
  svid              string not null,
  svaddress         string not null,
  authorized        boolean default false
  primary key (svid)
);

CREATE TABLE IF NOT EXISTS svcrop
(
  svid              string not null,
  cid               string not null,
  amount_bought     decimal not null
  primary key (svid, cid)
);

CREATE TABLE IF NOT EXISTS shop_inv
(
  svid              string not null,
  cid               string not null,
  amount_bought     decimal not null
  primary key (svid, cid)
);
//dont know

CREATE TABLE IF NOT EXISTS Storagecrop
(
  sid               string not null,
  cid               string not null
  primary key (sid,cid)
);

CREATE TABLE IF NOT EXISTS shopinv
(
  svid              string not null,
  itemno            string not null,
  itempri           string not null,
  units             string not null 
  primary key (svid,itemno)
);

CREATE TABLE IF NOT EXISTS transporters
(
  tid               string not null,
  price             decimal not null,
  mintwht           decimal not null,
  maxtwht           decimal not null,
  resavl            string not null,
  authorized        boolean default false
  primary key (tid)
);

CREATE TABLE IF NOT EXISTS ftt
(
  transid            string not null,
  fid                string not null,
  tid                string not null
  primary key (transid)
);

CREATE TABLE IF NOT EXISTS fsvt
(
  transid            string not null,
  fid                string not null,
  svid               string not null
  primary key (transid)
);

CREATE TABLE IF NOT EXISTS transcrop
(
  tid                string not null,
  cid                string not null
  primary key (tid,cid)
);

CREATE TABLE IF NOT EXISTS fspt
(
  transid            string not null,
  fid                string not null,
  spid               string not null
  primary key (transid)
);

CREATE TABLE IF NOT EXISTS storageprov
(
  spid               string not null,
  name               string not null,
  contact            integer(10) not null,
  lat                decimal not null,
  long               decimal not null,
  authorized         boolean default false
  primary key (spid)
);

CREATE TABLE IF NOT EXISTS spstorage
(
  sid                string not null,
  spid               string not null
  primary key (sid)
);

CREATE TABLE IF NOT EXISTS trasaction
(
  transid            string not null,
  amount             decimal not null,
  moneyspt           decimal not null,
  stage              string not null
  primary key (transid)
);

CREATE TABLE IF NOT EXISTS bankfloan
(
  lid                string not null,
  bid                string not null,
  fid                string not null
  primary key (lid)
);

CREATE TABLE IF NOT EXISTS loan
(
  lid                string not null,
  rateoffr           decimal not null,
  dateoffr           date not null,
  offrto             string not null,
  iniamt             decimal not null,
  pendamt            decimal not null
  primary key (lid)
);

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
  availability       boolean default false
  primary key (sid)
);

CREATE TABLE IF NOT EXISTS bank
(
  bid                string not null,
  lat                decimal not null,
  long               decimal not null,
  rateoffr           decimal not null,
  authorized         boolean default false
  primary key (bid)
);

CREATE TABLE IF NOT EXISTS loantrans
(
  lid                string not null,
  transid            string not null
  primary key (lid,transid)
);






CREATE TABLE IF NOT EXISTS execution
(
  shortcut string not null references lecture (shortcut),
  semester integer default 1,
  lecturer string,
  primary key (shortcut, semester)
);

CREATE TABLE IF NOT EXISTS exam
(
  shortcut string not null,
  semester integer default 1,
  n_tries  integer default 1,
  mark     integer,
  degree   string  default 'b' check (degree = 'b' or degree = 'm'),
  kind     integer default 0 check (kind >= 0 and kind < 2),
  primary key (shortcut, semester, n_tries),
  foreign key (shortcut, semester) references execution (shortcut, semester)

);