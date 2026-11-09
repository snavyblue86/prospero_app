"""
PROSPERO MANAGER v5
Layer: CORE MANAGER - The brain between Dashboard and Cores
Dashboard -> Manager -> Core -> Viewport
Manager NEVER draws fake frames. It reports truth.
"""

from core import BaseCore, PS1Core, PS2Core, PS3Core, PS4Core, CoreState, CoreInfo
import os

class CoreManager:
    def __init__(self):
        self.cores = {
            "ps1": PS1Core(),
            "ps2": PS2Core(),
            "ps3": PS3Core(),
            "ps4": PS4Core(),
        }
        self.active_key = None

    def list_cores(self):
        return [c.info() for c in self.cores.values()]

    def get_core(self, key: str) -> BaseCore | None:
        return self.cores.get(key.lower())

    def launch(self, console_key: str, game_path: str) -> dict:
        """
        The ONE launch flow for all consoles.
        Returns a truth report, never a fake RUNNING screen.
        """
        core = self.get_core(console_key)
        if not core:
            return {"ok": False, "reason": f"UNKNOWN_CONSOLE: {console_key}"}

        # 1. Is a core even installed?
        if core.state == CoreState.NOT_INSTALLED:
            return {
                "ok": False,
                "console": core.name,
                "reason": "CORE_NOT_INSTALLED",
                "message": f"{core.name} core not installed yet. Architecture is ready, emulator core is not plugged in.",
                "next_step": f"Plug a real {core.name} core into {core.key}_core.py that implements BaseCore"
            }

        # 2. Does file exist?
        if not os.path.exists(game_path):
            return {"ok": False, "console": core.name, "reason": "FILE_NOT_FOUND", "path": game_path}

        # 3. BIOS check
        if not core.check_bios():
            return {"ok": False, "console": core.name, "reason": "BIOS_MISSING", "message": "BIOS not found. Dump BIOS from your own console."}

        # 4. Load + Boot
        if not core.load(game_path):
            return {"ok": False, "console": core.name, "reason": "LOAD_FAILED", "path": game_path}
        if not core.boot():
            return {"ok": False, "console": core.name, "reason": "BOOT_FAILED"}

        self.active_key = core.key
        return {"ok": True, "console": core.name, "state": core.state.value, "game": game_path, "message": "Core booted. run_frame() will now produce real frames."}

    def status(self) -> dict:
        return {
            "active": self.active_key,
            "cores": [{ "key": c.key, "name": c.name, "state": c.state.value, "bios": c.bios_found, "game": c.current_game } for c in self.cores.values()]
        }

# Quick test - run: python manager.py
if __name__ == "__main__":
    m = CoreManager()
    print("=== PROSPERO CORE MANAGER v5 ===")
    for c in m.list_cores():
        print(f"{c.name} [{c.key}] - {c.state.value} - {c.message}")
    print()
    print("Test launch PS2:")
    print(m.launch("ps2", "/storage/emulated/0/Download/GTA III Mod Menu.iso"))
    print()
    print(m.status())
