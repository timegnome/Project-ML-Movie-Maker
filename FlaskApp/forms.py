from wtforms import Form, StringField, TextAreaField, validators, SelectField, SelectMultipleField


class SubmissionForm(Form):
    # genres = StringField('Genres', [validators.Length(min=5, max=100)])
    genres = SelectMultipleField('Genres', choices=[('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Family', 'Family'), ('Adventure', 'Adventure'), ('Fantasy', 'Fantasy'), ('Romance', 'Romance'), ('Drama', 'Drama'), ('Action', 'Action'), ('Crime', 'Crime'), ('Thriller', 'Thriller'), ('Horror', 'Horror'), ('History', 'History'), ('Mystery', 'Mystery'), ('War', 'War'), ('Foreign', 'Foreign'), ('Music', 'Music'), ('Documentary', 'Documentary'), ('Western', 'Western')], default = 'Action')
    prodComp = StringField('prodComp', [validators.Length(min=0, max=200)])
    prodCont = StringField('prodCont', [validators.Length(min=0, max=200)])
    new_Key = StringField('New Key', [validators.Length(min=0, max=100)])
    # percent_Profit = StringField('percent_Profit', [validators.Length(min=0, max=10)])
    percent_Profit = SelectField('percent_Profit', choices=[('(-0.0009794, 0.19]', 'less than 19 %'),
     ('(0.19, 0.369]', '19-36%'), ('(0.369, 0.531]', '36-53%'), ('(0.531, 0.707]', '50-70%'),
     ('(0.707, 0.905]', '70-90%'), ('(0.905, 1.077]', '90-107%'), ('(1.077, 1.252]', '107-125%'), ('(1.252, 1.509]', '120-150%'), 
      ('(1.509, 1.739]', '150-173%'), ('(1.739, 2.004]', '173-200%'), ('(2.004, 2.223]', '200-222%'), ('(2.223, 2.531]', '222-253%'),
       ('(2.531, 2.852]', '253-285%'), ('(2.852, 3.176]', '285-317%'), ('(3.176, 3.614]', '317-361%'), ('(3.614, 4.227]', '361-422%'),
         ('(4.227, 5.085]', '422-508%'), ('(5.085, 6.787]', '508-678%'), ('(6.787, 10.635]', '678-1065%'), ('(10.635, 6552255.0]', '1060%+')], default = '(1.739, 2.004]')
    good_Movie = SelectField('good_Movie', choices = [('A','A'),('B','B'),('C','C'),('D','D')], default = 'A')

    