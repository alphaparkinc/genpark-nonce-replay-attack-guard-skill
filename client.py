import time
from typing import Dict, Any

class NonceReplayAttackGuard:
    def __init__(self, window_sec: float = 300.0):
        self.seen_nonces: Dict[str, float] = {}
        self.window_sec = window_sec

    def check_and_record(self, nonce: str) -> Dict[str, Any]:
        now = time.time()
        expired = [n for n, ts in self.seen_nonces.items() if now - ts > self.window_sec]
        for n in expired:
            del self.seen_nonces[n]
        if nonce in self.seen_nonces:
            return {"accepted": False, "reason": "REPLAY_DETECTED", "nonce": nonce}
        self.seen_nonces[nonce] = now
        return {"accepted": True, "nonce": nonce, "active_nonces_count": len(self.seen_nonces)}

    def benchmark_nonce_protection(self) -> Dict[str, Any]:
        first = self.check_and_record("agent_nonce_xyz123")
        second = self.check_and_record("agent_nonce_xyz123")
        return {"first_request": first, "second_replay": second}
