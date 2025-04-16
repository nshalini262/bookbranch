
# filtered_df = df.loc[df['isbn'] < 1906863482, ['author']]

import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "GoodReads_100k_books.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "mdhamani/goodreads-books-100k",
  file_path,
)

print("First 5 records:", df.head())