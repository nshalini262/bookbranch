import pandas as pd
import tree_build
import traverse

books_df = pd.read_csv("GoodReads_100k_books.csv")
# getting rid of data points without information
books_df = books_df.dropna(subset=['author', 'desc', 'genre', 'isbn', 'pages', 'rating', 'title', 'totalratings'])
books_df.to_csv("GoodReads_100k_books.csv", index=False)

books = []
for _, row in books_df.iterrows():
    books.append(tree_build.Book(
        row['author'],
        row['desc'],
        row['genre'],
        row['isbn'],
        row['pages'],
        row['rating'],
        row['title'],
        row['totalratings']
    ))

filter_type = input("Filter books by 'genre', 'author' or 'rating': ").strip().lower()

root = tree_build.tree_build(books, filter_type)

choose_filter = ""

if filter_type == "genre":
    choose_filter = input("Choose a genre:\n"
                         "-----------------------\n"
                         "1. Non-Fiction\n"
                         "2. Science Fiction\n"
                         "3. Mystery\n"
                         "4. Historical Fiction\n"
                         "5. Romance\n"
                         "6. Other\n").strip()
elif filter_type == "author":
    choose_filter = input("Enter author name: ").strip()
    print("Note: could display less than selected number of books based on limited dataset.")

elif filter_type == "rating":
    ratings = {
        "1": "0.0-1.0",
        "2": "1.0-2.0",
        "3": "2.0-3.0",
        "4": "3.0-4.0",
        "5": "4.0-5.0"
    }
    rating_choice = input(
        "Choose a rating range (1-5):\n"
        "-----------------------\n"
        "1. 0.0-1.0\n"
        "2. 1.0-2.0\n"
        "3. 2.0-3.0\n"
        "4. 3.0-4.0\n"
        "5. 4.0-5.0\n"
    ).strip()
    choose_filter = ratings.get(rating_choice, None)

try:
    amt_res = int(input("How many results would you like? "))
    if amt_res <= 0:
        raise ValueError
except ValueError:
    print("Results must be a positive integer.")
    exit()

traversal_in = input("bfs or dfs: ").strip().lower()
if traversal_in == "bfs":
    traverse.bfs(root, choose_filter, amt_res)
elif traversal_in == "dfs":
    traverse.dfs(root, choose_filter, amt_res)
