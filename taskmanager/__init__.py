# Next, the entire application will need to be its own Python package, so to make this
# a package, we need a new folder which we will simply call taskmanager/.
# Inside of that, a new file called __init__.py
# This will make sure to initialize our taskmanager application as a package, allowing us to use
# our own imports, as well as any standard imports.
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa



# Now we can create an instance of the imported Flask() class, and that will be stored in
# a variable called 'app', which takes the default Flask __name__ module.
# Then, we need to specify two app configuration variables, and these will both come from our environment variables.
# app.config SECRET_KEY and app.config SQLALCHEMY_DATABASE_URI, both wrapped in square brackets and quotes.
# Each of these will be set to get their respective environment variable, which is SECRET_KEY,
# and the short and sweet DB_URL for the database location which we'll set up later.


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")



# Then, we need to create an instance of the imported SQLAlchemy() class, which will be
# assigned to a variable of 'db', and set to the instance of our Flask 'app'.
# Finally, from our taskmanager package, we will be importing a file called 'routes' which we'll create momentarily.
db = SQLAlchemy(app)

from taskmanager import routes  # noqa