"""Lecture 6 - Team 1 Sets"""

empty_set = set()
s = {1, 2, 3}
# can't use an empty curly brackets because its considered a definition
s.add(4)
s.remove(2)

# s[0] = 4 doesn't work
# s now has {1, 3, 4}

s = {(1, 2), (3, 4)}

# can't create a list of sets
