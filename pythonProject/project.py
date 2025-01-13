from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Устанавливаем код ответа HTTP
        self.send_response(200)

        # Устанавливаем заголовки
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Отправляем тело ответа
        self.wfile.write(b"Hello, World!")

host = "0.0.0.0"
port = 8060
server = HTTPServer((host, port), SimpleHTTPRequestHandler)
print(f"HTTP сервер запущен на {host}:{port}")

# Запускаем сервер
server.serve_forever()

