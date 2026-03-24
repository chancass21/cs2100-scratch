'''
    CS2100
    Spring 2026
    Sample code from class -- a file system is a tree!
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

if __name__ == "__main__":
    main()
