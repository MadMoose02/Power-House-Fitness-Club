import click, json
from random import randint
from base64 import b64encode
from flask.cli import AppGroup
from datetime import date, datetime, timedelta

from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( 
    create_user, 
    get_all_users_json, 
    get_all_users, 
    create_classes, 
    create_packages,
    create_facilities,
    create_emergency_contact,
    create_wallet,
    create_activity,
    add_debit,
    create_transaction
)

app = create_app()
migrate = get_migrate(app)

@app.cli.command("init", help="Creates and initialises the database")
def initialise():
    db.drop_all()
    db.create_all()
    print("Database constructed")
    
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
    
    # Add emergency contact for test users
    create_emergency_contact(
        fname="Wendy",
        lname="the Builder",
        relation="Spouse",
        contact="519-2352"
    )
    create_emergency_contact(
        fname="Roy",
        lname="Layton",
        relation="Brother",
        contact="953-2180"
    )
    
    # Create wallet for default users
    create_wallet(
        debit=300,
        credit=0
    )
    
    create_wallet(
        debit=350,
        credit=0
    )
    
    # Add default users
    create_user(
        username='bob', 
        password='bobpass', 
        fname='Bob', 
        lname='the Builder', 
        dob=date(1900, 1, 15), 
        address='#10A Nickelodeon Road', 
        phone='123-5432', 
        sex='male',
        email='bob.thebuilder@mail.com',
        image=b64encode(open("App/static/images/male.jpg", "rb").read()),
        package_id=2,
        emergency_contact_id=1,
        wallet_id=1
    )
    
    create_user(
        username='ann', 
        password='annpass', 
        fname='Annette', 
        lname='Layton', 
        dob=date(1998, 9, 30), 
        address='#9 Avenue Street', 
        phone='235-4545', 
        sex='female', 
        email='annette.layton@mail.com',
        image=b64encode(open("App/static/images/female.jpg", "rb").read()),
        package_id=3,
        emergency_contact_id=2,
        wallet_id=2
    )
    
    # Add test data to data
    energy_lvl_labels = ["Low", "Medium", "High"]
    for i in range(1, 20):
        energy_lvl = randint(0, 2)
        start_date = datetime.today().date() - timedelta(days=20)
        days_between = (datetime.today().date() - start_date).days
        random_day = start_date + timedelta(days=randint(0, days_between))
        create_activity(
            user_id=1, 
            date=random_day, 
            pre_workout=randint(0, 1),
            energy_level=energy_lvl_labels[energy_lvl],
            details=f"This is test activity #{i}"
        )
        
        # Add points to the user's wallet
        add_debit(wallet_id=2, debit=10)
        create_transaction(
            user_id=1, 
            wallet_id=2, 
            type="Debit",
            amount=10,
            details="Added 10 points to debit for completing a workout",
            datetime=random_day.strftime("%Y-%m-%d %H:%M:%S")
        )
    
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