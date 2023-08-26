import http.server
import sqlite3
from urllib.parse import parse_qs

class RequestHandler(http.server.BaseHTTPRequestHandler):
    db_path = 'book-rental.sqlite'

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            with open('index.html', 'r') as file:
                index_page = file.read()

            books = self.fetch_books()
            book_list = self.render_book_list(books)
            index_page = index_page.replace("<!-- Book list will be dynamically populated here -->", book_list)
            self.wfile.write(index_page.encode())
        elif self.path == '/add_book':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            add_book_form = self.render_add_book_form()
            self.wfile.write(add_book_form.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/add_book':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            book_data = parse_qs(data.decode())
            self.create_book(book_data)

            self.send_response(302)  # Redirect after POST
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def fetch_books(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Book")
        books = cursor.fetchall()
        connection.close()
        return books

    def create_book(self, book_data):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        query = "INSERT INTO Book (title, author, isbn, genre, publication_date, price) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (
            book_data['title'][0],
            book_data['author'][0],
            book_data['isbn'][0],
            book_data['genre'][0],
            book_data['publication_date'][0],
            book_data['price'][0]
        ))
        connection.commit()
        connection.close()

    def render_book_list(self, books):
        book_list_html = """
        <ul>
            {}
        </ul>
        """

        book_list_items = ""
        for book in books:
            book_list_items += f"<li>{book[1]} by {book[2]}</li>"

        return book_list_html.format(book_list_items)

    def render_add_book_form(self):
        with open("add_book.html", "r") as file:
            return file.read()

def main():
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, RequestHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    main()
