import csv
from typing import Any
from flask import Flask, redirect, render_template, request # type: ignore

app = Flask(__name__) # type: ignore

def valid_login(username: str, password: str): # type: ignore
    '''
    valid_login
    '''
    return True

def write_to_csv(username: str, password: str):
    '''
    write_to_csv
    '''
    print(username, password)
    with open('./server/data.csv', mode='a', newline='') as database:
        writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([username, password])

@app.route("/") # type: ignore
def hello_world() -> Any:
    '''
    hello_world
    '''
    return render_template('index.html') # type: ignore
    # return "<p>Hello, World!</p>"

# Path Params
@app.route("/profile/<name>") # type: ignore
def blog(name: str) -> Any:
    '''
    blog
    '''
    return f'<p>Profile Route! {name}</p>'

# Dynamic Page
@app.route("/string:<page_name>")  # type: ignore
def page(page_name: str) -> Any:
    '''
    hello_world
    '''
    return render_template(page_name)  # type: ignore
    # return "<p>Hello, World!</p>"

# Request Object
@app.route('/login', methods=['POST', 'GET'])
def login():
    '''
    login
    '''
    error = None

    if request.method == 'POST':
        data = request.form.to_dict()
        username = data['username']
        password = data['password']

        if valid_login(username, password):
            write_to_csv(username, password)
            return redirect('/home.html')
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
