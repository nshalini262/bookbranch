import pandas as pd
books_df = pd.read_csv("GoodReads_100k_books.csv")
# getting rid of data points without information
books_df = books_df.dropna(subset=['author', 'desc', 'genre', 'isbn', 'pages', 'rating', 'title', 'totalratings'])
books_df.to_csv("GoodReads_100k_books.csv", index=False)
