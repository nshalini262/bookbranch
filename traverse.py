import tree_build
from collections import deque


# perform Breadth First Search
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
    return second

# perform Depth First Search
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
    return second


# wrapper functions for UI
def bfs_collection(root, filter_value, counts, rating_filter = None):
    return bfs(root, filter_value, counts, rating_filter)

def dfs_collection(root, filter_value, counts, rating_filter = None):
    return dfs(root, filter_value, counts, rating_filter)

