import http.server, socketserver, os
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        games=[]
        for d in [os.path.expanduser("~/storage/downloads"), os.path.expanduser("~/prospero_app")]:
            if not os.path.exists(d): continue
            for f in os.listdir(d):
                if f.lower().endswith((".iso",".bin",".cue",".chd",".pkg",".elf",".img")):
                    games.append(f)
        bios="FOUND" if "SCPH-70012.bin" in games else "MISSING"
        html=f"<html><body style='background:#000;color:#00f0ff;font-family:monospace;text-align:center;padding-top:30px'><h1>STEP 7 - LAUNCH CHECK</h1><p>Pick PS2 + GTA III Mod Menu.iso</p><p>BIOS: {bios}</p><p>CORE: NOT_INSTALLED</p><p>RESULT: WILL NOT FAKE RUN</p><p>Reason: No emulator core plugged in yet</p><p>Architecture is honest now.</p></body></html>"
        self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
        self.wfile.write(html.encode())
print("STEP 7 RUNNING - open http://localhost:8088/")
socketserver.ThreadingTCPServer(("",8088),H).serve_forever()
