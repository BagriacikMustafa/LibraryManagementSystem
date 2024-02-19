import tkinter as tk
from tkinter import simpledialog

class Library:
    def __init__(self,file_path = "books.txt"):
        self.file_path = file_path
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        book_list = []
        for book in books:
            book_info = book.split(',')
            book_list.append(f"Book: {book_info[0]}, Author: {book_info[1]}, release_year: {book_info[2]}, num_pages: {book_info[3]}")
        return book_list

    def add_book(self, title, author, release_year, num_pages):
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)

    def remove_book(self, title):
        self.file.seek(0)
        books = self.file.read().splitlines()
        updated_books = [book for book in books if title not in book]
        self.file.seek(0)
        self.file.truncate()
        self.file.write('\n'.join(updated_books))

class LibraryGUI:
    def __init__(self, master):
        self.master = master
        self.lib = Library()

        self.menu_label = tk.Label(master, text="*** MENU ***")
        self.menu_label.pack()

        self.list_books_button = tk.Button(master, text="List Books", command=self.list_books,width=15,height=2)
        self.list_books_button.pack()

        self.add_book_button = tk.Button(master, text="Add Book", command=self.add_book,width=15,height=2)
        self.add_book_button.pack()

        self.remove_book_button = tk.Button(master, text="Remove Book", command=self.remove_book,width=15,height=2)
        self.remove_book_button.pack()

        self.display_text = tk.Text(master, height=18, width=65)
        self.display_text.pack()

    def list_books(self):
        book_list = self.lib.list_books()
        self.display_text.delete(1.0, tk.END)  # Clear previous content
        for book in book_list:
            self.display_text.insert(tk.END, book + '\n')

    def add_book(self):
        title = simpledialog.askstring("Input", "Enter Book Title:")
        author = simpledialog.askstring("Input", "Enter Book Author:")
        release_year = simpledialog.askstring("Input", "Enter Release Year:")
        num_pages = simpledialog.askstring("Input", "Enter Number of Pages:")
        self.lib.add_book(title, author, release_year, num_pages)

    def remove_book(self):
        title = simpledialog.askstring("Input", "Enter Book Title to Remove:")
        self.lib.remove_book(title)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("LibraryManagementSystem")
    root.configure(background="lavender")
    root.geometry("600x500")
    app = LibraryGUI(root)
    root.mainloop()
