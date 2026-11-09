import http.server, socketserver, os
def scan():
    out=[]
    for d in [os.path.expanduser("~/storage/downloads"), os.path.expanduser("~/prospero_app")]:
        if not os.path.exists(d): continue
        for f in os.listdir(d):
            if f.lower().endswith((".iso",".bin",".cue",".chd",".pkg",".elf",".img")):
                out.append(f)
    return out
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        games=scan()
        items="".join([f"<p>{g}</p>" for g in games]) or "<p>No game files found</p>"
        html=f"<html><body style='background:#000;color:#00f0ff;font-family:monospace;text-align:center;padding-top:40px'><h1>STEP 2 - STORAGE CHECK</h1><h3>Games Found:</h3>{items}</body></html>"
        self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
        self.wfile.write(html.encode())
print("STEP 2 RUNNING - open http://localhost:8083/")
socketserver.ThreadingTCPServer(("",8083),H).serve_forever()
