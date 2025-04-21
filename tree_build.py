from collections import deque


class Book:
    # initialize book objects
    def __init__(self, author, desc, genre, isbn, pages, rating, title, totalratings):
        self.author = author
        self.desc = desc
        self.genre = genre
        self.isbn = isbn
        self.pages = pages
        self.rating = float(rating)
        self.title = title
        self.totalratings = totalratings

# initialize tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.books = []
        self.children = []

def get_rating(rating):
    if rating < 1.0:
        return "0.0-1.0"
    elif 1.0 <= rating < 2.0:
        return "1.0-2.0"
    elif 2.0 <= rating < 3.0:
        return "2.0-3.0"
    elif 3.0 <= rating < 4.0:
        return "3.0-4.0"
    else:
        return "4.0-5.0"

def get_genre(genre):
    if "Nonfiction" in genre:
        return "Nonfiction"
    elif "Science Fiction" in genre:
        return "Science Fiction"
    elif "Mystery" in genre:
        return "Mystery"
    elif "Historical Fiction" in genre:
        return "Historical Fiction"
    elif "Romance" in genre:
        return "Romance"
    else:
        return "Other"

# build tree based on filter
def tree_build(books, filter):
    root = TreeNode("Root")
    book_dict = {}
    for book in books:
        if filter == "genre":
            key = get_genre(book.genre)
        elif filter == "author":
            key = book.author
        elif filter == "rating":
            key = get_rating(book.rating)
        else:
            print("Invalid Input!")

        if key not in book_dict:
            node = TreeNode(key)
            node.books.append(book)
            root.children.append(node)
            book_dict[key] = node
        else:
            book_dict[key].books.append(book)

    return root