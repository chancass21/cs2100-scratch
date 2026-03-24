'''
    Create some podcasts and albums, and some generic spotify content
    
'''

from spotify_content import SpotifyContent
from podcast import Podcast
from album import Album


# store the name of the datafile and the mapping of column
# names to positions
DATAFILE = "spotify_data - Form Responses 1.csv"
COLUMNS = { "type" : 1,
            "title" : 2,
            "creator" : 3,
            "genre" : 4}

def read_csv(filename: str) -> list[list[str]]:
    ''' read a csv file into a 2d list 
        parameters: filename, a string, the CSV file to read
        returns: a 2d list of strings, the content of the file
        raises: FileNotFound error if file not found
    '''
    data = []
    with open(filename, "r", encoding = "utf-8") as infile:
        for row in infile:
            data.append(row.lower().strip().split(","))
    return data[1:]

def make_objects(lst: list[list[str]], cols: dict[str, int]) -> list[SpotifyContent]:
    ''' make SpotifyContent objects out of 2d list of strings 
        parameters: 
            lst, a 2d list of strings, each row has data for one object
            cols, a dictionary of str:int, which specifies which column
                in the 2d list to find particular values
        returns:
            a list of SpotifyContent objects, one per row of 2d list
        raises:
            ValueError if list is empty
    '''
    if not lst:
        raise ValueError("List must not be empty :(")
    objs = []
    for row in lst:
        if row and row[cols["title"]] and row[cols["creator"]]:
            match row[cols["type"]].lower():
                case "podcast":
                    objs.append(Podcast(row[cols["title"]], row[cols["creator"]]))
                case "album":
                    objs.append(Album(row[cols["title"]], row[cols["creator"]], row[cols["genre"]]))
                case _:
                    objs.append(SpotifyContent(row[cols["title"]], row[cols["creator"]]))
    return objs

def main() -> None:
    ''' create some objects out of super class and sub class '''
    lst = read_csv(DATAFILE)
    object_list = make_objects(lst, COLUMNS)

    # did we have anything in common??
    print("\n=== Looking for anything multiple people like :) ===")

    # now we've got our object list, let's check out the different 
    # subclass / superclass subtleties
    # Here, split into three lists: album, podcast, generic
    print("\n=== Filtering by type ===")

    # how many of each type do we have?
    print("\n=== Type distribution ===")

    # Each class's __str__ is different, but we call them the same way, this is polymorphism
    print("\n=== polymorphism! ===")

    # what methods do we have in each one? 
    print("\n=== which methods? ===")


if __name__ == "__main__":
    main()
