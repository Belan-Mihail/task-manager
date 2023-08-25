# We're going to start using some Flask functionality, so we can import render_template from flask to start with.
# Then, from our main taskmanager package, let's import both 'app' and 'db'.

from flask import render_template
from taskmanager import app, db
# At the top of the routes, we need to import these classes in order to generate our database next.
from taskmanager.models import Category, Task

# For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
# This will be used to target a function called 'home', which will just return the rendered_template
# of "base.html" that we will create shortly.
@app.route("/")
def home():
    return render_template("base.html")