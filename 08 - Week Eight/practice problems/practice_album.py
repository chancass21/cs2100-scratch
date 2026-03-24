'''
    Practice problems for inheritance!

    In class, we created a SpotifyContent class, which could be anything on spotify -- a podcast,
    an album, an audio book, etc. Then we wrote one subclass, Podcast.

    For practice, write another subclass, Album. It should:
    - inherit from SpotifyContent
    - add any attributes that are specific to Album (our sample solution added genre and a songs list)
    - add @property and setter methods for any attributes you add, validating appropriately
    - add a @property and setter for artist, which alises to SpotifyContent's creator
    - implement its own len() method via __len__
    - implement a method to add a song to the album
'''