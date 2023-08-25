# We'll start by creating a new file called models.py within our taskmanager package.
# Since we will be defining the database, we obviously need to import db from the main taskmanager package.
# For the purposes of these videos, we will be creating two separate tables, which will
# be represented by class-based models using SQLAlchemy's ORM.

from taskmanager import db

# The first table will be for various categories, so let's call this class 'Category', which
# will use the declarative base from SQLAlchemy's model.
# However, with Flask-SQLAlchemy, the 'db' variable contains each of those already, and we can
# simply use dot-notation to specify the data-type for our columns.
class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
#     In order to properly link our foreign key and cascade deletion, we need to add one more field to the Category table.
# We'll call this variable 'tasks' plural, not to be confused with the main Task class, and
# for this one, we need to use db.relationship instead of db.Column.
# Since we aren't using db.Column, this will not be visible on the database itself like
# the other columns, as it's just to reference the one-to-many relationship.
# To link them, we need to specify which table is being targeted, which is "Task" in quotes.
# Then, we need to use something called 'backref' which establishes a bidirectional relationship
# in this one-to-many connection, meaning it sort of reverses and becomes many-to-one.
# It needs to back-reference itself, but in quotes and lowercase, so backref="category".
# Also, it needs to have the 'cascade' parameter set to 'all, delete' which means it will find
# all related tasks and delete them.
# The last parameter here is lazy=True, which means that when we query the database for
# categories, it can simultaneously identify any task linked to the categories.
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_nam


# The second table will be for each task created, so we'll call this class 'Task', also using the default db.Model.
class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
#     Then, the next column will be 'due_date', and this data-type will be db.Date with 
#     nullable=False,
#     but if you need to include time on your database, then db.DateTime or db.Time are suitable.
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
#     The final column we need for our tasks is a foreign key pointing to the specific category, which will be our category_id.
# This will use db.Integer of course, and for the data-type we need to use db.ForeignKey
# so our database recognizes the relationship between our tables, which will also be nullable=False.
# The value of this foreign key will point to the ID from our Category class, and therefore
# we need to use lowercase 'category.id' in quotes.
# In addition to this, we are going to apply something called ondelete="CASCADE" for this foreign key.
# Since each of our tasks need a category selected, this is what's known as a one-to-many relationship.
# One category can be applied to many different tasks, but one task cannot have many categories.
# If we were to apply many categories to a single task, this would be known as a many-to-many relationship.
# Let's assume that we have 10 tasks on our database, and 2 categories, with these two
# categories being assigned to 5 tasks each.
# Later, we decide to delete 1 of those categories, so any of the 5 tasks that have this specific
# category linked as a foreign key, will throw an error, since this ID is no longer available.
# This is where the ondelete="CASCADE" comes into play, and essentially means that once
# a category is deleted, it will perform a cascading effect and also delete any task linked to it.
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)


    # For each model, we also need to create a function called __repr__ that takes itself as the argument,
    # similar to the 'this' keyword in JavaScript.
    # This is a standard Python function meaning 'represent’, which means to represent the class objects as a string.
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
#         The final thing that we need to do with our class-based models, is to return some sort of string for the Task class.
# We could simply return self.task_name, but instead, let's utilize some of Python's formatting to include different columns.
# We'll use placeholders of {0}, {1}, and {2}, and then the Python .format() method to specify
# that these equate to self.id, self.task_name, and self.is_urgent.
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )