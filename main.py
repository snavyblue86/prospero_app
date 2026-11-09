import http.server, socketserver
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            html="<html><head><meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1'><style>body{margin:0;background:#000;overflow:hidden}video{width:100vw;height:100vh;object-fit:cover;display:block}a{position:fixed;bottom:20px;left:0;right:0;text-align:center;color:#00f0ff;font-family:monospace}</style></head><body><video autoplay muted playsinline><source src='/boot.mp4' type='video/mp4'></video><a href='/main'>ENTER PROSPERO</a></body></html>"
            self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
            self.wfile.write(html.encode())
        elif self.path == "/main":
            html="<html><body style='background:#000;color:#00f0ff;font-family:monospace;text-align:center;padding-top:40px'><h1>PROSPERO - COMPLETE ARCHITECTURE</h1><p>BOOT VIDEO - DONE</p><p>ARCHITECTURE - DONE</p><p>READY FOR REAL CORE</p></body></html>"
            self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
            self.wfile.write(html.encode())
        else:
            super().do_GET()
print("BOOT PAGE RUNNING - open http://localhost:8096/")
socketserver.ThreadingTCPServer(("",8096),H).serve_forever()
