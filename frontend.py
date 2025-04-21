import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import tree_build
import traverse
import time


class BookBranch:

    # initialize popup window
    def __init__(self, master):
        self.master = master
        master.title("Book Branch")


        # read CSV file and filter data
        self.books_df=pd.read_csv("GoodReads_100k_books.csv")
        self.books_df.dropna(subset=['author','desc','genre','isbn','pages','rating','title','totalratings'], inplace=True)

        # initializing table rows from csv
        self.books=[tree_build.Book(row['author'],row['desc'],row['genre'],row['isbn'],row['pages'],row['rating'],
                                    row['title'],row['totalratings'])
                    for _, row in self.books_df.iterrows()]

        self.root=None

        # frontend page formatting - drop down menus for each option: genre/genre type, author/author name, rating/choice and if they want double filters
        self.display_title=tk.Label(master, text="Book Branch", font=("Helvetica", 16))
        self.display_title.pack(pady=10)

        self.framing=tk.Frame(master)
        self.framing.pack(pady=5)

        # titles and drop down menus for filter type
        self.first_filter=tk.Label(self.framing, text="Select filter type:", font=("Helvetica", 10))
        self.first_filter.grid(row=0, column=0, sticky="w")

        self.filter_type_entry=ttk.Combobox(self.framing, values =["genre", "author", "rating"])
        self.filter_type_entry.grid(row=0, column=1)
        self.filter_type_entry.bind("<<ComboboxSelected>>", self.set_filter_values)

        # titles and drop down menus for filter value
        filter_label = tk.Label(self.framing, text="Choose filter value:", font=("Helvetica", 10))
        filter_label.grid(row = 1, column=0, sticky="w")

        self.filter_value_entry=ttk.Combobox(self.framing)
        self.filter_value_entry.grid(row = 1, column = 1)

        # prompt and dropdown for extra filter
        self.rating_prompt = tk.Label(self.framing, text="Further filter by rating?", font=("Helvetica", 10))
        self.rating_prompt.grid(row=2, column=0, sticky="w")

        self.second_rating_prompt = ttk.Combobox(self.framing, values =["yes", "no"])
        self.second_rating_prompt.grid(row = 2,column=1)
        self.second_rating_prompt.bind("<<ComboboxSelected>>", self.rating_dropdown)

        # rating Range
        self.rating_range = tk.Label(self.framing, text="Select rating range:", font=("Helvetica", 10))
        self.rating_range.grid(row=3, column=0, sticky="w")

        self.rating_choice = ttk.Combobox(self.framing, values = ["0.0-1.0", "1.0-2.0", "2.0-3.0",
                                                                  "3.0-4.0", "4.0-5.0"])
        self.rating_choice.grid(row=3, column=1)

        # textbox for desired number of results
        self.result_amount = tk.Label(self.framing, text = "Number of results:", font=("Helvetica", 10))
        self.result_amount.grid(row=4, column=0, sticky="w")

        self.input_value = tk.Entry(self.framing)
        self.input_value.grid(row = 4, column=1)

        self.button = tk.Frame(master)
        self.button.pack(pady = 10)

        # set button for running BFS & DFS
        self.bfs_button = tk.Button(self.button, text = "Run BFS", command = self.run_bfs)
        self.bfs_button.grid(row = 0, column =0, padx = 5)

        self.dfs_button = tk.Button(self.button, text="Run DFS", command=self.run_dfs)
        self.dfs_button.grid(row=0, column=1, padx=5)

        # compare button
        self.compare = tk.Button(self.button, text="Compare BFS vs DFS", command=self.traversal_comparison)
        self.compare.grid(row=0, column=2, padx = 5)

        self.comparison = tk.Label(master, text = "", font = ("Helvetica", 10), fg = "#E91E63")
        self.comparison.pack(pady = 5)

        # reset button
        self.reset_button=tk.Button(self.button, text="Reset Filters", command=self.reset_filters)
        self.reset_button.grid(row=0, column=3, padx=5)


        # table display
        self.table = ttk.Treeview(master, columns = ("Title", "Author", "ISBN", "Rating"), show = "headings")
        for col in ("Title", "Author", "ISBN", "Rating"):
            self.table.heading(col, text = col)
            self.table.column(col, width = 150)
        self.table.pack(padx = 10, pady = 10)

    # after initial category select, these are the dropdown menu options for each
    def set_filter_values(self, event):
        filter_type = self.filter_type_entry.get()
        if filter_type == "genre":
            self.filter_value_entry["values"] = ["Nonfiction", "Science Fiction", "Mystery",
                                                 "Historical Fiction", "Romance", "Other"]
        elif filter_type == "rating":
            self.filter_value_entry["values"] = ["0.0 - 1.0", "1.0-2.0", "2.0-3.0",
                                                                  "3.0-4.0", "4.0-5.0"]
        elif filter_type == "author":
            self.filter_value_entry["values"] = sorted(set(self.books_df['author'].dropna().unique()))
        else:
            self.filter_type_entry["values"] = []

    # second dropdown for if the user wants extra rating filter
    def rating_dropdown(self, event):
        if self.second_rating_prompt.get() == "yes":
            self.rating_range.grid()
            self.rating_choice.grid()
        else:
            self.rating_range.grid_remove()
            self.rating_choice.grid_remove()


    # run function for each
    def run_bfs(self):
        self.traversal("bfs")

    def run_dfs(self):
        self.traversal("dfs")


    # call run based on selections
    def traversal(self, method):
        filter_type = self.filter_type_entry.get()
        filter_value = self.filter_value_entry.get()
        apply_rating = self.second_rating_prompt.get() == "yes"
        rating_val = self.rating_choice.get() if apply_rating else None

        # catch and set error messages
        try:
            limit = int(self.input_value.get())
            if limit <= 0:
                raise ValueError
        except ValueError:
            if not filter_type or not filter_value:
                messagebox.showerror("Missing Input", "Fill out all fields.")
                return
            messagebox.showerror("Error", "Please enter a positive integer.")
            return

        self.root = tree_build.tree_build(self.books, filter_type)

        if method == "bfs":
            books = traverse.bfs_collection(self.root, filter_value, limit, rating_val)
        else:
            books = traverse.dfs_collection(self.root, filter_value, limit, rating_val)

        # displaying error if there are no matching books for desired fields
        if rating_val and not books:
            messagebox.showerror("No Valid Results", "No books in the selected rating range.")

        self.populate_tbl(books)


    # repeat of traversal but to get time taken to traverse
    def traversal_comparison(self):
        filter_type = self.filter_type_entry.get()
        filter_value = self.filter_value_entry.get()
        apply_rating = self.second_rating_prompt.get() == "yes"
        rating_val = self.rating_choice.get() if apply_rating else None


        # catch and set error messages
        try:
            limit = int(self.input_value.get())
            if limit <= 0:
                raise ValueError
        except ValueError:
            if not filter_type or not filter_value:
                messagebox.showerror("Missing Input", "Fill out all fields.")
                return
            messagebox.showerror("Error", "Please enter a positive integer.")
            return

        # run BFS and DFS and store the time it takes each
        self.root = tree_build.tree_build(self.books, filter_type)
        start_bfs = time.perf_counter()
        books_bfs = traverse.bfs_collection(self.root, filter_value, limit, rating_val)
        bfs_time = time.perf_counter() - start_bfs

        start_dfs = time.perf_counter()
        books_dfs = traverse.dfs_collection(self.root, filter_value, limit, rating_val)
        dfs_time = time.perf_counter() - start_dfs

        # output message for speed comparison between BFS and DFS
        faster = "BFS" if bfs_time < dfs_time else "DFS"
        self.comparison.config(
            text=(
                  f"BFS found {len(books_bfs)} books in {bfs_time:.8f} s | "
                  f"DFS found {len(books_dfs)} books in {dfs_time:.8f}s - "
                  f"{faster} was faster!"
            )
        )

    # printing and adding values in table
    def populate_tbl(self, books):
        for row in self.table.get_children():
            self.table.delete(row)
        for book in books:
            self.table.insert('', tk.END, value=(book.title, book.author, book.isbn, book.rating))

    # function for reset button to clear all filters
    def reset_filters(self):
        self.filter_type_entry.set('')
        self.filter_value_entry.set('')
        self.second_rating_prompt.set("")
        self.rating_choice.set('')
        self.input_value.delete(0, tk.END)

        self.rating_range.grid_remove()
        self.rating_choice.grid_remove()

        # remove previous table
        for row in self.table.get_children():
            self.table.delete(row)

        self.comparison.config(text="")

# run
if __name__ == "__main__":
    root = tk.Tk()
    app = BookBranch(root)
    root.mainloop()

