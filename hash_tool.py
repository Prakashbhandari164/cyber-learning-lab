"""Calculate SHA-256 for text entered locally."""
import hashlib
import getpass

def main():
    print("CYBER LEARNING LAB | SHA-256 Text Hash")
    text = getpass.getpass("Text to hash (hidden; do not use a real password): ")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print("SHA-256:", digest)
    print("Note: hashing is one-way and is not encryption.")

if __name__ == "__main__":
    main()
