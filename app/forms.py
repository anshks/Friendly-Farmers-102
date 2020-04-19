from flask_wtf import (
    FlaskForm
)
from wtforms import (
    StringField,
    IntegerField,
    SubmitField,
    SelectField
)
from wtforms.validators import (
    DataRequired,
    Length,
    ValidationError
)
from app.query_helper import (
    query_db
)


class AddLectureForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 1024)])
    shortcut = StringField('Shortcut', validators=[DataRequired(), Length(1, 64)])
    ects = IntegerField('ECTS', default=1, validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_shortcut(self, shortcut):
        if len(query_db("select * from lecture where shortcut= ? ", (shortcut.data,))) > 0:
            raise ValidationError("Shortcut {} already exists!".format(shortcut.data))


class AddExecutionForm(FlaskForm):
    shortcut = SelectField('Shortcut', coerce=str, validators=[DataRequired()])
    lecturer = StringField('Lecturer', validators=[DataRequired()])
    semester = IntegerField('Semester', default=1, validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddExamForm(FlaskForm):
    executions = SelectField('Execution', coerce=str, validators=[DataRequired()])
    n_tries = IntegerField('Try', default=1, validators=[DataRequired()])
    mark = IntegerField('Grade', validators=[DataRequired()])
    degree = SelectField('Degree', default='b', choices=[('b', 'Bachelor'), ('m', 'Master')])
    kind = SelectField('Kind', coerce=int, default=0, choices=[(0, 'written'), (1, 'oral')])
    submit = SubmitField('Submit')
