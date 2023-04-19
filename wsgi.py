import click, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from datetime import date

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users )

app = create_app()
migrate = get_migrate(app)

@app.cli.command("init", help="Creates and initialises the database")
def initialise():
    db.drop_all()
    db.create_all()
    print("Database constructed")
    create_user(
        username="rob", 
        password="robpass", 
        fname="Rob", 
        lname="Bob", 
        dob=date(2000, 1, 12),
        address="address", 
        phone="phone", 
        sex="male", 
        email="email"
    )
    print("Added test user 'rob'")
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


# '''
# Test Commands
# Usage : flask test <command> [<args>]
# '''
# test = AppGroup('test', help='Testing commands') 

# @test.command("user", help="Run User tests")
# @click.argument("type", default="all")
# def user_tests_command(type):
#     if type == "unit":
#         sys.exit(pytest.main(["-k", "UserUnitTests"]))
#     elif type == "int":
#         sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
#     else:
#         sys.exit(pytest.main(["-k", "App"]))
    
# # Add all test commands
# app.cli.add_command(test)