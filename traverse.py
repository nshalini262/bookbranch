import tree_build
from texttable import Texttable

from collections import deque


def print_table(filter_value, books, max_rows):
    table = Texttable()
    table.header(["Filter", "Title", "Author", "ISBN", "Rating"])
    table.set_cols_width([30, 20, 20, 20, 10])

    for i, book in enumerate(books):
        if i < max_rows:
            table.add_row([filter_value, book.title, book.author, book.isbn, book.rating])
        else:
            break

    print(table.draw())


def bfs(root, filter_value, counts):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.books and node.value.lower() == filter_value.lower():
            print_table(node.value, node.books, counts)
            break
        queue.extend(node.children)


def dfs(root, filter_value, counts):
    stack = [root]

    while stack:
        node = stack.pop()
        # if node.books and node.value.lower() == filter_value:
        if node.books and node.value.lower() == filter_value.lower():
            print_table(node.value, node.books, counts)
            break
        stack.extend(reversed(node.children))

