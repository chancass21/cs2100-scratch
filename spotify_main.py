'''
    Create some podcasts and albums, and some generic spotify content

    Download the CSV: https://bit.ly/4kEjxEf

    Some things to keep an eye out that'll be useful for HW5:
     * in spotify_content.py we create our own error type
     * here, we read from a CSV file into a 2d list of strings
     * we use isinstance(obj, ) to see if an ojbect is a Podcast or an Album
     * but, isinstance(obj, SpotifyContent) will return True for every single object
             that is Podcast or Album or SpotifyCOntent
     * we use type(obj) == SpotifyContent instead to see if it's superclass and not
             subclass
    * when we print obj.__dict__, we see: superclass's methods/attributes first,
        then subclass's. Note the name mangling for _SpotifyContent__total_duration because 
        we inherit a private attribute.
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
    # use our own version of __eq__
    # overriding __eq__ impacts: p1 == p2, p1 in lst, lst.count(p1)
    print("\n=== Looking for anything multiple people like :) ===")
    dupes = [item for item in object_list if object_list.count(item) > 1]
    for dupe in dupes:
        print(dupe)

    # now we've got our object list, let's check out the different
    # subclass / superclass subtleties
    # Here, split into three lists: album, podcast, generic
    print("\n=== Filtering by type ===")
    pods = [obj for obj in object_list if isinstance(obj, Podcast)]
    albums = [obj for obj in object_list if isinstance(obj, Album)]
    # doesn't do what we expect, counts ALL subclass objects of SpotifyContent
    # generic = [obj for obj in object_list if isinstance(obj, SpotifyContent)] :(:(
    generic = [obj for obj in object_list if type(obj) == SpotifyContent]
    print(f"Podcasts: {len(pods)}")
    print(f"Albums: {len(albums)}")
    print(f"All other content: {len(generic)}")


    # Each class's __str__ is different, but we call them the same way, this is polymorphism
    print("\n=== polymorphism! ===")
    for obj in object_list[7:]:
        print(f"{type(obj)}... {obj}\n")

    # what methods and attributes do we have in each one? 
    print("\n=== which attributes and methods? ===")
    print("=== super class's info first, then sublcass===")
    for obj in object_list[12:]:
        print(obj.__dict__, "\n")

if __name__ == "__main__":
    main()
