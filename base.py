from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()

Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()
'''
import sqlite3


def submit(obj):
    # Create a database or connect to one
    conn = sqlite3.connect('habits.db')
    # Create cursor
    c = conn.cursor()
    # Insert into table
    c.execute("INSERT INTO habits_list VALUES (:id, :name, :spec, :period, :tracked, :cr_date)",
            {
                'id': obj.id,
                'name': obj.name,
                'spec': obj.spec,
                'period': obj.period,
                'tracked': obj.tracked,
                'cr_date': obj.cr_date               
            })

    # Submit changes
    conn.commit()

    # Close connection
    conn.close()


def delete():
    conn = sqlite3.connect('habits.db')
    # Create cursor
    c = conn.cursor()

    c.execute("DELETE from habits WHERE oid=PLACEHOLDER")
    
    # Submit changes
    conn.commit()

    # Close connection
    conn.close()


def query():
    # Create a database or connect to one
    conn = sqlite3.connect('habits.db')
    # Create cursor
    c = conn.cursor()
    # Query the database
    c.execute("SELECT *, oid from habits_list")
    c.fetchall() # возвращает список с кортежем внутри
    records = c.fetchall()

    for record in records:
        print_records += str(record) + " " 



    # Create table
    c.execute("""CREATE TABLE habits_list,
            name text,
            periodicity text,
            date/time created integer
        """)




l = ['jack','jill','bob']


c.execute("CREATE TABLE first_table(int id, varchar(255) text, additional fields)")
c.execute("CREATE TABLE names_table(int id, int num, varchar(255) name)")

SELECT name FROM names_table 
WHERE id=?
ORDER BY num
'''
