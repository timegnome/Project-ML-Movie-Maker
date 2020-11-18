import json
import urllib.request
import os

from datetime import datetime
from flask import render_template, request, redirect
from FlaskApp import app
from FlaskApp.forms import SubmissionForm

MOVIE_KEY = os.environ.get('API_KEY', '<API_KEY>')
MOVIE_URL = os.environ.get('URL', '<URL>')

# Construct the HTTP request header
HEADERS = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + MOVIE_KEY)}

# Main app page/route
@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    
    form = SubmissionForm(request.form)

    # Form has been submitted
    if request.method == 'POST' and form.validate():
        # Plug in the data into a dictionary object
        # -data from the input form
        data = {
            "Inputs": {
                "input1": {
                    "ColumnNames": ["budget", "keywords", "genre", "vote_average", "revenue"],
                    "Values": [ [
                        0,
                        1,
                        form.title.data.lower(),
                        0
                    ]
                  ]
                }
            },
            "GlobalParameters": {}
        }

        # Serialize the input data into json string
        body = str.encode(json.jumps(data))

        # Formulate the request
        req = urllib.request.Request(MOVIE_URL, body, HEADERS)

        # Send this request to the AML service and render the results on page
        try:
            response = urllib.request.urlopen(req)
            #print(response)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            result = do_something_pretty(result)
            # result = json.dumps(result, indent=4, sort_keys=True)
            return render_template(
                'result.html',
                title = "Fill this in later:",
                result = result)
        # An HTTP error
        except urllib.error.HTTPError as err:
            result = "The request failed with status code: " + str(err.code)
            return render_template (
                'result.html',
                title = 'There was an error',
                result = result)
            # print(err)
    
    # Serve up the input form
    return render_template (
        'form.html',
        form = form,
        title = 'Run App',
        year = datetime.now().year,
        message = 'Our movie form'
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title = 'Contact',
        year = datetime.now().year,
        message = 'Our contact page'
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        title = 'About',
        year = datetime.now().year,
        message = 'Our descriptor page'
    )

def do_something_pretty(jsondata):
    import itertools

    value = jsondata["Results"]["output1"]["value"]["Values"][0]
    print(value)
    # Convert values (a list) to a list of tuples [(cluster#,distance),...]
    # valuetuple = list(zip(range(valuelen-1), value[1:(valuelen)]))
    # Convert the list of tuples to one long list (flatten it)
    # valuelist = list(itertools.chain(*valuetuple))

    # Convert to a tuple for the list
    # data = tuple(list(value[0]) + valuelist)

    # Build a placeholder for the cluster#,distance values
    #repstr = '<tr><td>%d</td><td>%s</td></tr>' * (valuelen-1)
    # print(repstr)
    output='For a '+value[1]+ 'movie with a budget size of : '+value[2]+ "<br/>Our Algorithm would calculate the popularity to be: "+ value[4]
    # Build the entire html table for the results data representation
    #tablestr = 'Cluster assignment: %s<br><br><table border="1"><tr><th>Cluster</th><th>Distance From Center</th></tr>'+ repstr + "</table>"
    #return tablestr % data
    return output
        