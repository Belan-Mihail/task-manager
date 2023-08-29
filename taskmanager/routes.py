from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)
# all like def categories():

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



# Now, we can head back over to the routes.py file, and since we've given an argument of
# 'category_id' when clicking the 'Edit' button, this also needs to appear in our app.route.
# These types of variables being passed back into our Python functions must be wrapped
# inside of angle-brackets within the URL.
# We know that all of our primary keys will be integers, so we can cast this as an 'int'.
@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
#     In order for this function to know which specific category to load, we need to attempt to find
# one in the database using the ID provided from the URL.
# The template is expecting a variable 'category', so let's create that new variable now.
# Using the imported Category model from the top of the file, we need to query the database,
# and this time we know a specific record we'd like to retrieve.
# There's a SQLAlchemy method called '.get_or_404()', which takes the argument of 'category_id'.
# What this does is query the database and attempts to find the specified record using the data
# provided, and if no match is found, it will trigger a 404 error page.
    category = Category.query.get_or_404(category_id)
    # Update name of categories
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


# This function needs to know which particular category we would like to delete from the data base.
# Let's actually copy a few things from the 'edit' function above.
# First, we need to pass the category ID into our app route and function, and once again,
# we are casting it as an integer.
# Next, we should attempt to query the Category table using this ID, and store it inside of a variable called 'category'.
@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))



@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)




# @app.route("/add_task", methods=["GET", "POST"])
# def add_task():

# If you recall from the video where we designed our database schema, each task actually requires
# the user to select a category for that task.
# In order to do that, we first need to extract a list of all of the categories available from the database.
#     categories = list(Category.query.order_by(Category.category_name).all())


# From our models.py file, each task must have a few different elements, including a task
# name, description, due date, category, and whether or not it's urgent.
# That means we need to update the POST method to reflect each of the fields that will be
# added from the form that we will create shortly.

# Task name will be set to the form's name attribute of 'task_name'.
# Task description will use the form's 'task_description' field
# The 'is_urgent' field will be a Boolean, either true or false, so we'll make it True if the
# form data is toggled on, otherwise it will be set to False by default.
# Due date will of course be the form's 'due_date' input box.
# Then finally, the last column for each Task will be the selected Category ID, which will
# be generated as a dropdown list to choose from, using the 'categories' list above.
#     if request.method == "POST":
#         task = Task(
#             task_name=request.form.get("task_name"),
#             task_description=request.form.get("task_description"),
#             is_urgent=bool(True if request.form.get("is_urgent") else False),
#             due_date=request.form.get("due_date"),
#             category_id=request.form.get("category_id")
#         )

# Once the form is submitted, we can add that new 'task' variable to the database session,
# and then immediately commit those changes to the database.
# If successful, then we can redirect the user back to the 'home' page where each task will eventually be displayed.
#         db.session.add(task)
#         db.session.commit()
#         return redirect(url_for("home"))

# This should render the template for "add_task.html", and in order for the dropdown list to display
# each available category, we need to pass that variable into the template.
# As a reminder, the first 'categories' listed is the variable name that we will be able
# to use on the template itself.
#     return render_template("add_task.html", categories=categories)