from sqlalchemy import Column, Integer, UnicodeText, Boolean, Date, PickleType
from base import Base

#from random import choice
#from string import letters

import datetime

last_id = 0

#engine = create_engine('sqlite:////tmp/test.db', echo=True)
#Base = declarative_base(bind=engine)
#Session = sessionmaker(bind=engine)
#s = Session()

class Habit(Base):
    __tablename__ = 'habits'
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText)
    spec = Column(UnicodeText, nullable=True)
    period = Column(UnicodeText)
    tracked = Column(Boolean)
    creation_date = Column(Date)
    tracking = Column(PickleType)
    longest_streak = Column(UnicodeText)

    
    def __init__(self, name, period, creation_date=datetime.date.today(), spec="", tracked=False,
                 tracking=[], longest_streak=0):
        self.name = name
        self.spec = spec
        self.period = period
        self.tracked = tracked
        self.creation_date = creation_date #datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        self.tracking = tracking # = TrackingList()
        self.longest_streak = longest_streak

    def match(self, filter):
        return filter in self.name
    '''
#Base.metadata.create_all()



'''
#class TrackingList(List):
    
'''


class HabitsList:
    def __init__(self):
        self.habits = []

    def new_habit(self, name, period, spec):
        self.habits.append(Habit(name, period, spec))

    def _find_habit(self, habit_id):
        for habit in self.habits:
            if str(habit.id) == str(habit_id):
                return habit
        return None

    def modify_name(self, habit_id, name):
        habit = self._find_habit(habit_id)
        if habit:
            habit.name = name
            return True
        return False

    def modify_period(self, habit_id, period):
        habit = self._find_habit(habit_id)
        if habit:
            habit.period = period
            return True
        return False

    def modify_spec(self, habit_id, spec):
        habit = self._find_habit(habit_id)
        if habit:
            habit.spec = spec
            return True
        return False

    def check_off(self, habit_id):
        habit = self._find_habit(habit_id)
        return habit.tracking.append(datetime.datetime.now().timestamp())

    def search(self, filter):
        return [habit for habit in self.habits if habit.match(filter)]

    def analyze_tracking(self, habit_id):
        print(self._find_habit(habit_id).tracking)
'''
