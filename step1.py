import http.server, socketserver
HTML = "<html><body style='background:#000;color:#00f0ff;font-family:monospace;text-align:center;padding-top:80px'><h1>PROSPERO ARCHITECTURE IS LIVE</h1><p>STEP 1 WORKS</p></body></html>"
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
        self.wfile.write(HTML.encode())
print("STEP 1 RUNNING - open http://localhost:8082/")
socketserver.ThreadingTCPServer(("",8082),H).serve_forever()
