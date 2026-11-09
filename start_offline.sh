#!/data/data/com.termux/files/usr/bin/bash
echo "[*] Starting Prospero Offline Architecture..."
export PORT=8080
python3 main.py > prospero.log 2>&1 &
echo $! > prospero.pid
echo "[*] Prospero running in background (PID: $(cat prospero.pid))"
echo "[*] Logging to prospero.log"
echo "[*] Access locally at: http://localhost:8080"
