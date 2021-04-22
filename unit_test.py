import unittest
from start import *
from database import Database
from analytics import tracked, same_period, longest_streak
from datetime import datetime
from freezegun import freeze_time
from habits import HabitsList
import os


habits_list = HabitsList()
Database.name = 'test_db.db'
db_connection = Database()
db_connection.create_db_table(Database.name)
process_query(db_connection.query_db_all(Database.name), habits_list)


class HabitAppTestCase(unittest.TestCase):
    """This is a class with the test cases to test functionality of the Habit Tracker App."""

    def test_a_create_new_habit(self):
        """Test #1. Testing method new_habit of the class HabitClass"""
        habits_list.new_habit('Test habit #1', 1, 'Test habit #1', creation_datetime=datetime(2021, 2, 1, 12, 0, 1))
        new_habit_1 = habits_list.habits[-1]
        self.assertEqual(new_habit_1, habits_list.habits[-1])

    def test_b_created_habit_name(self):
        """Test #2. Testing the attribute period of the created habit."""
        new_habit_1 = habits_list.habits[-1]
        self.assertEqual(new_habit_1.name, 'Test habit #1')

    def test_c_created_habit_period(self):
        """Test #3. Testing the attribute period of the created habit."""
        new_habit_1 = habits_list.habits[-1]
        self.assertEqual(new_habit_1.period, 1)

    def test_d_created_habit_spec(self):
        """Test #4. Testing the attribute spec of the created habit."""
        new_habit_1 = habits_list.habits[-1]
        self.assertEqual(new_habit_1.spec, 'Test habit #1')

    def test_e_created_habit_tracked(self):
        """Test #5. Testing the attribute tracked of the created habit."""
        new_habit_1 = habits_list.habits[-1]
        self.assertEqual(new_habit_1.tracked, False)

    def test_f_created_habit_creation_datetime(self):
        """Test #6. Testing the attribute creation_datetime of the created habit."""
        new_habit_1 = habits_list.habits[-1]
        self.assertEqual(new_habit_1.creation_datetime, datetime(2021, 2, 1, 12, 0, 1))

    def test_g_created_habit_id(self):
        """Test #7. Testing the attribute id of the created habit."""
        new_habit_1 = habits_list.habits[-1]
        self.assertEqual(new_habit_1.id, 1)

    def test_h_created_habit_tracking(self):
        """Test #8. Testing the attribute tracking of the created habit."""
        new_habit_1 = habits_list.habits[-1]
        self.assertEqual(new_habit_1.tracking, [])

    def test_i_created_habit_longest_streak(self):
        """Test #9. Testing the attribute tracking of the created habit."""
        new_habit_1 = habits_list.habits[-1]
        self.assertEqual(new_habit_1.longest_streak, 0)

    def test_j_track_habit(self):
        """Test #10. Testing method track_habit of the class HabitsList."""
        new_habit_1 = habits_list.habits[-1]
        habits_list.track_habit(new_habit_1.id)
        self.assertEqual(new_habit_1.tracked, True)

    def test_k_check_off(self):
        """Test #11. Testing method check_off of the class HabitsList."""
        new_habit_1 = habits_list.habits[-1]
        with freeze_time('2021-02-01 12:00:02.123456'):
            habits_list.check_off(new_habit_1.id)
        last_entry = new_habit_1.tracking[-1]
        self.assertEqual(last_entry, datetime(2021, 2, 1, 12, 0, 2, 123456))

    def test_l_check_off(self):
        """Test #12. Testing method check_off of the class HabitsList. Method should overwrite the last timestamp
        because it is overdue."""
        new_habit_1 = habits_list.habits[-1]
        with freeze_time('2021-02-03 12:00:03.123456'):
            habits_list.check_off(new_habit_1.id)
        tracking_length = len(new_habit_1.tracking)
        self.assertEqual(tracking_length, 1)

    def test_m_delete_habit(self):
        """Test #13. Testing the method delete_habit of the class HabitsClass."""
        new_habit_1 = habits_list.habits[-1]
        habits_list.delete_habit(new_habit_1.id)
        self.assertEqual(len(habits_list.habits), 0)

    def test_n_load_predefined(self):
        """Test #14. Testing the function load_predefined()."""
        load_predefined(PREDEFINED_HABITS, habits_list)
        self.assertEqual(len(habits_list.habits), 7)

    def test_o_tracked(self):
        """Test #15. Testing the function tracked()."""
        tracked_list = tracked(habits_list.habits)
        self.assertEqual(len(tracked_list), 7)

    def test_p_same_period_daily(self):
        """Test #16. Testing function same_period() with argument 'daily'. """
        daily = same_period(habits_list.habits, 1)
        self.assertEqual(len(daily), 3)

    def test_q_same_period_weekly(self):
        """Test #17. Testing function same_period() with argument 'daily'. """
        weekly = same_period(habits_list.habits, 7)
        self.assertEqual(len(weekly), 4)

    def test_r_longest_streak(self):
        """Test #18. Testing function longest_streak(). """
        habit = longest_streak(habits_list.habits)[0]
        self.assertEqual(habit.name, 'Study python')

    def test_s_habit_status(self):
        """Test #19. Testing habit_status() function."""
        with freeze_time('2021-02-03 12:00:03.123456'):
            habit_status(habits_list.habits)
        not_broken = []
        for habit in habits_list.habits:
            if len(habit.tracking) > 1:
                not_broken.append(habit)
        self.assertEqual(len(not_broken), 5)

    def test_t_database_creation(self):
        """Test #20, testing creation of the database."""
        self.assertEqual(os.path.exists('test_db.db'), True)

    def test_u_database_query_all(self):
        """Test #21, testing method query_db_all() of the class Database."""
        records = db_connection.query_db_all('test_db.db')
        self.assertEqual(len(records), 7)

    def test_v_database_submit_to_db_query_db(self):
        """Test #22, testing method submit_to_db() and query_db() of the class Database."""
        habits_list.new_habit('Test habit #2', 1, 'Test habit #2', creation_datetime=datetime(2021, 2, 1, 12, 0, 1))
        new_habit_2 = habits_list.habits[-1]
        db_connection.submit_to_db(new_habit_2, 'test_db.db')
        record = db_connection.query_db(9, 'test_db.db')
        self.assertEqual(record[1], 'Test habit #2')

    def test_w_update_db_row(self):
        """Test #23, testing method update_db_row() and query_db() of the class Database."""
        new_habit_2 = habits_list.habits[-1]
        new_habit_2.name = 'Test habit #2 ammended.'
        db_connection.update_db_row(new_habit_2, 'test_db.db')
        record = db_connection.query_db(9, 'test_db.db')
        self.assertEqual(record[1], 'Test habit #2 ammended.')

    def test_x_delete_row(self):
        """Test #24, testing function delete_row()."""
        new_habit_2 = habits_list.habits[-1]
        db_connection.delete_row(new_habit_2, 'test_db.db')
        record = db_connection.query_db(9, 'test_db.db')
        self.assertEqual(record, None)

    def test_y_delete_all_predefined_habits(self):
        new_habit_1 = habits_list.habits[-1]
        habits_list.delete_habit(new_habit_1.id)
        new_habit_2 = habits_list.habits[-1]
        habits_list.delete_habit(new_habit_2.id)
        new_habit_3 = habits_list.habits[-1]
        habits_list.delete_habit(new_habit_3.id)
        new_habit_4 = habits_list.habits[-1]
        habits_list.delete_habit(new_habit_4.id)
        new_habit_5 = habits_list.habits[-1]
        habits_list.delete_habit(new_habit_5.id)
        new_habit_6 = habits_list.habits[-1]
        habits_list.delete_habit(new_habit_6.id)
        new_habit_7 = habits_list.habits[-1]
        habits_list.delete_habit(new_habit_7.id)
        new_habit_8 = habits_list.habits[-1]
        habits_list.delete_habit(new_habit_8.id)
        self.assertEqual(len(habits_list.habits), 0)

if __name__ == '__main__':
    unittest.main()

