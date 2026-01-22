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

"""Team 1 -- Write Function to Generate Sets"""
# We'll work on transforming a 2D list of strings (read from a file) into a
# dictionary where keys are strings, and vlues are sets.
# Below are unittests; write a function that would pass the tests. 
# Don't worry about edge cases or documentation. 

def list_to_sets(l: list[list[str]]) -> dict[str, set[str]]:
    """
    Transform 2D list of strings into a dictionary where keys are strings
    and values are sets
    """
    pass

start_list = [["a"], ["b"], ["c"]]
expected = {"a": set(), "b": set(), "c": set()}
actual = list_to_sets(start_list)
self.assertEqual(expected, actual)


start_list1 = ["a","b", "c"]
expected1 = {"a" : {"b", "c"}}
actual1 = list_to_sets(start_list2)
self.assertEqual(expected1, actual1)

start_list2 = [["a", "b", "c"], ["d", "e", "f"]]
expected2 = {"a" : {"b", "c"}, "d" : {"e", "f"}}
actual2 = list_to_sets(start_list)
self.assertEqual(expected2, actual2)