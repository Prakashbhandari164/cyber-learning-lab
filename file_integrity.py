"""Calculate a file's SHA-256 fingerprint to help verify integrity."""
import hashlib
from pathlib import Path

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main():
    raw = input("Path to a file you own or are allowed to inspect: ").strip()
    path = Path(raw).expanduser()
    if not path.is_file():
        print("Error: file not found or path is not a file.")
        return
    print("File:", path.name)
    print("SHA-256:", sha256_file(path))
    print("Save this fingerprint and compare it later to check for changes.")

if __name__ == "__main__":
    main()
