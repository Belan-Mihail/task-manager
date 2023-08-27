from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
#     All we need to do here now, is add some code to query the database so we can use that within our template.
# First, let's define a new variable within the categories function, which will also be
# called categories to keep things consistent.
# We just need to query the 'Category' model that is imported at the top of the file from
# our models.py file, and we can do that by simply typing:
# Category.query.all()
# Sometimes though, categories might be added at different times, so this would have the
# default method of sorting by the primary key when things get added.
# Let's go ahead and use the .order_by() method, and have it sort by the key of 'category_name'.
# We also need to make sure that we tell it the specific model as well, even though it
# might seem redundant, it's possible to use other sorting methods.
# You need to make sure the quantifier, which is .all() in this case, is at the end of the
# query, after the .order_by() method.
# By using the .all() method, this is actually what's known as a Cursor Object, which is
# quite similar to an array or list of records.
# Even if the result comes back with a single record, it's still considered a Cursor Object,
# and sometimes Cursor Objects can be confusing when using them on front-end templates.
# Thankfully, there's a simple Python method that can easily convert this Cursor Object
# into a standard Python list, by wrapping the variable inside of 'list()'.
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)
#     Now, all that's left to do here is to pass this variable into our rendered template,
# so that we can use this data to display everything to our users.
# The first declaration of 'categories' is the variable name that we can now use within the HTML template.
# The second 'categories', which is now a list(), is the variable defined within our function
# above, which is why, once again, it's important to keep your naming convention quite similar.


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")