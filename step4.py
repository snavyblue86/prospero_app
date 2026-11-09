import http.server, socketserver
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        html="<html><body style='background:#000;color:#00f0ff;font-family:monospace;text-align:center;padding-top:40px'><h1>STEP 4 - CORE CHECK</h1><p>PS1 - NOT_INSTALLED</p><p>PS2 - NOT_INSTALLED</p><p>PS3 - NOT_INSTALLED</p><p>PS4 - NOT_INSTALLED</p><p>Plug is ready. No fake running.</p></body></html>"
        self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
        self.wfile.write(html.encode())
print("STEP 4 RUNNING - open http://localhost:8085/")
socketserver.ThreadingTCPServer(("",8085),H).serve_forever()
