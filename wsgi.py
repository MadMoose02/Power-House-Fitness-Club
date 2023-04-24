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
    create_transaction,
    create_discussion,
    create_message
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
    
    # Create user wallets
    wallet_1 = create_wallet(debit=0, credit=0)
    wallet_2 = create_wallet(debit=0, credit=0)
    wallet_3 = create_wallet(debit=0, credit=0)
    
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
    create_emergency_contact(
        fname="Daniel",
        lname="Allen",
        relation="Father",
        contact="968-6296"
    )
    
    # Add default users
    bob = create_user(
        username='bob',
        password='bobpass', 
        fname='Bob', 
        lname='the Builder', 
        dob=date(1900, 1, 15), 
        address='#10A Nickelodeon Road', 
        phone='123-5432', 
        sex='male',
        email='bob.thebuilder@mail.com',
        image=b64encode(open("App/static/images/user/male.jpg", "rb").read()),
        package_id=2,
        emergency_contact_id=1,
        wallet_id=wallet_1.id
    )
    
    ann = create_user(
        username='annette.layton', 
        password='annpass', 
        fname='Annette', 
        lname='Layton', 
        dob=date(1998, 9, 30), 
        address='#9 Avenue Street', 
        phone='235-4545', 
        sex='female', 
        email='annette.layton@mail.com',
        image=b64encode(open("App/static/images/user/female.jpg", "rb").read()),
        package_id=3,
        emergency_contact_id=2,
        wallet_id=wallet_2.id
    )
    
    sam = create_user(
        username='sam.allen',
        password='sampass',
        fname="Samantha",
        lname="Allen",
        dob=date(2000, 4, 10),
        address="43929 SE 160th Street, North Bend",
        phone="282-1784",
        sex="female",
        email="samantha.allen@mail.com",
        image=b64encode(open("App/static/images/user/sam.jpg", "rb").read()),
        package_id=1,
        emergency_contact_id=3,
        wallet_id=wallet_3.id
    )
    
    # Add test data to data
    energy_lvl_labels = ["Low", "Medium", "High"]
    for i in range(1, 20):
        energy_lvl = randint(0, 2)
        start_date = datetime.today().date() - timedelta(days=20)
        days_between = (datetime.today().date() - start_date).days
        random_day = start_date + timedelta(days=randint(0, days_between))
        create_activity(
            user_id=bob.id, 
            date=random_day, 
            pre_workout=randint(0, 1),
            energy_level=energy_lvl_labels[energy_lvl],
            details=f"This is test activity #{i}"
        )
        
        # Add fitcoins to the user's wallet
        add_debit(wallet_id=bob.id, debit=10)
        create_transaction(
            user_id=bob.id, 
            wallet_id=bob.wallet_id, 
            type="Debit",
            amount=10,
            details="Added 10 Fitcoins to debit for completing an activity",
            datetime=random_day.strftime("%Y-%m-%d %H:%M:%S")
        )
        
    # Add comments to the forum
    create_discussion(title="How do I start with HIT?", started_by=bob.id)
    create_message(
        discussion_id=1,
        user_id=bob.id,
        content="I'm unsure how to start doing High Intensity Training. How do I begin?",
        external_link="",
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    create_message(
        discussion_id=1,
        user_id=ann.id,
        content="Hi there! Maybe this can help you?",
        external_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    
    create_discussion("Recommendations for pre-workout Meal/Snacks?", started_by=ann.id)
    create_message(
        discussion_id=2,
        user_id=ann.id,
        content="Any recommendations for a simple yet nutritous pre-workout meal or snack? I'd love to hear them!",
        external_link="",
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    create_message(
        discussion_id=2,
        user_id=bob.id,
        content="How about yogurt? Or maybe a banana?",
        external_link="",
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    create_message(
        discussion_id=2,
        user_id=sam.id,
        content="Crix and tuna",
        external_link="",
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    
    create_discussion("Why are the packages so expensive?", started_by=sam.id)
    create_message(
        discussion_id=3,
        user_id=sam.id,
        content="I'm a student and Powerhouse Fitness Club's student package is still a bit pricey.",
        external_link="",
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    create_message(
        discussion_id=3,
        user_id=bob.id,
        content=f"I blame @{ann.username} for this.",
        external_link="https://www.youtube.com/watch?v=mAG7DnQDljg",
        datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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