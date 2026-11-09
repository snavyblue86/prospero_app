"""
PROSPERO CORE ARCHITECTURE v5
Layer: CORE INTERFACE
Purpose: Every console (PS1-PS4) uses the SAME plug.
No core fakes a game - if it can't run, it says so.
"""

from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
import time

class CoreState(Enum):
    IDLE = "IDLE"
    LOADING = "LOADING"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"
    STOPPED = "STOPPED"
    ERROR = "ERROR"
    NOT_INSTALLED = "NOT_INSTALLED"

@dataclass
class FrameResult:
    frame_number: int
    fps: float
    cpu_usage: float
    rendered: bool  # True only if a REAL frame was drawn

@dataclass
class CoreInfo:
    name: str
    key: str  # ps1, ps2, ps3, ps4
    state: CoreState
    bios_found: bool
    bios_path: str = ""
    current_game: str = ""
    message: str = ""

class BaseCore(ABC):
    """Every console core MUST implement this. No exceptions."""

    def __init__(self, key: str, name: str):
        self.key = key
        self.name = name
        self.state = CoreState.IDLE
        self.current_game = ""
        self.frame_number = 0
        self.start_time = 0
        self.bios_found = False
        self.bios_path = ""

    # --- REQUIRED INTERFACE ---
    @abstractmethod
    def check_bios(self) -> bool:
        """Return True only if a real BIOS file is found. No fake OK."""
        pass

    @abstractmethod
    def load(self, game_path: str) -> bool:
        """Load a game file. Validate header, don't just trust extension."""
        pass

    @abstractmethod
    def boot(self) -> bool:
        """Boot BIOS + game. Return False if anything missing."""
        pass

    @abstractmethod
    def run_frame(self) -> FrameResult:
        """Run ONE frame. Must return rendered=True only if real frame drawn."""
        pass

    def pause(self):
        if self.state == CoreState.RUNNING:
            self.state = CoreState.PAUSED
            return True
        return False

    def resume(self):
        if self.state == CoreState.PAUSED:
            self.state = CoreState.RUNNING
            return True
        return False

    def stop(self):
        self.state = CoreState.STOPPED
        self.current_game = ""
        self.frame_number = 0
        return True

    def info(self) -> CoreInfo:
        return CoreInfo(
            name=self.name,
            key=self.key,
            state=self.state,
            bios_found=self.bios_found,
            bios_path=self.bios_path,
            current_game=self.current_game,
            message=self._status_message()
        )

    def _status_message(self) -> str:
        if self.state == CoreState.NOT_INSTALLED:
            return f"{self.name} CORE: NOT_INSTALLED - plug a real core in here"
        if not self.bios_found:
            return f"{self.name} CORE: BIOS_MISSING"
        if self.state == CoreState.RUNNING:
            return f"{self.name} CORE: RUNNING {self.current_game}"
        return f"{self.name} CORE: {self.state.value}"

# --- STUB CORES - Architecture placeholders, NOT emulators ---
# These intentionally DO NOT fake frames. They report NOT_INSTALLED / BIOS_MISSING
# When you plug a real core in, you replace just this class.

class PS1Core(BaseCore):
    def __init__(self):
        super().__init__("ps1", "PlayStation 1")
        self.state = CoreState.NOT_INSTALLED
    def check_bios(self) -> bool:
        return False
    def load(self, game_path: str) -> bool:
        self.state = CoreState.ERROR
        return False
    def boot(self) -> bool:
        return False
    def run_frame(self) -> FrameResult:
        return FrameResult(0, 0.0, 0.0, rendered=False)

class PS2Core(BaseCore):
    def __init__(self):
        super().__init__("ps2", "PlayStation 2")
        self.state = CoreState.NOT_INSTALLED
    def check_bios(self) -> bool:
        return False
    def load(self, game_path: str) -> bool:
        self.state = CoreState.ERROR
        return False
    def boot(self) -> bool:
        return False
    def run_frame(self) -> FrameResult:
        return FrameResult(0, 0.0, 0.0, rendered=False)

class PS3Core(BaseCore):
    def __init__(self):
        super().__init__("ps3", "PlayStation 3")
        self.state = CoreState.NOT_INSTALLED
    def check_bios(self) -> bool:
        return False
    def load(self, game_path: str) -> bool:
        self.state = CoreState.ERROR
        return False
    def boot(self) -> bool:
        return False
    def run_frame(self) -> FrameResult:
        return FrameResult(0, 0.0, 0.0, rendered=False)

class PS4Core(BaseCore):
    def __init__(self):
        super().__init__("ps4", "PlayStation 4")
        self.state = CoreState.NOT_INSTALLED
    def check_bios(self) -> bool:
        return False
    def load(self, game_path: str) -> bool:
        self.state = CoreState.ERROR
        return False
    def boot(self) -> bool:
        return False
    def run_frame(self) -> FrameResult:
        return FrameResult(0, 0.0, 0.0, rendered=False)
