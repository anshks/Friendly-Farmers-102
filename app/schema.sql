DROP TABLE IF EXISTS farmer;
DROP TABLE IF EXISTS land;
DROP TABLE IF EXISTS farmerland;
DROP TABLE IF EXISTS crop;
DROP TABLE IF EXISTS landcrop;
DROP TABLE IF EXISTS shopvendors;
DROP TABLE IF EXISTS svcrop;

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