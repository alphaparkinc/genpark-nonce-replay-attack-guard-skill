from client import NonceReplayAttackGuard

def run_example():
    print("=== GenPark Nonce Replay Guard Example ===")
    guard = NonceReplayAttackGuard()
    print("Result:", guard.benchmark_nonce_protection())

if __name__ == "__main__":
    run_example()
