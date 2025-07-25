from fastapi import FastAPI,Body
app = FastAPI()


BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/")  # Define a route for GET request
def read_root():
    return {"Hello": "World"}


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{title}")
async def get_book_by_title(title: str):
    for book in BOOKS:
        if book.get('title', '').casefold() == title.casefold():
            return book
    return {"error": "Book not found"}



@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

