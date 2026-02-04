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
from pandas.api.types import is_integer_dtype
import numpy as np

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
print(df_copy[["total_goals", "home_goal_count", "visiting_goal_count"]])

# 9. how many games went into overtime?
overtime = len(df_copy[df_copy["overtime"] > 0])
print(overtime)

# 10. how many times were there 0 total goals in a game? 1? 2? 3? ...
zero_goals = len(df_copy[df_copy["total_goals"] == 0])
print(f"\nUsing a filter, we had zero goals this many times... {zero_goals}")

print("\nUsing value_counts(), how many times did we have any # of goals?\n")
print(df_copy["total_goals"].value_counts())

# 11. can we sort the dataframe by date?
sorted_df = df_copy.sort_values(by = "date")
print(f"Datafram sorted by date... {sorted_df[["date", "attendance"]].head()}")

#######################################################
#
# PART THREE 
#
#######################################################

# 12. filter the dataframe so we just see the rows where total goals were 0
sorted_df = df_copy.sort_values(by = ["date", "attendance"], 
                                ascending = [True, False])


# 13. Validate - is the periods "column" all integers?
# (either could be home/visiting)
if is_integer_dtype(df_copy["periods"]):
    print("\nThis column is ints!")
else:
    print("\nColumn was expected to be ints, but is not :(")

# 14. we currently have periods (normally 3, but could be 4, 5, or 6). 
# # add a new column, game_length, n, using the following dictionary and map()
game_length = {3 : "standard", 4 : "one ot", 5 : "two ot", 6 : "three ot"}
df_copy["game_length"] = df_copy["periods"].map(game_length)
print("\nPrintint out dataframe with new game_length column")
print(df_copy[["periods", "game-length"]].head(15))

# 15. Filter the dataframe so we just see Boston vs New York
# (either could be home/visiting)
# (Boston team is 1, NY is 4)
teams = [1, 4]
bos_v_ny = df_copy[df_copy["home_team"].isin(teams) 
                   & df_copy["visiting_team"].isin(teams)]

print(f"\nWe used isin() and & operator to learn that "
      "{len(bos_v_ny)} games featured Boston vs NY")

# 16. Pick a couple of columns and see if they correlate or nah
r = np.corrcoef(df_copy["attendance"], df_copy["home_goal_count"])
print("The r value of attendance, home goal count... numpy gives us"
"a table [[a, b] [c, d]]. a, d are both 1.0 b, c are both the"
"correlation coefficient between attendance and goals\n")
print(r)
