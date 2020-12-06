from wtforms import Form, StringField, TextAreaField, validators


class SubmissionForm(Form):
    genres = StringField('Genres', [validators.Length(min=5, max=100)])
    prodComp = StringField('prodComp', [validators.Length(min=0, max=200)])
    prodCont = StringField('prodCont', [validators.Length(min=0, max=200)])
    new_Key = StringField('New Key', [validators.Length(min=0, max=100)])
    percent_Profit = StringField('percent_Profit', [validators.Length(min=0, max=20)])
    good_Movie = StringField('good_Movie', [validators.Length(min=0, max=20)])