import http.server, socketserver
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        html="<html><body style='background:#000;color:#00f0ff;font-family:monospace;text-align:center;padding-top:30px'><h1>STEP 8 - INPUT CHECK</h1><p>CONTROLLER: NOT_CONNECTED</p><p>KEYBOARD: READY</p><p>TOUCH: READY</p><p>INPUT PLUG: READY</p><p>When a real core plugs in, input plugs in here.</p></body></html>"
        self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
        self.wfile.write(html.encode())
print("STEP 8 RUNNING - open http://localhost:8089/")
socketserver.ThreadingTCPServer(("",8089),H).serve_forever()
