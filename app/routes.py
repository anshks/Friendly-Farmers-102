from app import (
    app,
)
from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    g
)
from app.forms import (
    AddLectureForm,
    AddExecutionForm,
    AddExamForm
)
from app.query_helper import (
    query_db,
    insert,
    Pagination
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lecture', methods=('GET', 'POST'))
def add_lecture():
    form = AddLectureForm()

    if form.validate_on_submit():
        insert('lecture',
               ('name', 'shortcut', 'ects'),
               (form.name.data, form.shortcut.data, form.ects.data))

        flash("Successfully added new lecture {}!".format(form.name.data))
        return redirect(url_for('add_lecture'))

    return render_template('add_lecture.html',
                           title="Lectures",
                           form=form
                           )


@app.route('/exams/', defaults={'page': 1}, methods=('GET', 'POST'))
@app.route('/exams/page/<int:page>', methods=('GET', 'POST'))
def view_exams(page):
    total_count = query_db(
        "select count(shortcut) from exam", one=True)[0]

    pagination = Pagination(page, total_count, per_page=3)

    exams = query_db(
        "select shortcut, name, semester, n_tries, mark, degree,kind "
        "from exam join lecture using (shortcut) order by shortcut,semester,n_tries limit ?,?",
        ((page - 1) * pagination.per_page, pagination.per_page))

    next_page = url_for('view_exams', page=page + 1) if pagination.has_next else None
    prev_page = url_for('view_exams', page=page - 1) if pagination.has_prev else None

    return render_template('view_exams.html',
                           exams=exams,
                           next_page=next_page,
                           prev_page=prev_page,
                           title="Exams"
                           )


@app.route('/add_exam', methods=('GET', 'POST'))
def add_exam():
    form = AddExamForm()
    executions = query_db("select shortcut, semester from execution")
    form.executions.choices = [('?'.join(map(str, k)), "{} in semester {}".format(*k)) for k in executions]

    if form.validate_on_submit():
        shortcut, semester = form.executions.data.split('?')
        if len(query_db("select 1 from exam where shortcut=? and semester=? and n_tries=?",
                        (shortcut, semester, form.n_tries.data))) > 0:
            flash("Exam already exists!")
            return redirect(url_for('add_exam'))

        insert('exam',
               ('shortcut', 'semester', 'n_tries', 'mark', 'degree', 'kind'),
               (shortcut, semester, form.n_tries.data, form.mark.data,
                form.degree.data,
                form.kind.data))

        flash("Successfully added exam {}!".format(shortcut))
        return redirect(url_for('view_exams'))

    return render_template('add_exam.html',
                           title="Exams",
                           form=form
                           )


@app.route('/execution', methods=('GET', 'POST'))
def add_execution():
    form = AddExecutionForm()
    lectures = query_db("select shortcut,name from lecture")
    form.shortcut.choices = [(k[0], k[1]) for k in lectures]

    if form.validate_on_submit():
        # insert
        insert('execution',
               ('shortcut', 'lecturer', 'semester'),
               (form.shortcut.data, form.lecturer.data, form.semester.data))
        flash("Successfully added execution!")
        return redirect(url_for('add_execution'))

    return render_template('add_execution.html',
                           title="Executions",
                           form=form)


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
