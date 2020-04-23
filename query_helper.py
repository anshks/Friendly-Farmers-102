from app import (
    app
)
from flask import (
    current_app,
    g
)
from math import (
    ceil
)

import sqlite3


# Basic database helper methods

def get_db():
    """
    get database connection
    """
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config['DATABASE_PATH'])
    return db


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
    cur.execute(query, values)
    db.commit()
    id = cur.lastrowid
    cur.close()
    # printalltables()
    return id


def init_db():
    """
    initialize a database
    created a database schema according to schema.sql
    """
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            store= f.read()
            db.cursor().executescript(store)
        db.commit()
        insertintotrasaction()
        insertintoloan()
        printalltables('loan')
        printalltables('trasaction')
        insertintofarmer()
        insertintoland()
        printalltables('farmer')
        printalltables('land')


        



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
    insert('trasaction', ('transid', 'amount', 'moneyspt', 'stage'), ('T_101', 15000.00, 10000.00, 'Overdue'))
    insert('trasaction', ('transid', 'amount', 'moneyspt', 'stage'), ('T_102', 120000.00, 50000.00, 'Complete'))
    insert('trasaction', ('transid', 'amount', 'moneyspt', 'stage'), ('T_103', 100000.00,  0.00, 'Active'))

def insertintoloan():
    insert('loan', ('lid', 'rateoffr', 'dateoffr', 'offrto', 'iniamt', 'pendamt'), ('L_1586', 10.35, '22-04-10', 'F_102', 13500.00, 11000.00))
    insert('loan', ('lid', 'rateoffr', 'dateoffr', 'offrto', 'iniamt', 'pendamt'), ('L_2000', 8.00, '10-04-10', 'F_104', 50000.00, 49000.00))
    insert('loan', ('lid', 'rateoffr', 'dateoffr', 'offrto', 'iniamt', 'pendamt'), ('L_2314', 9.35, '18-04-10', 'F_105', 20500.00, 20500.00))

def insertintofarmer():
    insert('farmer', ('fid', 'fname', 'fcontact', 'faddress', 'authorized'), ('F_102','Ramu',9997712345,'12/a kanpur',1))
    insert('farmer', ('fid', 'fname', 'fcontact', 'faddress', 'authorized'), ('F_104','Sahu',9412345678,'1/12 Pauri',0))
    insert('farmer', ('fid', 'fname', 'fcontact', 'faddress', 'authorized'), ('F_105','Sid',7771122333,'4A udaynagar',1))

def insertintoland():
    insert('trasaction', ('lid', 'areaocc', 'lat', 'long'), ('LD_1321',44.12,26.4499,80.3319))
    insert('trasaction', ('lid', 'areaocc', 'lat', 'long'), ('LD_5412',12.89,29.8688,78.8383))
    insert('trasaction', ('lid', 'areaocc', 'lat', 'long'), ('LD_3498',23.01,24.5854,73.7125))

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
