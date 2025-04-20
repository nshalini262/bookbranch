import pandas as pd

books_df = pd.read_csv("GoodReads_100k_books.csv")

# filtering the data for relevant columns
books_df = books_df.dropna(subset=['author', 'desc', 'genre', 'isbn', 'pages', 'rating', 'title', 'totalratings'])
