"""Basic local password-strength feedback. Input is not saved or transmitted."""
import getpass
import string

def assess(password: str) -> tuple[int, list[str]]:
    score = 0
    tips = []
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 12 characters when possible.")
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Consider mixing uppercase and lowercase letters.")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Consider including numbers.")
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Consider including symbols.")
    common = {"password", "12345678", "qwerty", "letmein", "admin"}
    if password.lower() in common:
        score = 0
        tips.append("Avoid common, predictable passwords.")
    return score, tips

def main():
    print("CYBER LEARNING LAB | Local Password Checker")
    password = getpass.getpass("Enter a test password (input is hidden): ")
    score, tips = assess(password)
    labels = ["Very weak", "Weak", "Fair", "Fair", "Good", "Stronger"]
    print(f"Basic estimate: {labels[min(score, 5)]}")
    print("This is a simple educational estimate, not a breach check.")
    for tip in tips:
        print(f"- {tip}")
    print("Use a unique password and enable multi-factor authentication.")

if __name__ == "__main__":
    main()
