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
    printalltables()
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
        insertintofarmer()
        # print(db)


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

def printalltables():
    alltables= query_db("Select * from farmer")
    print(alltables)
    return alltables

def insertintofarmer():
    insert('farmer', ('fid', 'fname', 'fcontact', 'faddress'), ('UNIQUE', 'Farmer', 9811308881, 'LOL'))


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
