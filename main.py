import http.server
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

            self.wfile.write(index_page.encode())
        elif self.path == '/login':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            login_page = self.render_login_page()
            self.wfile.write(login_page.encode())
        elif self.path == '/register':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            register_page = self.render_register_page()
            self.wfile.write(register_page.encode())
        elif self.path == '/forgot_password':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            forgot_password_page = self.render_forgot_password_page()
            self.wfile.write(forgot_password_page.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            login_data = parse_qs(data.decode())

            # Process login data
            
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
        elif self.path == '/register':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            register_data = parse_qs(data.decode())
            
            # Process registration data
            
            self.send_response(302)
            self.send_header('Location', '/login')
            self.end_headers()
        elif self.path == '/forgot_password':
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            forgot_password_data = parse_qs(data.decode())
            
            # Process password recovery data
            
            self.send_response(302)
            self.send_header('Location', '/login')
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def render_login_page(self):
        with open('login.html', 'r') as file:
            return file.read()

    def render_register_page(self):
        with open('register.html', 'r') as file:
            return file.read()

    def render_forgot_password_page(self):
        with open('forgot_password.html', 'r') as file:
            return file.read()

if __name__ == '__main__':
    main()
              