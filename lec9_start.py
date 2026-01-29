'''
    CS2100
    Spring 2026

    Starter code for lecture on 1/29/26

    The starter code is just comments! We're working with the file 
    all_games.py, which is a dataset containing PWHL games from 2023-2025

    We'll be using Pandas today, which is a Python library that is super handy
    for working with files, especially files that are messy, have mixed data types, etc.

    Pandas Documentation: https://pandas.pydata.org/docs/

    Instructions:
    - each comment below describes a task we want to accomplish using pandas
    - with a teammate, look up in the pandas documentation how it should work
    - then we'll put it into the real code below
'''

import pandas as pd

#######################################################
#
# PART ONE 
#
#######################################################

# 1. read all_games.csv into a dataframe
GAMEFILE = "all_games.csv"
df = pd.read_csv(GAMEFILE, encoding = "utf")

# 2. what's in the dataframe?

# Information about each game, like points, location, date, and goals.
print("Print the dataframe...")
print(df) 
print("\nPrint the first 10 rows of the dataframe.")
print(df.head(10))

# 3. how big is the dataframe? how many rows/columns?

# 191 x 16
print("\nPrinting out df.shape (rows first, columns second)")
print(df.shape)

# 4. what are the names of the columns in the dataframe? 

# id,season_id,game_number,date,home_team,visiting_team,home_goal_count,visiting_goal_count,periods,overtime,shootout,status,game_status,venue_name,venue_location,attendance
print("\nWhat columns do I have?")
print(df.columns)

# 5. what are the datatypes of the columns?

# Strings and floats/ints
print("\nWhat datatypes do I have?")
print(df.dtypes)


#######################################################
#
# PART TWO 
#
#######################################################

# 6. ask the user for a column name and tell them if it's there
col = input("What column are you looking for?\n")
if col in df.columns:
    print(df[col])
else:
    print(f"{col} does not exist")

# 7. make a copy of the dataframe. (bonus question: why??)
df_copy = df.copy()

# 8. add a new column that has total goals (instead of home goals, visit goals)
df_copy["total_goals"] = df_copy["home_goal_count"] + df_copy["visiting_goal_count"]
print("\n printing out just the columns I like from my dataframe.")
print(df_copy[["total_goals", "home_goal_count", "visting_goal_count"]])

# 9. how many games went into overtime?
overtimes = len(df_copy[df_copy["overtime"] > 0])
print(overtime)

# 10. how many times were there 0 total goals in a game? 1? 2? 3? ...

# 11. can we sort the dataframe by date?

#######################################################
#
# PART THREE 
#
#######################################################

# 12. filter the dataframe so we just see the rows where total goals were 0


# 13. filter the dataframe so we just see boston vs new york
# (either could be home/visiting)
# (boston team is 1, NY is 4)


# 14. Print out boston vs new york, but only some of the columns, so we see
# who was the home team, how many goals the home team had, how many goals the visiting
# team had. 


# 15. How many games had boston vs new york?


# 16. how many of those games did boston win?


