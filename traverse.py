import tree_build
from texttable import Texttable

from collections import deque

def table_print(node, counts, row_count):
    # taking multiple inputs
    print_table = Texttable()
    print_table.header(["Filter", "Title", "Author", "ISBN", "Rating"])
    print_table.set_cols_width([30, 20, 20, 20, 10])
    for book in node.books:
        if row_count < counts:
            print_table.add_row([node.value, book.title, book.author, book.isbn, book.rating])
            row_count += 1
        else:
            print(print_table.draw())
            break

def bfs (root, genre, counts):
    queue = deque([root])
    row_count = 0
    while queue:
        node=queue.popleft()
        if node.books and node.value.lower() == genre.lower():
            # print(f"Node [{node.value}]->{[book.title for book in node.books]}")
            # print(f"Node [{node.value}]->{[(book.title, book.author, book.isbn, book.rating) for book in node.books]}")
            table_print(node, counts, row_count)
        queue.extend(node.children)


def dfs (root, genre, counts):
    stack=[root]
    row_count = 0
    while stack:
        node=stack.pop()

        # if node.books and node.value.lower() == filter_value:
        if node.books and node.value.lower() == genre.lower():
            table_print(node, counts, row_count)
        stack.extend(reversed(node.children))

