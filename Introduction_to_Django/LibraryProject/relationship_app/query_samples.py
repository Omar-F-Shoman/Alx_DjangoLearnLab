from .models import Book, Author

def list_all_books():
    return Book.objects.all()

def query_books_by_author(author_id):
    return Book.objects.filter(author_id=author_id)
