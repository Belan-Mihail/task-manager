# We need to import os once again, in order to utilize environment variables within this file.
# We also need to import the 'app' variable that we've created within our taskmanager
# package, defined in the init file.
import os
from taskmanager import app



# The last step to run our application is to tell our app how and where to run the application.
# This is the same process we've seen before, checking that the 'name' class is equal to
# the default 'main' string, wrapped in double underscores.
# If it's a match, then we need to have our app running, which will take three arguments:
# 'host', 'port', and 'debug'.
# Each of these, as you may recall, are stored in the environment variables, so we need to
# use os.environ.get().
# The host is the IP, the port is obviously PORT, but that needs to be converted into
# an integer, and then debug is of course DEBUG.
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )