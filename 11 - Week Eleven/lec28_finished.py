'''
    cs2100
    Spring 2026
    starter code for class on 3/25/26

    VERY similar, nearly identical to earlier code where we 
    used a tree to rep a file system.
    But now the file system is housed via webpages and links.

    In class, we'll...
    * Scrape the initial starting page, looking for titles and links
    * For all of the children (id'ed by <a href>), scrape and add as child
    We'll also finish off main, to navigate this new file system
'''


from __future__ import annotations
import requests
from bs4 import BeautifulSoup


class Webpage:
    ''' class to rep a webpage '''
    _base_url = "https://khoury.northeastern.edu/home/laney/crawl"

    def __init__(self, page: str):
        ''' create a webpage '''
        self.page = page
        self.title = ""
        self.children: list[Webpage] = []

    def add(self, child: Webpage) -> None:
        ''' add a child to this page '''
        print(f"adding {child.title} to {self.title}")
        self.children.append(child)

    def print_tree(self) -> None:
        ''' print all the titles in the subtree rooted at this node '''
        print(self.title)
        for c in self.children:
            c.print_tree()

    def count_nodes(self) -> int:
        ''' count all the nodes in the subtree rooted here '''
        num = 1
        for c in self.children:
            num += c.count_nodes()
        return num

    def scrape(self) -> None:
        ''' recursively scrape this webpage and its links,
            building tree as we go 
            step one in anything recursive on a tree: solve problem for the root!
            Then, same problem, smaller trees
        '''
        print(f"scraping {type(self)._base_url}/{self.page}")
        response = requests.get(f"{type(self)._base_url}/{self.page}", timeout = 5)
        if response.status_code != 200:
            raise ValueError(f"Error fetching url: {self.page}")

        bs = BeautifulSoup(response.text, "html.parser")

        if not bs or not bs.title:
            raise ValueError("scraping error")

        self.title = bs.title.get_text()
        links = bs.find_all("a", href = True)
        for link in links:
            try:
                child = Webpage(str(link.get("href")))
                child.scrape()
                self.add(child)
            except ValueError as e:
                print(f"skipping page {self.page} due to exceiption {e}")


    def ls(self) -> None:
        ''' print the names of this page's children '''
        if not self.children:
            print("(no children)")
        for child in self.children:
            print(child.title)

    def pwd(self, path: list[Webpage]) -> str:
        ''' return the path from root to this node '''
        s = ""
        for node in path:
            s += str(f"{node.title} > ")
        return s

    def cd(self, title: str, path: list[Webpage]) -> Webpage:
        ''' return the node with the given title, or raise an error.
           updates the given path to match the navigation.
           parameters: name (str), the folder name to navigate to
                       path (list of Folders), the current path
           returns: a Folder object, where we have navigated to
           raises: ValueError if invalid folder name given
        '''
        if title == "..":
            if len(path) <= 1:
                print("Already at root")
                return self
            path.pop()
            return path[-1]
        for child in self.children:
            if child.title == title:
                path.append(child)
                return child
        raise ValueError("No such folder")


def navigate(root: Webpage) -> None:
    ''' navigate through the file system rooted at the given Webpage,
        in response to user commands in the terminal. Runs until
        user provides quit command.
        parameters: root, a Webpage
        returns: none
    '''
    current = root
    path = [root]
    while True:
        command = input(f"\n[{current.title}] > ").strip()
        if command == "ls":
            current.ls()
        elif command == "pwd":
            print(current.pwd(path))
        elif command.startswith("cd "):
            name = command[3:]
            try:
                current = current.cd(name, path)
            except ValueError:
                print("Command failed, try again!")
        elif command == "quit":
            break
        else:
            print("Commands: ls, cd <name>, cd .., pwd, quit")


def main() -> None:
    ''' scrape a website --- start with some practice using bs4'''
    response = requests.get("https://khoury.northeastern.edu/home/laney/crawl/documents.html",
                            timeout = 5)
    if response.status_code != 200:
        raise ValueError(f"Error fetching url: {response.status_code}")

    # parse the HTML from the web page we just request.get'ed
    bs = BeautifulSoup(response.text, "html.parser")

    # print out JUST the text of the page
    print(bs.get_text())

    # get the title of the page, including <title>xxx</title>
    print(bs.title)
    # get the title of the page, text only
    if bs.title:
        print(bs.title.get_text())

    # get all the links of the web page (these will be children)
    links = bs.find_all("a", href = True)
    for link in links:
        print(link.get("href"))

    print("\n\n........now for the crawler and navigator........\n")
    # crawl the mini website
    documents = Webpage("documents.html")
    documents.scrape() # recursively scrape this page and all its children
    navigate(documents)




if __name__ == "__main__":
    main()
