from wtforms import Form, StringField, TextAreaField, validators, SelectField, SelectMultipleField


class SubmissionForm(Form):
    genres = SelectMultipleField('Genres', choices=[('Animation', 'Animation'), ('Comedy', 'Comedy'),
     ('Family', 'Family'), ('Adventure', 'Adventure'), ('Fantasy', 'Fantasy'), ('Romance', 'Romance'),
      ('Drama', 'Drama'), ('Action', 'Action'), ('Crime', 'Crime'), ('Thriller', 'Thriller'), ('Horror', 'Horror'),
       ('History', 'History'), ('Mystery', 'Mystery'), ('War', 'War'), ('Foreign', 'Foreign'), ('Music', 'Music'),
        ('Documentary', 'Documentary'), ('Western', 'Western')], default = 'Action')

    prodComp = SelectMultipleField('prodComp', choices =[('Paramount Pictures', 'Paramount Pictures'),
  ('Universal Pictures', 'Universal Pictures'), ('Twentieth Century Fox Film Corporation',  'Twentieth Century Fox Film Corporation'),
    ('Columbia Pictures Corporation', 'Columbia Pictures Corporation'), ('Columbia Pictures', 'Columbia Pictures'), ('United Artists', 'United Artists'),
      ('New Line Cinema', 'New Line Cinema'), ('Miramax Films', 'Miramax Films'), ('Walt Disney Pictures', 'Walt Disney Pictures'), ('TriStar Pictures', 'TriStar Pictures'),
        ('Regency Enterprises', 'Regency Enterprises'), ('DreamWorks SKG', 'DreamWorks SKG'), ('Channel Four Films', 'Channel Four Films'), ('Touchstone Pictures', 'Touchstone Pictures'),
          ('Village Roadshow Pictures', 'Village Roadshow Pictures'), ('StudioCanal', 'StudioCanal'), ('Gaumont', 'Gaumont'), ('TF1 Films Production', 'TF1 Films Production'),
            ('Fox Searchlight Pictures', 'Fox Searchlight Pictures'), ('Imagine Entertainment', 'Imagine Entertainment'), ('France 2 Cinéma', 'France 2 Cinéma'),
              ('Hollywood Pictures', 'Hollywood Pictures'), ('Toho Company', 'Toho Company'), ('Orion Pictures', 'Orion Pictures'),
                ('PolyGram Filmed Entertainment', 'PolyGram Filmed Entertainment')], default ='Universal Pictures')

    prodCont = SelectMultipleField('prodCont', choices =[('United States of America', 'United States of America'),
 ('United Kingdom', 'United Kingdom'), ('France', 'France'), ('Japan', 'Japan'), ('Germany', 'Germany'), ('Italy', 'Italy'),
  ('Canada', 'Canada'), ('Australia', 'Australia'), ('Hong Kong', 'Hong Kong'), ('Spain', ' Spain'), ('Sweden', 'Sweden'),
    ('Russia', 'Russia'), ('Finland', 'Finland'), ('Denmark', 'Denmark'), ('India', 'India'), ('South Korea', 'South Korea'),
      ('China', 'China'), ('Mexico', 'Mexico'), ('Poland', 'Poland'), ('Belgium', 'Belgium'), ('Czech Republic', 'Czech Republic'),
        ('Brazil', 'Brazil'), ('Ireland', 'Ireland'), ('Austria', 'Austria'), ('Argentina', 'Argentina')], default = 'United States of America')

    new_Key = SelectMultipleField('New Key', choices=[('independent film', 'independent film'), ('murder', 'murder'),
  ('based on novel', 'based on novel'), ('sex', 'sex'), ('nudity', 'nudity'), ('musical', 'musical'),
    ('violence', 'violence'), ('revenge', 'revenge'), ('love', 'love'), ('suspense', 'suspense'), ('female nudity', 'female nudity'),
      ('police', 'police'), ('world war ii', 'world war ii'), ('prison', 'prison'), ('biography', 'biography'), ('friendship', 'friendship'),
        ('sport', 'sport'), ('sequel', 'sequel'), ('woman director', 'woman director'), ('paris', 'paris'), ('new york', 'new york'),
          ('suicide', 'suicide'), ('rape', 'rape'), ('teenager', 'teenager'), ('drug', 'drug')], default = 'new york')

    percent_Profit = SelectField('percent_Profit', choices=[('(-0.0009794, 0.19]', 'less than 19 %'),
     ('(0.19, 0.369]', '19-36%'), ('(0.369, 0.531]', '36-53%'), ('(0.531, 0.707]', '50-70%'),
      ('(0.707, 0.905]', '70-90%'), ('(0.905, 1.077]', '90-107%'), ('(1.077, 1.252]', '107-125%'), ('(1.252, 1.509]', '120-150%'), 
        ('(1.509, 1.739]', '150-173%'), ('(1.739, 2.004]', '173-200%'), ('(2.004, 2.223]', '200-222%'), ('(2.223, 2.531]', '222-253%'),
          ('(2.531, 2.852]', '253-285%'), ('(2.852, 3.176]', '285-317%'), ('(3.176, 3.614]', '317-361%'), ('(3.614, 4.227]', '361-422%'),
            ('(4.227, 5.085]', '422-508%'), ('(5.085, 6.787]', '508-678%'), ('(6.787, 10.635]', '678-1065%'), ('(10.635, 6552255.0]', '1060%+')], default = '(1.739, 2.004]')
    good_Movie = SelectField('good_Movie', choices = [('A','A'),('B','B'),('C','C'),('D','D')], default = 'A')

    