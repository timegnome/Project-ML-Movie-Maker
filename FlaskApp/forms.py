from wtforms import Form, StringField, TextAreaField, validators, SelectField


class SubmissionForm(Form):
    # genres = StringField('Genres', [validators.Length(min=5, max=100)])
    genres = SelectField('Genres', choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Family', 'Family') ,('Fantasy', 'Fantasy') ,('Foreign', 'Foreign'), ('History', 'History'), ('Horror', 'Horror'), ('Music', 'Music'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], default = 'Action')
    # prodComp = StringField('prodComp', [validators.Length(min=0, max=200)])
    prodComp = SelectField('prodComp', choices=[('Amblin Entertainment', 'Amblin Entertainment'), ('Channel Four Films', 'Channel Four Films'), ('Columbia Pictures', 'Columbia Pictures'), ('Columbia Pictures Corporation', 'Columbia Pictures Corporation'), ('DreamWorks SKG', 'DreamWorks SKG'), ('Fox Searchlight Pictures', 'Fox Searchlight Pictures'), ('Gaumont', 'Gaumont'), ('Hollywood Pictures', 'Hollywood Pictures'), ('Imagine Entertainment', 'Imagine Entertainment'), ('Lions Gate Films', 'Lions Gate Films'), ('Miramax Films', 'Miramax Films'), ('New Line Cinema', 'New Line Cinema'), ('Paramount Pictures', 'Paramount Pictures'), ('Regency Enterprises', 'Regency Enterprises'), ('StudioCanal', 'StudioCanal'), ('TF1 Films Production', 'TF1 Films Production'), ('Toho Company', 'Toho Company'), ('Touchstone Pictures', 'Touchstone Pictures'), ('TriStar Pictures', 'TriStar Pictures'), ('Twentieth Century Fox Film Corporation', 'Twentieth Century Fox Film Corporation'), ('United Artists', 'United Artists'), ('Universal Pictures', 'Universal Pictures'), ('Village Roadshow Pictures', 'Village Roadshow Pictures'), ('Walt Disney Pictures', 'Walt Disney Pictures')], default = 'Amblin Entertainment')
    prodCont = StringField('prodCont', [validators.Length(min=0, max=200)])
    # new_Key = StringField('New Key', [validators.Length(min=0, max=100)])
    new_Key = SelectMultipleField('New Key', choices=[('aftercreditsstinger', 'After-Credits Scene'), ('airplane', 'Airplane'), ('alien', 'Alien'), ('animation', 'Animation'), ('based on comic', 'Based on comic'), ('based on novel', 'Based on novel'), ('daughter', 'Daughter'), ('duringcreditsstinger', 'During-Credits Scene'), ('dying and death', 'Dying and Death'), ('dystopia', 'Dystopia'), ('friendship', 'Friendship'), ('island', 'Island'), ('love', 'Love'), ('magic', 'Magic'), ('marvel comic', 'Marvel Comic'), ('musical', 'Musical'), ('saving the world', 'Saving the World'), ('secret identity', 'Secret Identity'), ('sequel', 'Sequel'), ('ship', 'Ship'), ('superhero', 'Superhero'), ('suspense', 'Suspense'), ('undercover', 'Undercover'), ('violence', 'Violence'), ('witch', 'Witch')], default = 'After-Credits Scene')
    # percent_Profit = StringField('percent_Profit', [validators.Length(min=0, max=10)])
    percent_Profit = SelectField('percent_Profit', choices=[('(-0.0009794, 0.19]', 'less than 19 %'),
     ('(0.19, 0.369]', '19-36%'), ('(0.369, 0.531]', '36-53%'), ('(0.531, 0.707]', '50-70%'),
     ('(0.707, 0.905]', '70-90%'), ('(0.905, 1.077]', '90-107%'), ('(1.077, 1.252]', '107-125%'), ('(1.252, 1.509]', '120-150%'), 
      ('(1.509, 1.739]', '150-173%'), ('(1.739, 2.004]', '173-200%'), ('(2.004, 2.223]', '200-222%'), ('(2.223, 2.531]', '222-253%'),
       ('(2.531, 2.852]', '253-285%'), ('(2.852, 3.176]', '285-317%'), ('(3.176, 3.614]', '317-361%'), ('(3.614, 4.227]', '361-422%'),
         ('(4.227, 5.085]', '422-508%'), ('(5.085, 6.787]', '508-678%'), ('(6.787, 10.635]', '678-1065%'), ('(10.635, 6552255.0]', '1060%+')], default = '(1.739, 2.004]')
    good_Movie = SelectField('good_Movie', choices = [('A','A'),('B','B'),('C','C'),('D','D')], default = 'A')

 