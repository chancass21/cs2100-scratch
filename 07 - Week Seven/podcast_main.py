'''
    Create some podcasts for practice and use some getters and setters :)
'''

from podcast import Podcast

def main() -> None:
    ''' create a few podcasts for examples, add episodes and print them '''
    nobody = Podcast(title = "Nobody Asked Us",
                     host = "Des and Kara")
    redhanded = Podcast(title = "Redhanded",
                        host = "Hannah and Suruthi")

    nobody.add_episode("Winter Olympics", 51)
    nobody.add_episode("NB Track", 68)
    nobody.host = "Kara and Des" # calls the setter!

    redhanded.add_episode("Au Pair Affair", 72)
    redhanded.add_episode("OJ Simpson", 212)
    redhanded.title = "Red Handed" # calls the setter!

    print(nobody)
    print(redhanded)

    # print("\nHere are some things NOT to do :):):)...")
    # print(nobody._host) # works, but python gives warning
    # # print(nobody.__total_duration) # python doesn't even let this happen!
    # print(nobody._Podcast__total_duration) # name mangling works, but also don't do it

if __name__ == "__main__":
    main()
