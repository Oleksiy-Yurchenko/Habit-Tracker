"""Main module of this app."""


import sys
import datetime
from habits import HabitsList
from analytics import tracked, same_period, longest_streak
from predefined_habits import PREDEFINED_HABITS
import json
from database import Database
from functools import wraps
import re


def main():
    """The function creates an instance of class HabitsList and class Database, then a database is created or connected
    if exists. Function process_query queries the database and creates instances of class Habit and stores them in list
    'habits' of the habits_list instance. All of the tracked habits are checked in order to update the longest_streak
    attribute of the instances of class Habit stored in the tracked_list. On the end function main_menu is called."""
    habits_list = HabitsList()
    db_connection = Database()
    db_connection.create_db_table(Database.name)
    process_query(db_connection.query_db_all(Database.name), habits_list)
    while True:
        tracked_list = tracked(habits_list.habits)
        habit_status(tracked_list)
        main_menu(habits_list)


def habit_status(tracked_list):
    """The function takes a list of habits with attribute tracked set to True, then function examines contents of the
     habit.tracking and converts it to datetime.date objects and stores them into the list 'habit_track_data'. All
     the double entries are removed by converting habit_track_data into the set. If the habit was checked off for a time
     more then a period, habit.tracking is reduced to the last entry. If the length of the set is bigger then the
     attribute longest_streak then attribute longest_streak is set to length of the set."""
    for habit in tracked_list:
        if habit.tracking:
            habit_track_data = []
            for date_time in habit.tracking:
                if isinstance(date_time, datetime.datetime):
                    habit_track_data.append(date_time.date())
                elif isinstance(date_time, str):
                    habit_track_data.append(datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f').date())
            habit_unique_tracking = set(habit_track_data)
            if (datetime.date.today() - habit_track_data[-1]).days - habit.period > 0:
                habit.tracking = habit.tracking[-1:]
            else:
                if habit.longest_streak < len(habit_unique_tracking):
                    habit.longest_streak = len(habit_unique_tracking)


def main_menu(habits_list):
    """The function main_menu() realizes the logic of the GUI. It takes an instance of class HabitsClass as an argument.
    It gets a user's choice from the function users_choice() and then depending on the value of the user's choice it
    evaluates different scenarios.
    If the choice is 1: then called function sub_menu() which loads a sub menu..
    If the choice is 2: then called show_habits() function which prints all the habits and then function add_habit()
    is called which adds a habit.
    If the choice is 3: then created a non_tracked_list - a list with all non-tracked habits, it's printed and after
    called function track() which allows to select and track a habit.
    If the choice is 4: then created a tracked_list - a list with all tracked habits, it's printed and after called
    function track_off() which allows to select and track off a habit.
    If the choice is 5: then printed a list of all habits and called a function check_off() which allows to select and
    check off a habit. If the habit is not tracked then by checking off it will be tracked.
    If the choice is 6: then if there are any habits created, called function delete_habit() which allows to select and
    delete a habit.
    if the choice is 7: then called function load_predefined() which loads predefined habits.
    if the choice is 8: called quit_app() function which quits the application."""
    while True:
        display_main_menu()
        choice = get_choice(7)
        if choice == 1:
            sub_menu(habits_list)
        elif choice == 2:
            show_habits(habits_list.habits)
            add_habit(habits_list)
            break
        elif choice == 3:
            non_tracked_list = tracked(habits_list.habits, tracked_status=False)
            show_habits(non_tracked_list, tracked=False)
            if non_tracked_list:
                track(non_tracked_list, habits_list)
            else:
                print('There are no habits to track. Possibly all habits are tracked already.')
            break
        elif choice == 4:
            tracked_list = tracked(habits_list.habits)
            show_habits(tracked_list)
            if tracked_list:
                track_off(tracked_list, habits_list)
            else:
                print('There are no habits to track off. Create more habits.')
            break
        elif choice == 5:
            show_habits(habits_list.habits)
            check_off(habits_list.habits, habits_list)
            break
        elif choice == 6:
            if habits_list.habits:
                show_habits(habits_list.habits)
                delete_habit(habits_list.habits, habits_list)
            else:
                print("There are no habits to delete.")
            break
        elif choice == 7:
            load_predefined(PREDEFINED_HABITS, habits_list)
            break
        elif choice == 0:
            quit_app()
        else:
            print("{0} is not a valid choice".format(choice))


def sub_menu(habits_list):
    """The function sub_menu() realizes logic of the sub menu.
    Function display_sub_menu() prints sub menu on the screen. Get_choice() gives a user's choice.
    If choice is 1: called function show_habits() which prints all the habits.
    If choice is 2: created a tracked_list - list of all tracked habits and the called show_habits which prints it.
    If choice is 3: called get_period() function to get period and then same_period() which takes as arguments list of
    habits and period. Then function show_habits() is called to print all habits with the same period.
    If choice is 4: called function longest_streak() and show_habits to print habit with the longest streak.
    If choice is 5: called function show_habits() which prints all the habits and then called function select_habits()
    which allows to select habits and returns a list of selected habits. Then called function longest_streak() with
    an argument - list of selected habits in return we obtain a list with the habit with the longest streak among
    selected.
    If choice is 0: loop breaks and we return to the main menu."""
    while True:
        display_sub_menu()
        choice = get_choice(5)
        if choice == 1:
            show_habits(habits_list.habits)
        elif choice == 2:
            tracked_list = tracked(habits_list.habits)
            show_habits(tracked_list, tracked=True)
        elif choice == 3:
            period = get_period()
            show_habits(same_period(habits_list.habits, period), period=True)
        elif choice == 4:
            if longest_streak(habits_list.habits):
                show_habits(longest_streak(habits_list.habits), longest_streak=True)
            else:
                print("None of habits has streak")
        elif choice == 5:
            show_habits(habits_list.habits)
            selected_habits = select_habits(habits_list.habits)
            if selected_habits:
                show_habits(longest_streak(selected_habits), longest_streak=True)
            else:
                print("None of habits were selected.")
        elif not choice:
            break


def display_main_menu():
    """Function prints a main menu on the screen."""
    print(
        """
Habit Tracker Menu

1. Show habits
2. Add habit
3. Track habit
4. Track off habit
5. Check off habit
6. Delete habit
7. Load Pre-defined habits
0. Quit
"""
    )


def display_sub_menu():
    """Function prints a sub menu on the screen."""
    print(
        """
Menu 

1. Show all habits
2. Show all tracked habits
3. Show habits with same periodicity
4. Show habit with the longest streak among all habits
5. Show habit with the longest streak among selected habits
0. Back
    """
    )


def get_choice(menu_length):
    """The function allows to make a user's choice. It takes a menu_length argument which states a max digit in the
    menu. It loops over until the correct value of the user's choice will be entered."""
    while True:
        choice = input("Enter an option: ")
        try:
            int_choice = int(choice)
            if int_choice <= menu_length:
                break
            else:
                print("{0} is not a valid option. Please enter a value between 0-{1}".format(choice, menu_length))
        except ValueError:
            print("{0} is not a valid option. Please enter 0-9".format(choice))
    return int_choice


def add_habit(habits_list):
    """The function allows to create a new habit. It calls function get_name() to obtain habit's name. It calls function
    get_period() to get habit's period. After method new_habit() of the class HabitsClass is called to create new habit.
    """
    while True:
        name = get_name()
        period = get_period()
        spec = input("Enter habit's specification: ")
        print('''You are about to create a following habit:
        Habit name: {0}, Habit Periodicity: {1}, Habit Specification: {2}.'''
              .format(name, 'Daily' if period == 1 else 'Weekly', spec))
        confirmation = input('To save the habit type y or Y, to cancel the habit type any other key: ')
        if confirmation in {'y', 'Y'}:
            habits_list.new_habit(name, period, spec)
            print('Your habit has been added.')
        break


def get_name():
    """Function returns a habit's name with the length not more than 32 characters."""
    while True:
        name = input("Enter a habit's name (Max 32 characters): ")
        if len(name) <= 32:
            break
    return name


def get_period():
    """Fuction returns a habit's period as integer."""
    while True:
        period = input("Enter a habit's periodicity: d, D for a Daily Period, w, W for a Weekly Period: ")
        if period in {'d', 'D'}:
            period = 1
            break
        elif period in {'w', 'W'}:
            period = 7
            break
        else:
            print('{0} is not a valid period.'.format(period))
    return period


def select_habits(list_of_habits):
    """The function takes a user input as a string of habit numbers separated by spaces, parses it, returns a list of
    the selected habits. """
    template_len = 1
    if 10 < len(list_of_habits) < 100:
        template_len = 2
    elif 100 < len(list_of_habits) < 1000:
        template_len = 3

    selected_habits = []
    break_flag = False
    while True:
        inputs = input("Enter habits numbers separated by the space or 0 to return to previous menu: ")
        input_template = re.compile(rf'^[\d{1, {template_len}} ]+[\d{1, {template_len}}]|[\d{1, template_len}]$')
        if input_template.match(inputs):
            print(inputs)
            test = inputs.strip(' ').split(' ')
            for el in test:
                if el == '':
                    test.remove(el)
            failed = []
            for i in test:
                if 0 < int(i) <= len(list_of_habits):
                    selected_habits.append(list_of_habits[int(i) - 1])
                elif int(i) == 0:
                    break_flag = True
                    break
                else:
                    failed.append(i)
            if break_flag:
                break
            if failed:
                fail_str = ''
                for i in failed:
                    fail_str += i + ' '
                print('{0} is not a valid habit number'.format(fail_str.rstrip()))
                selected_habits = []
            else:
                break
        else:
            print('{0} not a valid habit numbers'.format(inputs))
    return selected_habits


def choice_exec(my_func):
    """The function is a decorator function for functions check_off(), track(), track_off(), delete_habit(). It takes
    a function as an argument and returns an inner function wrapper(). The inner function wrapper() takes a list of
    the habits and an instance of the HabitsList class as arguments. Depends on the list of habits it takes a user's
    choice of habit_id and passes it to the nested function as an argument along with an instance of HabitList class and
    keyword arguments if necessary."""
    @wraps(my_func)
    def wrapper(list_of_habits, habits_list, **kwargs):
        while True:
            id = input("Enter an id of a habit or 0 to return to Previous Menu: ")
            try:
                int_id = int(id)
                if 0 < int_id <= len(list_of_habits):
                    habit_id = list_of_habits[int_id - 1].id
                    my_func(habit_id, habits_list, **kwargs)
                    break
                elif not int_id:
                    break
            except ValueError:
                print("{0} is not a valid habit number".format(id))
    return wrapper


def show_habits(habits, tracked=False, period=None, longest_streak=None):
    """The function takes a list of habits and prints it for the whole breadth of the page(80 characters).
    If the keyword argument tracked=True, in the header will be added word 'tracked'. If keyword argument period=True,
    in the header will be added ' with the same period'. If the longest_streak=True, in the header will be added ' with
    the longest streak'. It converts date into strings and periods into string representations."""
    header_string = '{0}{1}Habit{2}{3}{4}'.format('List of ' if not longest_streak else '',
                                                  'Tracked ' if tracked else '', 's' if not longest_streak else '',
                                                  ' with the longest streak' if longest_streak else '',
                                                  ' with the same period' if period else ''
                                                  )
    print('{0:-^80}'.format(header_string))
    print('Id', '' * 2, 'Name', ' ' * 27, 'Period', '', 'Longest Streak', '', 'Last Completed on')
    for habit in habits:
        print('{0: <3} {1: <32} {2: ^7} {3: ^14} {4: ^17}'.format(habits.index(habit) + 1, habit.name,
                                                                  'Weekly' if habit.period == 7 else 'Daily',
                                                                  habit.longest_streak,
                                                                  date_transform(habit.tracking[-1])
                                                                  if habit.tracking else ''))
    print('\n')


def load_predefined(predefined, habits_list):
    """The function takes a tuple with predefined habits and an instance of the HabitsList class and calls new_habit()
    method to create new habits from the predefined habits.
    """
    for habit in predefined:
        habits_list.new_habit(*habit)


def date_transform(date):
    """The function checks the date given as an argument and return date as a string."""
    if isinstance(date, datetime.datetime):
        return date.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return date[:19]


def process_query(records, habits_list):
    """The function takes list of the list with the attributes of instances of Habit class and maps it to new_habit()
    method to create habits from the database."""
    if records:
        for row in records:
            habits_list.new_habit(row[1], row[2], row[3], bool(row[4]), row[5], json.loads(row[6]), row[7])


@choice_exec
def check_off(habit_id, habits_list):
    """The function is wrapped by decorator @choice_exec. It takes as arguments habit ID and an instance of the class
    HabitsList and then calls method check_off() and track_habit() of the class HabitsLIst."""
    habits_list.check_off(habit_id)
    habits_list.track_habit(habit_id)


@choice_exec
def track(habit_id, habits_list):
    """The function is wrapped by decorator @choice_exec. It takes as arguments habit ID and an instance of the class
    HabitsList and then calls method track_habit() of the class HabitsLIst."""
    habits_list.track_habit(habit_id)


@choice_exec
def track_off(habit_id, habits_list):
    """The function is wrapped by decorator @choice_exec. It takes as arguments habit ID and an instance of the class
    HabitsList and then calls method track_habit() with the kwarg tracked=False of the class HabitsLIst."""
    habits_list.track_habit(habit_id, tracked=False)


@choice_exec
def delete_habit(habit_id, habits_list):
    """The function is wrapped by decorator @choice_exec. It takes as arguments habit ID and an instance of the class
    HabitsList and then calls method delete_habit() of the class HabitsLIst."""
    habits_list.delete_habit(habit_id)


def quit_app():
    """The function terminates execution of the app."""
    print("Thank you for using your habit tracker today.")
    sys.exit(0)


if __name__ == "__main__":
    main()
