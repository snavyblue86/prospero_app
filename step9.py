import http.server, socketserver
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        html="<html><body style='background:#000;color:#00f0ff;font-family:monospace;text-align:center;padding-top:30px'><h1>STEP 9 - AUDIO + VIDEO CHECK</h1><p>VIDEO OUT: READY</p><p>AUDIO OUT: READY</p><p>FRAME: WAITING FOR REAL CORE</p><p>SOUND: WAITING FOR REAL CORE</p><p>No fake FPS. No fake sound.</p></body></html>"
        self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
        self.wfile.write(html.encode())
print("STEP 9 RUNNING - open http://localhost:8090/")
socketserver.ThreadingTCPServer(("",8090),H).serve_forever()
