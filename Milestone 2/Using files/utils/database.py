def create_book_table():
    with open('books.txt', 'w') as file:
        pass


def _save_all_books(books):
    with open("books.txt", "w") as file:
        for book in books:
            file.write("{},{},{}\n".format(book["name"], book["author"], book["read"]))


def add_book(name, author):
    with open("books.txt", "a") as file:
        file.write("{},{},0\n".format(name, author))


def get_all_books():
    with open("books.txt", "r") as file:
        lines = [line.strip().split(",") for line in file.readlines()]
    books = [{"name": line[0], "author": line[1], "read": line[2]} for line in lines]
    return books


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book["name"] == name:
            book["read"] = "1"
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book["name"] != name]
    _save_all_books(books)
