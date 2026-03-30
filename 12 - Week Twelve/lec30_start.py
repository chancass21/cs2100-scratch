'''
    CS2100
    Spring 2026
    sample code from class 3/30/26

    We start with nodes A, B, C, D, E all in their own disjoint sets

    Then we union A, B. What should be A.rank, A.parent, B.rank, B.parent?

    Then we union C, D. What should be C.rank, C.parent, D.rank, D.parent?

    Then we union D, E. What should be D.rank, D.parent, E.rank, E.parent?
'''

from __future__ import annotations
from typing import Any


class Node:
    ''' A graph node with support for disjoint set operations (Union-Find). '''

    def __init__(self, data: Any):
        self.data = data
        self.parent = self  # Initially, each node is its own parent
        self.rank = 0

    def find_set(self) -> Node:
        '''
        Implement the find operation for Union-Find.
        Find the representative of the set to which this node belongs.
        For now, don't use path compression.

        Returns:
            The representative node of the set
        '''
        if self.parent == self:
            return self
        return self.parent.find_set()

    def union(self, other: Node) -> None:
        '''
        Implement the union operation for Union-Find.
        Merges the two sets to which this node and the other node belong.
        Use union by rank for efficiency.

        Args:
            other: The other node to union with
        '''
        


    def __str__(self) -> str:
        ''' return string formatted node '''
        return str(self.data)


def main() -> None:
    ''' get some practice with union-find '''
    # Five nodes, each in its own set
    # what does find() do in each case below?
    A, B, C, D, E = [Node(c) for c in 'ABCDE']

    print("=========== at the beginning, each node should be its own parent =========")
    print(A.find_set())
    print(B.find_set())
    print(C.find_set())
    print(D.find_set())
    print(E.find_set())

    # 5 nodes, standalone, what does union do in each case below?
    # what happens to rank, parent?
    A, B, C, D, E = [Node(c) for c in 'ABCDE']

    print("=========== union A, B. What should be A.rank, A.parent, B.rank, B.parent?  =========")
    A.union(B)
    print(f"A.rank = {A.rank}, A.parent = {A.parent}")
    print(f"B.rank = {B.rank}, B.parent = {B.parent}")

    print("=========== union C, D What should be C.rank, C.parent, D.rank, D.parent?  =========")
    C.union(D)
    print(f"C.rank = {C.rank}, C.parent = {C.parent}")
    print(f"D.rank = {D.rank}, D.parent = {D.parent}")

    print("=========== union D, E What should be D.rank, D.parent, E.rank, E.parent?  =========")
    D.union(E)
    print(f"D.rank = {D.rank}, D.parent = {D.parent}")
    print(f"E.rank = {E.rank}, E.parent = {E.parent}")

    print("=========== Now what happens when I find_set on A, B, C, D, E? =========")
    print(f"A.find_set()... {A.find_set()}")
    print(f"B.find_set()... {B.find_set()}")
    print(f"C.find_set()... {C.find_set()}")
    print(f"D.find_set()... {D.find_set()}")
    print(f"E.find_set()... {E.find_set()}")

    print("\n=========== Mini-Kruskal! =========")
    A, B, C, D, E = [Node(c) for c in 'ABCDE']

    # Some makeshift edges; you'll want to do something more robust
    # in homework
    edges = [
        (1, A, B),
        (2, C, D),
        (3, B, C),
        (4, D, E),
        (5, A, E), # the MST should exclude this! 
    ]
    mst: set[Any] =  set()


if __name__ == "__main__":
    main()
