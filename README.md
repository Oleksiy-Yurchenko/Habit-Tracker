# Habit Tracker 

## Habit Tracker App is an app to monitor and manage the habits.

## Installation instructions
To install the habit tracker app the archive with the app should be downloaded from the GitHub and unzipped.

## How to start Habit tracker
To run a habit tracker app module start.py should be started.

## General Comments

In The Habit Tracker App all the timestamps are stored as datetime objects in the attribute tracking of the instance of the class Habit, as this is a part of the requirements. 
All the datetime objects are treated as date object in the application. The practical implication is that the difference between 2 timestamps will be measured in days, 
habits #periods will be measured in days. 

                           Habit due date = last check off + period

This is the formula to determine if habit is overdue or not. As we are dealing with dates all the expirations will happen with the change of the day at midnight. 

##User Instuctions
Once app is running select required menu options by pressing a corresponding number. 
1. By selecting "1. Show habits" we will load the next menu (sub menu). 
2. By pressing "2. add habit" we can add habit, by pressing ‘track’, ‘track off’ or ‘check off’ 
habit  we track, track off or check off habits. Option ‘delete habit’ allows us to delete a habit. We can as well load predefined habits. 
There are 7 predefined habits with 4 weekly tracking period.

In this sub menu we can get access to the habits itself. 
By pressing 1 we can get a list of all habits. 
By pressing 2 – activated function tracked() from module analytics and #we can get a list of all tracked habits. 
By pressing 3 – activated function same_period() from module analytics and we can get list of habits with the same period. 
By pressing 4 – activated function longest_streak() from module analytics and we can get a habit with the longest streak among all habits. 
By pressing 5 – we can a habit with #the longest streak among selected habits.

