'''
    CS2100
    Spring 2026

    Starter code for lecture on 2/2/26

    The starter code picks up where we left off on Thursday 1/29! 
    We're working with the file  all_games.csv, which is a dataset containing PWHL games from 2023-2025

    Instructions:
    - jump down to PART TWO, CONTINUED
    - read up on the Pandas documentation to answer the questions - https://pandas.pydata.org/docs/
    - code up your answers and see how they work!
    - we'll go over them all together
'''

import pandas as pd

GAMEFILE = "all_games.csv"

#######################################################
#
# PART ONE 
#
#######################################################

# 1. read all_games.csv into a dataframe
df = pd.read_csv(GAMEFILE, encoding = "utf-8")

# 2. what's in the dataframe?
print("Print the entire dataframe....")
print(df)
print("\nPrint the first 10 rows of the dataframe using head()")
print(df.head(10))

# 3. how big is the dataframe? how many rows/columns?
print("\nPrinting out df.shape (rows first, columns second!)")
print(df.shape)

# 4. what are the names of the columns in the dataframe? 
print("\nWhat columns do I have? They are in df.columns")
print(df.columns)

# 5. what are the datatypes of the columns?
print("\nWhat is the datatype of my column? We use .dtype for this")
print(df["game_number"].dtype)

#######################################################
#
# PART TWO 
#
#######################################################

# 6. ask the user for a column name and tell them if it's there
col = input("What column are you looking for?\n")
if col in df.columns:
    print("Found your column, here it is...")
    print(df[col])
else:
    print(f"{col} does not exist")

# 7. make a copy of the dataframe. (bonus question: why??)
print("\nMaking a copy of my dtaframe")
df_copy = df.copy()

# 8. add a new column that has total goals (instead of home goals, visit goals)
df_copy["total_goals"] = df_copy["home_goal_count"] + df_copy["visiting_goal_count"]
print("\nprinting out just the columns i like from my dataframe")
print(df_copy[["total_goals", "home_goal_count", "visiting_goal_count"]])

# 9. how many games went into overtime? -- Filter
overtimes = len(df_copy[df_copy["overtime"] > 0])
print(f"This many games went into overtime.... {overtimes}")


#######################################################
#
# PART TWO, CONTINUED
#
#######################################################

# 10. how many times were there 0 total goals in a game? 1? 2? 3? ...

# 11. can we sort the dataframe by date? 

# 12. can we sort the dataframe by date and then by attendance?


#######################################################
#
# PART THREE 
#
#######################################################


# 13. Validate - is the "periods" column all integers?
if ... :
    print("\nThis column is ints!")
else:
    print("\nColumn was expected to be ints, but is not :(")

# 14. we currently have periods (normally 3, but could be 4, 5, or 6).
# add a new column, game_length, using the following dictionary and map()
game_length = {3 : "standard", 4 : "one ot", 5 : "two ot", 6 : "three ot"}


# 15. filter the dataframe so we just see boston vs new york
# (either could be home/visiting)
# (boston team is 1, NY is 4)
teams = [1, 4]


#######################################################
#
# PART FOUR 
#
#######################################################

# 16. Pick a couple of columns and see if they are correlated or nah.

