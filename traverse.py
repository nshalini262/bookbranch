import tree_build
from collections import deque

def bfs (root):
    queue = deque([root])
    while queue:
        node=queue.popleft()
        if node.books:
            print(f"Node [{node.value}]->{[book.title for book in node.books]}")
        queue.extend(node.children)


def dfs (root):
    stack=[root]
    while stack:
        node=stack.pop()
        if node.books:
            print(f"Node [{node.value}]->{[book.title for book in node.books]}")
        stack.extend(reversed(node.children))

