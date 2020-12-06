from wtforms import Form, StringField, TextAreaField, validators, SelectField


class SubmissionForm(Form):
    # genres = StringField('Genres', [validators.Length(min=5, max=100)])
    genres = SelectField('Genres', choices=[('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Family', 'Family'), ('Adventure', 'Adventure'), ('Fantasy', 'Fantasy'), ('Romance', 'Romance'), ('Drama', 'Drama'), ('Action', 'Action'), ('Crime', 'Crime'), ('Thriller', 'Thriller'), ('Horror', 'Horror'), ('History', 'History'), ('Mystery', 'Mystery'), ('War', 'War'), ('Foreign', 'Foreign'), ('Music', 'Music'), ('Documentary', 'Documentary'), ('Western', 'Western')])
    prodComp = StringField('prodComp', [validators.Length(min=0, max=200)])
    prodCont = StringField('prodCont', [validators.Length(min=0, max=200)])
    new_Key = StringField('New Key', [validators.Length(min=0, max=100)])
    percent_Profit = StringField('percent_Profit', [validators.Length(min=0, max=10)])
    percent_Profit = SelectField('percent_Profit', choices=[('(10.635, 6552255.0]', '(10.635, 6552255.0]'), ('(2.223, 2.531]', '(2.223, 2.531]'), ('(0.531, 0.707]', '(0.531, 0.707]'), ('(1.252, 1.509]', '(1.252, 1.509]'), ('(-0.0009794, 0.19]', '(-0.0009794, 0.19]'), ('(3.614, 4.227]', '(3.614, 4.227]'), ('(3.176, 3.614]', '(3.176, 3.614]'), ('(2.852, 3.176]', '(2.852, 3.176]'), ('(2.531, 2.852]', '(2.531, 2.852]'), ('(2.004, 2.223]', '(2.004, 2.223]'), ('(6.787, 10.635]', '(6.787, 10.635]'), ('(1.509, 1.739]', '(1.509, 1.739]'), ('(4.227, 5.085]', '(4.227, 5.085]'), ('(1.077, 1.252]', '(1.077, 1.252]'), ('(0.905, 1.077]', '(0.905, 1.077]'), ('(0.707, 0.905]', '(0.707, 0.905]'), ('(5.085, 6.787]', '(5.085, 6.787]'), ('(0.369, 0.531]', '(0.369, 0.531]'), ('(0.19, 0.369]', '(0.19, 0.369]'), ('(1.739, 2.004]', '(1.739, 2.004]')])
    good_Movie = StringField('good_Movie', [validators.Length(min=0, max=10)])

 