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
    _base_url = "https://khoury.northeastern.edu/home/laney/crawl"
    ''' class to rep a webpage '''
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
    ''' navigate through the file system rooted at the given Folder,
        in response to user commands in the terminal. Runs until
        user provides quit command.
        parameters: root, a Folder
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
    response = requests.get("https://khoury.northeastern.edu/home/laney/crawl/documents.html")
    if response.status_code != 200:
        raise ValueError(f"Error fetching url: {response.status_code}")


if __name__ == "__main__":
    main()
