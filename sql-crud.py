from sqlalchemy import (create_engine, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class based model for the 'Programmer' table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# create a class based model for the 'Game' table
class Game(base):
    __tablename__ = "Game"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    game_genre = Column(String)
    release = Column(Integer)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer",
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing",
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language",
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11",
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft",
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web",
)

ivan_petrovic = Programmer(
    first_name="Ivan",
    last_name="Petrovic",
    gender="M",
    nationality="Croatian",
    famous_for="Great Ideas",
)

# creating records on our Game table
gta_sanandreas = Game(
    name = "Grand Theft Auto: San Andreas",
    game_genre = "Action",
    release = 2005
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(ivan_petrovic)    

# add each instance of our games to our session
session.add(gta_sanandreas)

# updating a single commit 
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President" 

# commit our session to the database
session.commit()

# # updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender == "Male"
#     else:
#         print("Gender Not Defined")
#     session.commit()

# # deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# defensive programming
# if Programmer is not None:
#     print("Programmer Found: ", Programmer.first_name + " " + Programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(Programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# # delete multiple records - programmers
# programmers = session.query(Programmer)
# for x in programmers:
#     session.delete(x)
#     session.commit()

# # delete multiple records - game
# games = session.query(Game)
# for x in games:
#     session.delete(x)
#     session.commit()

# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " +
#         programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )

games = session.query(Game)
for game in games:
    print(
        game.name,
        game.game_genre,
        game.release,
        sep=(" | ")
    )