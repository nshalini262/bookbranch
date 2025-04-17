import pandas as pd
import tree_build
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



