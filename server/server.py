from typing import Any
from flask import Flask, render_template # type: ignore

app = Flask(__name__) # type: ignore

print(__name__)

@app.route("/") # type: ignore
def hello_world() -> Any:
    '''
    hello_world
    '''
    return render_template('index.html') # type: ignore
    # return "<p>Hello, World!</p>"

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
