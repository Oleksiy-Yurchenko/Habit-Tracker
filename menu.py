import sys, datetime, sqlalchemy
from habit import Habit
from habits import HabitsList
from analytics import tracked, same_period, longest_streak
from predefined_habits import PREDEFINED_HABITS
from base import Session




YES = frozenset({"y", "Y", "yes", "Yes", "YES"})
NO = frozenset({"n", "N", "no", "No", "NO"})
#habits_list = HabitsList()


def main():
    #check on start up if the db has habits table
    try:
        session = Session()
        habits_list = session.query(Habit).all()
    except sqlalchemy.exc.OperationalError:
        habits_list = HabitsList()        
        create_objects(PREDEFINED_HABITS, habits_list)
    tracked_list = tracked(habits_list.habits)
    habit_status(tracked_list)

    main_menu(habits_list)

def habit_status(tracked_list):
    today = []
    broken_streak = []
    for habit in tracked_list:
        if habit.tracking:
            if (datetime.date.today() - habit.tracking[-1]).days - habit.period == 0:
                today.append(habit)
            elif (datetime.date.today() - habit.tracking[-1]).days - habit.period > 0:
                print("overdue")
                if habit.longest_streak < len(habit.tracking):
                    habit.longest_streak = len(habit.tracking)
                habit.tracking = [datetime.date.today()]
    show_habits(today)


def main_menu(habits_list):
    while True:
        show_habits(habits_list.habits)
        display_main_menu()
        choice = int(input("Enter an option: "))
        #action = main_menu.get(choice)
        if choice == 1:
            show_menu(habits_list)
            #break
            #show_habits(habits_list.habits)
        elif choice == 2: #add habit
            name = input("Enter a habit's name: ")
            period = input("Enter a habit's periodicity: ")
            spec = input("Enter habit's specipification: ")
            habits_list.new_habit(name, period, spec)
            print("Your habit has been added.")
        elif choice == 3:
            id = int(input("Enter a number of a habit: "))
            habits_list.track(id)
            choice_exec(habits_list.check_off, habits_list.habits)
        elif choice == 4:
            id = int(input("Enter a number of a habit: "))
            habits_list.track(id, tracked=False)
        elif choice == 5:
            choice_exec(habits_list.check_off, habits_list.habits)
        elif choice == 6:
            if habits_list.habits:
                choice_exec(habits_list.delete_habit, habits_list.habits)
            else:
                print("There are no habits to delete.")
        elif choice == 7:
            quit()
        else:
            print("{0} is not a valid choice".format(choice))

def show_menu(habits_list):
    while True:
        display_show_menu()
        choice = int(input("Enter an option: "))
        if choice == 1:
            show_habits(habits_list.habits)
        elif choice == 2:
            show_habits(tracked(habits_list.habits))
        elif choice == 3:
            period = input("Enter a period (Weekly, Daily):")
            show_habits(same_period(habits_list.habits, period))
        elif choice == 4:
            if longest_streak(habits_list.habits):
                show_habits(longest_streak(habits_list.habits))
            else:
                print("None of habits has streak")
        elif choice == 5:
            selected_habits = select_habits(tracked(habits_list.habits))
            if selected_habits:
                show_habits(longest_streak(selected_habits))
            else:
                print("None of habits were selected.")
        elif choice == 6:
            break

def create_objects(predefined, habits_list):
    for habit in predefined:
            habits_list.new_habit(
                habit["name"],
                habit["spec"],
                habit["period"],
                habit["creation_date"],
                habit["tracked"],
                habit["tracking"],
                habit["longest_streak"]
            )

def display_main_menu():
    print(
            """
Habit Tracker Menu

1. Show habits
2. Add habit
3. Track habit
4. Untrack habit
5. Check off habit
6. Delete habit
7. Modify habit
8. Quit
"""
        )

def display_show_menu():
    print(
    """
1. Show all habits
2. Show all tracked habits
3. Show habits with same periodicity
4. Show habit with the longest streak
5. Show habit with the longest streak among selected habits
6. Back
    """
    )

def select_habits(habits_list):
    selected_habits = []
    break_flag = False
    while True:
        inputs = input("Enter habits numbers separated by the space or 0 to return to previous menu")
        test = inputs.split(" ")
        failed = []
        for i in test:
            if 0 < int(i) <= len(habits_list):
                selected_habits.append(habits_list[int(i)-1])
            elif int(i) == 0:
                break_flag = True
                break
            else:
                failed.append(i)
        if break_flag:
            break
        if failed:
            fail_str = ""
            for i in failed:
                fail_str += i + " "
            print("{0} is not a valid habit number".format(fail_str))
            selected_habits = []
        else:
            break
    return selected_habits

def choice_exec(action, habits_list):
    while True:
        id = int(input("Enter a number of a habit or 0 to return to Previous Menu: "))
        if 0 < id < len(habits_list):
            action(id-1)
            break
        elif not id:
            break
        print("{0} is not a valid habit number".format(id))

def show_habits(habits, Tracked=False, Period=None, longest_streak=None):
    print("=== List of habits ===")
    for habit in habits:
        print("{0}: {1} {2} \n{3} {4}".format(habits.index(habit) + 1, habit.name, habit.period, habit.spec, habit.tracking)) #[0] if habit.tracking else habit.tracking))

def search_habits(habits_list):
    #global habits_list
    filter = input("Search for: ")
    habits = habits_list.habits.search(filter)
    show_habits(habits)

def modify_habit():
    id = input("Enter a note id: ")
    name = input("Enter a name: ")
    period = input("Enter a habit's periodicity: ")
    spec = input("Enter habit's specipification: ")
    if name:
        habits_list.modify_name(id, name)
    if period:
        habits_list.modify_period(id, period)
    if spec:
        habits_list.modify_spec(id, spec)



def quit():
    print("Thank you for using your notebook today.")
    sys.exit(0)


#exception handling SystemExit and KeyboardInterrupt

if __name__ == "__main__":
    main()

'''
def track_habit(habits_list, habit_id, tracked=True):
    #global habits_list
    for habit in habits_list.habits:
        if habit.id == habit_id:
            habit.tracked = tracked

def delete_habit(habits_list, habit_id):
    for habit in habits_list.habits:
        if habit.id == habit_id:
            del habit
            
def add_habit(habits_list):
    name = input("Enter a habit's name: ")
    period = input("Enter a habit's periodicity: ")
    spec = input("Enter habit's specipification: ")
    habits_list.new_habit(name, period, spec)
    print("Your habit has been added.")
    
    
    
                            while True:
                id = int(input("Enter a number of a habit or 0 to come back: "))
                if 0 < id < habits_list.habits[-1].id + 1:
                    habits_list.check_off(id)
                elif id == 0:
                    break
                print("{0} is not a valid id".format(id))
                
                
                            
            id = int(input("Enter a number of a habit: "))
            habits_list.delete_habit(id)
'''
