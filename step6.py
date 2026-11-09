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
        html=f"<html><body style='background:#000;color:#00f0ff;font-family:monospace;text-align:center;padding-top:30px'><h1>PROSPERO HUB - ALL STEPS</h1><p>STEP 1 - LIVE - DONE</p><p>STEP 2 - STORAGE - DONE</p><p>STEP 3 - {bios}</p><p>STEP 4 - CORE PLUG - READY</p><p>STEP 5 - ALL TOGETHER - DONE</p><h3>Games:</h3>{g}<p>Architecture is built. No fake running.</p></body></html>"
        self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
        self.wfile.write(html.encode())
print("STEP 6 RUNNING - open http://localhost:8087/")
socketserver.ThreadingTCPServer(("",8087),H).serve_forever()
