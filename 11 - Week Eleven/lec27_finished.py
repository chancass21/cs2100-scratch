'''
    CS2100
    Spring 2026
    Finished code from lecture 27, 3/23/26

   Building on last week's code to represent a file system as a tree

   Folder class has two attrs: name (str) and children (list of Folders)

   In main, we create Folder objects and call add() method to
   define parent/child relationships and build out the whole tree.

   Today we:
    * implemented recursive method get_max(), which returns the node
      with the greatest number of children
    * overrode __gt__, which returns True if self has more children
      than other
    * implemented methods for a mini-terminal: cd, ls, pwd
    * used the navigate() function, which was part of starter code.
      you'll want something similar for the next HW, feel free to reuse
      anything here -- you'll need to adapt for the HW requirements,
      but the basic structure should be similar.
'''

class Folder:
    ''' class to rep a folder in a file system '''
    def __init__(self, name: str):
        ''' initialize with name, and empty children '''
        self.name = name
        self.children: list[Folder] = []

    def add(self, child: Folder) -> None:
        ''' add a child to this node '''
        self.children.append(child)

    def count_nodes(self) -> int:
        ''' how many nodes in the subtree rooted here? '''
        num = 1                     # solve problem for the root
        for c in self.children:     # same problem, smaller trees
            num += c.count_nodes()  # recursive call
        return num

    def print_tree(self) -> None:
        ''' print the subtree rooted at this node '''
        print(self.name)            # solve the prolem for the root
        for c in self.children:     # same problem, smaller trees
            c.print_tree()          # recursive call

    def __gt__(self, other: object) -> bool:
        ''' return a bool indicating self > other
            return NotImplemented if other is not a Folder object
        '''
        if not isinstance(other, Folder):
            return NotImplemented
        return len(self.children) > len(other.children)

    def get_max(self) -> Folder:
        ''' recursively find and return the node
            with the max # of children 
        '''
        curr_max = self
        for c in self.children:
            child_max = c.get_max()
            if child_max > curr_max:
                curr_max = child_max
        return curr_max

    def ls(self) -> None:
        ''' print the names of this folder's children '''
        if not self.children:
            print("no children")
        for c in self.children:
            print(c.name)

    def pwd(self, path: list[Folder]) -> str:
        ''' return the path from the root to this node '''
        s = ""
        for folder in path:
            s += f"{folder.name}/"
        return s

    def cd(self, name: str, path: list[Folder]) -> Folder:
        ''' return the Folder with the given name, update the path '''
        if name == "..":
            if len(path) <= 1:
                print("at root")
                return self
            path.pop() # remove the folder at the end of the path
            return path[-1] # this is the new current folder
        for c in self.children:
            if c.name == name:
                path.append(c)
                return c
        raise ValueError("bad cd command :(")

def navigate(root: Folder) -> None:
    ''' navigate through the file system rooted at the given Folder,
        in response to user commands in the terminal. Runs until
        user provides quit command.
        parameters: root, a Folder
        returns: none
    '''
    current = root
    path = [root]
    while True:
        command = input(f"\n[{current.name}] > ").strip()
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
    ''' make a file system tree based on laney's files '''
    docs = Folder("documents")
    git = Folder("github.txt")
    nu = Folder("NU")
    fall = Folder("2025Fall")
    spring = Folder("2026spring")
    pics = Folder("pics")
    run = Folder("running")

    # create the structure
    # docs is the root of the entire tree
    # docs has children: git, nu, pics run
    # nu has children: spring, fall
    docs.add(git)
    docs.add(nu)
    docs.add(pics)
    docs.add(run)
    nu.add(fall)
    nu.add(spring)


    print(".......call count nodes on entire tree, should be 7.......")
    print(docs.count_nodes())
    print("...... call count nodes on a leaf, should be 1........")
    print(git.count_nodes())
    print(pics.count_nodes())
    print("\n\n........print the entire tree.........")
    docs.print_tree()
    print("......print a leaf........")
    git.print_tree()

    print("\n\n.......which node has the most children?.......")
    print("....for pics, should be pics....")
    max_node = pics.get_max()
    print(max_node.name)
    print(".....for nu, should be nu.....")
    max_node = nu.get_max()
    print(max_node.name)
    print("......for the whole tree, should be documents....")
    max_node = docs.get_max()
    print(max_node.name)

    # practice our navigation
    print(".......test our mini terminal!!!!!..........")
    navigate(docs)

if __name__ == "__main__":
    main()
