from http.server import SimpleHTTPRequestHandler, HTTPServer
server = HTTPServer(('0.0.0.0', 5000), SimpleHTTPRequestHandler)
print("Server running on port 5000...")
server.serve_forever()
