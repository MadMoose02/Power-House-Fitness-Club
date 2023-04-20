import click, sys, json
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from datetime import date

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( 
    create_user, 
    get_all_users_json, 
    get_all_users, 
    create_classes, 
    create_packages,
    create_facilities
)

app = create_app()
migrate = get_migrate(app)

@app.cli.command("init", help="Creates and initialises the database")
def initialise():
    db.drop_all()
    db.create_all()
    print("Database constructed")
    
    # Add default users
    create_user(
        'bob', 
        'bobpass', 
        'Bob', 
        'the Builder', 
        date(1900, 1, 15), 
        '#10A Nickelodeon Road', 
        '123545452', 
        'male',
        'bob.thebuilder@mail.com'
    )
    print("Added test user 'bob'")
    create_user(
        'david', 
        'davidpass', 
        'David', 
        'Bossman', 
        date(1998, 9, 30), 
        '#9 Avenue Street', 
        '123545452', 
        'male', 
        'david.bossman@mail.com'
    )
    print("Added test user 'david'")
    
    # Add all classes
    with open("App/models/classes.json") as f:
        classes = json.load(f)
        create_classes(classes)
    print("Added all classes")
    
    # Add all packages
    with open("App/models/packages.json") as f:
        packages = json.load(f)
        create_packages(packages)
    print("Added all packages")
    
    # Add all facilities
    with open("App/models/facilities.json") as f:
        facilities = json.load(f)
        create_facilities(facilities)
    print("Added all facilities")
    
    print("Database intialised successfully")


'''
User Commands
Usage: flask user <command> [<args>]
'''
user_cli = AppGroup('user', help='User object commands') 

@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')


@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

# Add all user commands
app.cli.add_command(user_cli)