import http.server, socketserver, os
class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        bios=["SCPH-70012.bin","SCPH-1001.bin","SCPH-5500.bin","SCPH-5501.bin","SCPH-5502.bin"]
        found=[]
        for d in [os.path.expanduser("~/storage/downloads"), os.path.expanduser("~/prospero_app")]:
            if not os.path.exists(d): continue
            for f in os.listdir(d):
                if f in bios: found.append(f)
        items="".join([f"<p>{f} - FOUND</p>" for f in found]) or "<p>No BIOS found yet</p>"
        html=f"<html><body style='background:#000;color:#00f0ff;font-family:monospace;text-align:center;padding-top:40px'><h1>STEP 3 - BIOS CHECK</h1>{items}<p>BIOS = the console's startup chip. No BIOS = no boot.</p></body></html>"
        self.send_response(200); self.send_header("Content-type","text/html"); self.end_headers()
        self.wfile.write(html.encode())
print("STEP 3 RUNNING - open http://localhost:8084/")
socketserver.ThreadingTCPServer(("",8084),H).serve_forever()

