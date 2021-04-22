# Habit Tracker 

Habit Tracker App is an app to monitor and manage the habits.

### Installation instructions
To install the habit tracker app the archive with the app should be downloaded from the GitHub and unzipped.

### How to start Habit tracker
To run a habit tracker app, module start.py should be started.

### General Comments
Habit tracker's main purpose is to collect and analyze the data about the user's habits. 
Based on the collected data the app can provide a number of the consecutive time periods (set by the user) or streak when the habit was checked off or completed.
User can track or monitor habits, track off habits and delete habits.

The Habit tracker functionality can provide the following:
* List of all habits,
* List of the currently tracked habits,
* List of the habits with the same period,
* The habit with the longest streak among all habits,
* The habit with the longest streak among selected habits.

In addition user can load set of 7 predefined habits with tracking period of 4 weeks when required. 

Some of the habit's data is input by the user and rest is collected by the app. 
The user inputs the following data: 
* habit's name, 
* period (max period of time when the habits needs to be checked off),
* specification or description.
* time when the habit or task is completed or checked off.

The app among collects date and time when the app was created.

The Habit Tracker App treats all date and time data as dates. So, period in the habit tracker is a number of days.
If the number of days between "check off" events exceeds the period, than the current streak of the habit is reset to 0.


### User Instructions
Once app is running select required menu options by pressing a corresponding number. 
1. By pressing number "1" which corresponds to "Show habits" we will load the next menu (sub menu) where we can display various analytics views. 
2. By pressing number "2" which corresponds to "Add habit" we can add a new habit to the app.
3. By pressing "3" which corresponds to "Track habit" the habit can be tracked or monitored.
4. By pressing "4" which corresponds to "Track off habit" the habit can be tracked off or removed from monitor.
5. By pressing "5" which corresponds to "Check off habit" the habit can be checked off.
6. By pressing "6" which corresponds to "Delete habit" the habit can be deleted.
7. By pressing "7" which corresponds to "Load predefined habits" the redefined habits can be loaded.
0. By pressing "0" which corresponds to "Quit" the habit can be quitted.

In this sub menu we can get access to the habits itself by displaying them. 
Here we can choose various options of teh habits representation. 
1. By pressing "1" we can get a list of all the habits. 
2. By pressing "2" we can display a list of all presently tracked habits. 
3. By pressing "3" we can get list of habits with the same period. 
4. By pressing "4" we can obtain a habit with the longest streak among all habits. 
5. By pressing "5" we can print to the screen a habit with the longest streak among the selected habits.
6. By pressing "6" we can return to the previous menu.

