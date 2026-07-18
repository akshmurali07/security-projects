import re
import argparse

common_passwords = [
    "password", "123456", "123456789", "qwerty",
    "abc123", "password1", "iloveyou", "admin",
    "letmein", "welcome"
]

def check_password_strength(password):
    if password.lower() in common_passwords:
        print("❌ This is one of the most common passwords ever!")
        print("Please choose a completely different password.")
        return

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters")

    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    print(f"Password Strength: {strength[score-1]}")
    if feedback:
        print("Suggestions:", ", ".join(feedback))

# argparse part — reads password from terminal
parser = argparse.ArgumentParser()
parser.add_argument("--password", type=str, required=True)
args = parser.parse_args()

check_password_strength(args.password)