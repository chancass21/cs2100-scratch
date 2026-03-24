'''
    CS2100
    Spring 2026
    Sample code from class -- data pull design pattern, observer design pattern 
'''

import time
import random
from typing import Any
import feedparser

RSS_FEED = "https://www.reddit.com/r/running/.rss"

class Pull:
    ''' Data Pull: we go and check to see what's on the feed 
        (in real life and on HW, you'd see what's NEW on the feed)
    '''
    def __init__(self, url: str):
        ''' initialize with URL for the RSS feed '''
        self._url = url

    def get_feed(self) -> Any:
        ''' data pull: ask for info from the RSS feed '''
        parsed = feedparser.parse(self._url)

        # check for badness
        if parsed.bozo:
            print(f"Warning: problem getting the RSS feed: {parsed.bozo_exception}")
            return

        return parsed.entries

class Observer:
    ''' observer class: wait around for (fake) notifications '''
    def __init__(self, url: str):
        ''' initialize an observer object '''
        self._url = url

    def get_feed(self, pause: int) -> None:
        ''' observer: waiting around forever to see if we get notifications '''
        while True:
            print("========observer waiting============")
            parsed = feedparser.parse(self._url)
            if parsed.bozo:
                print(f"....error parsing rss feed: {parsed.bozo_exception}")
            new_item = False
            for entry in parsed.entries:
                if random.randint(1, 50) == 9:
                    print(f"NEW POST!!!!! {entry['title']}")
                    new_item = True
            time.sleep(pause)

def main() -> None:
    ''' create a data pull object and observer object and pull RSS feeds '''
    pull = Pull(RSS_FEED)
    print("============Data Pull Simulation: what's on the feed?=========")
    entries = pull.get_feed()
    for entry in entries:
        # what is available in each reddit post?
        # print(entry.keys())
        print(entry["title"], "\n")

    observer = Observer(RSS_FEED)
    print("============Observer Simulation: waiting to be notified=========")
    observer.get_feed(3)

if __name__ == "__main__":
    main()
