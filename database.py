"""Module contains class Database."""

import sqlite3
import json
from datetime import date


class Database:
    """Class Database provides a required functionality to work with the database. It utilizes sqlite3 database."""

    name = 'habits_list.db'

    def create_db_table(self, db_name):
        """Method takes a database name as an argument and creates if there is no such database or connects to
        the database if the database which such name exists. It creates table 'habits' and maps attributes of the
        instances of the Habit Class into it. Habit ID is used as a primary key."""
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY,
                name TEXT,
                period INTEGER,
                spec TEXT,
                tracked INTEGER,
                creation_date INTEGER,
                tracking TEXT,
                longest_streak INTEGER)
        """)
        conn.commit()
        conn.close()

    def query_db_all(self, db_name):
        """Method takes a database name as an argument and returns a list of all database's rows (attributes of
        instances of Habit Class)."""
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        sqlite_select_query = """SELECT * from habits"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        return records

    def submit_to_db(self, habit, db_name):
        """Method takes a database name as an argument and an instance of class habits and submits it to database."""
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO habits VALUES (:id, :name, :period, :spec,  :tracked,"
                       " :creation_datetime, :tracking, :longest_streak)",
                       {
                           "id": habit.id,
                           "name": habit.name,
                           "period": habit.period,
                           "spec": habit.spec,
                           "tracked": int(habit.tracked),
                           "creation_datetime": habit.creation_datetime,
                           "tracking": json.dumps(habit.tracking, default = self.myconverter),
                           "longest_streak": habit.longest_streak
                       })
        conn.commit()
        conn.close()


    def query_db(self, habit_id, db_name):
        """Method takes habit ID and database name as an argument and query the database. Method returns a list with
        the attributes of the instance of class Habit."""
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        sqlite_select_query = """SELECT * from habits where id = ?"""
        cursor.execute(sqlite_select_query, (habit_id,))
        record = cursor.fetchone()
        conn.commit()
        conn.close()
        return record

    def update_db_row(self, habit, db_name):
        """Method takes an instance of class Habit and a database name as an argument and updates the rom with the
        instance acordingly.  """
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        sqlite_update_query = """Update habits set name = ?, spec = ?, period = ?, tracked = ?, tracking = ?, 
            longest_streak = ? where id = ?"""
        column_values = (habit.name, habit.spec, habit.period, int(habit.tracked),
                         json.dumps(habit.tracking, default = self.myconverter), habit.longest_streak, habit.id)
        cursor.execute(sqlite_update_query, column_values)
        conn.commit()
        cursor.close()
        conn.close()

    def delete_row(self, habit, db_name):
        """Method takes an instance of class Habit and a database name as an argument and deletes a corresponding row in
        the database. """
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        sql_delete_query = """DELETE from habits where id = """ + str(habit.id)
        cursor.execute(sql_delete_query)
        conn.commit()
        cursor.close()
        conn.close()

    def myconverter(self, arg):
        """Method returns a string interpretation of an argument."""
        if isinstance(arg, date):
            return arg.__str__()