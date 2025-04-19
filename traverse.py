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


def bfs(root, filter_value, counts, rating_filter = None):
    queue = deque([root])
    second = []
    while queue:
        node = queue.popleft()
        if node.books and node.value.lower() == filter_value.lower():
            for book in node.books:
                if not rating_filter or tree_build.get_rating(book.rating) == rating_filter:
                    second.append(book)
                if len(second) == counts:
                    break

        queue.extend(node.children)
        if len(second) == counts:
            break
    print_table(filter_value, second, counts)


def dfs(root, filter_value, counts, rating_filter = None):
    stack = [root]

    second = []

    while stack:
        node = stack.pop()

        if node.books and node.value.lower() == filter_value.lower():

            for book in node.books:
                if not rating_filter or tree_build.get_rating(book.rating) == rating_filter:
                    second.append(book)
                if len(second) == counts:
                    break

        stack.extend(reversed(node.children))
        if len(second) == counts:
            break
    print_table(filter_value, second, counts)

