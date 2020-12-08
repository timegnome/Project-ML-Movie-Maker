import json
import urllib.request
import os

from datetime import datetime
from flask import render_template, request, redirect
from FlaskApp import app
from FlaskApp.forms import SubmissionForm

MOVIE_KEY = os.environ.get('API_KEY', '49RCpal8zEPblLmrWM9OZ66n9FKhQEyuNxE8FrT3qBK6CQqzkq9XmjF83quU+qWo4FJoUztHYac+IB5c3qTBpg==')
MOVIE_URL = os.environ.get('URL', 'https://ussouthcentral.services.azureml.net/workspaces/18f31513c1594885852c68af161cbcd9/services/783a1375c53c445790afcd94a0831b7b/execute?api-version=2.0&details=true')
PROFIT_KEY = os.environ.get('API_KEY', 'TvKx1GRQnT1i0INoFns6tJWyBS+lLmyzGdQsAh6btiKH6SU6BArL+gjzYPLKTiVs44zbcwWqAHLx+y5ap+HCYQ==')
PROFIT_URL =  os.environ.get('URL',  'https://ussouthcentral.services.azureml.net/workspaces/18f31513c1594885852c68af161cbcd9/services/189cf2c6c4474817bdb9b6881d1150e9/execute?api-version=2.0&details=true')
# Construct the HTTP request header
HEADERS1 = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + MOVIE_KEY)}
HEADERS2 = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + PROFIT_KEY)}
# print(app.url_map)
# Main app page/route


@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template (
        'index.html'
        # title = 'Project ML Movie Maker',
        # year = datetime.now().year,
        # message = 'Our movie form'
    )


@app.route('/mldeployRating',  methods = ['GET', 'POST'])
def rating():
    form = SubmissionForm(request.form)
    
    # Form has been submitted
    if request.method == 'POST' and form.validate():
        # Plug in the data into a dictionary object
        # -data from the input form
        data = {
            "Inputs": {
                "input1": {
                    "ColumnNames":[
                                    "Genres",
                                    "Production Companies",
                                    "Production Countries",
                                    "New Key",
                                    "Percent_Profit",
                                    "Good_Movie"
                                    ],
                                    "Values": [
                                    [
                                        '['+ ','.join([f'{x}' for x in form.genres.data.split(',')])+']',
                                        "['Twentieth Century Fox Film Corporation']",
                                        "['United States of America']",
                                        "['terrorist', 'hostage', 'explosive']",
                                        form.percent_Profit.data,
                                        'A'
                                    ]
                                ]
                }
            },
            "GlobalParameters": {}
        }

        # Serialize the input data into json string
        body = str.encode(json.dumps(data))
        # print(body)
        # Formulate the request
        req = urllib.request.Request(MOVIE_URL, body, HEADERS1)

        # Send this request to the AML service and render the results on page
        try:
            response = urllib.request.urlopen(req)
            #print(response)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            result = do_something_pretty(result, True)
            # result = json.dumps(result, indent=4, sort_keys=True)
            return render_template(
                'mldeployRating.html',
                title = "Movie Rating:",
                year = datetime.now().year,
                result = result)
        # An HTTP error
        except urllib.error.HTTPError as err:
            result = "The request failed with status code: " + str(err.code)
            return render_template (
                'mldeployRating.html',
                title = 'There was an error',
                year = datetime.now().year,
                result = result)
            # print(err)
    
    # Serve up the input form
    return render_template (
        'ratingform.html',
        form = form,
        title = 'Rating Prediction',
        year = datetime.now().year,
        message = 'Our movie form'
    )

@app.route('/mldeployProfit',  methods = ['GET', 'POST'])
def profit():
    form = SubmissionForm(request.form)

    # Form has been submitted
    # print(form.validate())
    if request.method == 'POST' and form.validate():
        # Plug in the data into a dictionary object
        # -data from the input form
        data = {
            "Inputs": {
                "input1": {
                    "ColumnNames": [
                                    "Genres",
                                    "Production Companies",
                                    "Production Countries",
                                    "New Key",
                                    "Percent_Profit",
                                    "Good_Movie"
                                    ],
                                    "Values": [
                                    [
                                        '['+ ','.join([f'{x}' for x in form.genres.data.split(',')])+']',
                                        "['Twentieth Century Fox Film Corporation']",
                                        "['United States of America']",
                                        "['terrorist', 'hostage', 'explosive']",
                                        '(10.635, 6552255.0]',
                                        form.good_Movie.data
                                    ]
                                ]
                }
            },
            "GlobalParameters": {}
        }

        # Serialize the input data into json string
        body = str.encode(json.dumps(data))

        # Formulate the request
        req = urllib.request.Request(PROFIT_URL, body, HEADERS2)

        # Send this request to the AML service and render the results on page
        try:
            response = urllib.request.urlopen(req)
            #print(response)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            result = do_something_pretty(result, False)
            # result = json.dumps(result, indent=4, sort_keys=True)
            return render_template(
                'mldeployProfit.html',
                title = "Percent Profit:",
                year = datetime.now().year,
                result = result)
        # An HTTP error
        except urllib.error.HTTPError as err:
            result = "The request failed with status code: " + str(err.code)
            return render_template (
                'mldeployProfit.html',
                title = 'There was an error',
                year = datetime.now().year,
                result = result)
            # print(err)
    
    # Serve up the input form\
    print (form)
    return render_template (
        'profitform.html',
        form = form,
        title = 'Run App',
        year = datetime.now().year,
        message = 'Our movie form'
    )

@app.route('/methodology')
def about():
    return render_template(
        'methodology.html'
    )

@app.route('/visualizations')
def viz():
    return render_template(
        'visualizations.html'
    )

@app.route('/mlprocess')
def mlprocess():
    return render_template(
        'mlprocess.html'
    )

def do_something_pretty(jsondata, ml):
    import itertools
    
    value = jsondata["Results"]["output1"]["value"]["Values"][0]
    # if true rating, false profit
    if ml :  
        labels =["Good_Movie",
          "Scored Probabilities for Class \"A\"",
          "Scored Probabilities for Class \"B\"",
          "Scored Probabilities for Class \"C\"",
          "Scored Probabilities for Class \"D\"",
          "Scored Labels"]
        words = ''
        for x in zip(value, labels):
            try:
                words = words+ f'  <br> {x[1]}: \t\t{float("{:.2f}".format(float(x[0])*100))}%'
            except:
                words = words+ f'  <br> {x[1]}: \t\t\t{x[0]}'
        output='For a movie with selected inputs <br/>Our Algorithm would calculate the probability for each label to be: '+ words
    else:
        
        
        labels =["Percent_Profit",
          "Scored Probabilities for Class \"(-0.0009794, 0.19]\"",
          "Scored Probabilities for Class \"(0.19, 0.369]\"",
          "Scored Probabilities for Class \"(0.369, 0.531]\"",
          "Scored Probabilities for Class \"(0.531, 0.707]\"",
          "Scored Probabilities for Class \"(0.707, 0.905]\"",
          "Scored Probabilities for Class \"(0.905, 1.077]\"",
          "Scored Probabilities for Class \"(1.077, 1.252]\"",
          "Scored Probabilities for Class \"(1.252, 1.509]\"",
          "Scored Probabilities for Class \"(1.509, 1.739]\"",
          "Scored Probabilities for Class \"(1.739, 2.004]\"",
          "Scored Probabilities for Class \"(10.635, 6552255.0]\"",
          "Scored Probabilities for Class \"(2.004, 2.223]\"",
          "Scored Probabilities for Class \"(2.223, 2.531]\"",
          "Scored Probabilities for Class \"(2.531, 2.852]\"",
          "Scored Probabilities for Class \"(2.852, 3.176]\"",
          "Scored Probabilities for Class \"(3.176, 3.614]\"",
          "Scored Probabilities for Class \"(3.614, 4.227]\"",
          "Scored Probabilities for Class \"(4.227, 5.085]\"",
          "Scored Probabilities for Class \"(5.085, 6.787]\"",
          "Scored Probabilities for Class \"(6.787, 10.635]\"",
          "Scored Labels"]
        words = ''
        for x in zip(value, labels):
            try:
                words = words+ f'  <br> {x[1]}: \t\t{float("{:.2f}".format(float(x[0])*100))}%'
            except:
                words = words+ f'  <br> {x[1]}: \t\t\t{x[0]}'
        output='For a movie with selected inputs <br/>Our Algorithm would calculate the probability for each label to be: '+ words
    # Convert values (a list) to a list of tuples [(cluster#,distance),...]
    # valuetuple = list(zip(range(valuelen-1), value[1:(valuelen)]))
    # Convert the list of tuples to one long list (flatten it)
    # valuelist = list(itertools.chain(*valuetuple))

    # Convert to a tuple for the list
    # data = tuple(list(value[0]) + valuelist)

    # Build a placeholder for the cluster#,distance values
    #repstr = '<tr><td>%d</td><td>%s</td></tr>' * (valuelen-1)
    # print(repstr)
    # Build the entire html table for the results data representation
    #tablestr = 'Cluster assignment: %s<br><br><table border="1"><tr><th>Cluster</th><th>Distance From Center</th></tr>'+ repstr + "</table>"
    #return tablestr % data
    return output
        