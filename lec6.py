"""Lecture 6 - Team 1 Sets"""

s = set()
s = {1, 2, 3}
s.add(4)
s.remove(2)

# s[0] = 4 doesn't work
# s now has {1, 3, 4}

s_a = {(1, 2), (3, 4)} # set of tuples

# can't create a list of sets
# can't create a set of sets
# can't use an empty curly brackets because its considered a definition
