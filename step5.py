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
        g="".join([f"<p>{x}</p>" for x in games]) or "<p>No games</p>"
        bios="SCPH-70012.bin - FOUND" if "SCPH-70012.bin" in games else "BIOS - MISSING"
        html=f"<html><body style='background:#000;color:#00f0ff;font-family:monospace;text-align:center;padding-top:30px'><h1>STEP 5 - ALL TOGETHER</h1><p>ARCHITECTURE - LIVE</p><p>CORE - NOT_INSTALLED</p><p>{bios}</p><h3>Games:</h3>{g}</body></html>"
        self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
        self.wfile.write(html.encode())
print("STEP 5 RUNNING - open http://localhost:8086/")
socketserver.ThreadingTCPServer(("",8086),H).serve_forever()
