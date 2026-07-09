#!/usr/bin/env python3
"""Local dev server for Agnes Mortgage — mimics Vercel cleanUrls.
Run: python3 local-server.py  →  http://localhost:8000
"""
import http.server, socketserver, os

PORT = 8000

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("?")[0].split("#")[0]
        if path != "/" and not os.path.splitext(path)[1]:
            candidate = path.lstrip("/") + ".html"
            if os.path.isfile(candidate):
                self.path = "/" + candidate
        super().do_GET()

    def send_error(self, code, *args, **kwargs):
        if code == 404 and os.path.isfile("404.html"):
            self.error_message_format = open("404.html", encoding="utf-8").read()
        super().send_error(code, *args, **kwargs)

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
    print(f"Serving Agnes Mortgage at http://localhost:{PORT} (Ctrl+C to stop)")
    httpd.serve_forever()
