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
if filter_type == "genre":
    choose_genre = input("Choose a genre:\n"
                         "-----------------------\n"
                         "1. Non-Fiction\n"
                         "2. Science Fiction\n"
                         "3. Mystery\n"
                         "4. Historical Fiction\n"
                         "5. Romance\n"
                         "6. Other\n").strip()

    amt_res = int(input("How many results would you like? "))
    if amt_res < 0:
        print("Results must be greater than 0")
        amt_res = int(input("Try again: "))

    traversal_in = input("bfs or dfs: ").strip().lower()
    if traversal_in == "bfs":
        traverse.bfs(root, choose_genre, amt_res)
    elif traversal_in == "dfs":
        # traverse.bfs(root)
        traverse.dfs(root, choose_genre, amt_res)
