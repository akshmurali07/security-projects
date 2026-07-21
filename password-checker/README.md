# Password Strength Analyzer

A CLI-based Python tool that evaluates password strength and detects commonly used passwords.

## What it does
- Checks password strength across 5 criteria (length, uppercase, lowercase, numbers, special characters)
- Detects if password matches a list of most common passwords
- Provides actionable feedback and improvement suggestions
- Accepts password directly via command line arguments

## How to install
pip install -r requirements.txt

## How to run
python password_checker.py --password YourPasswordHere

## Example Output
Password Strength: Strong
Suggestions: Add uppercase letters

## Technologies Used
- Python 3
- Argparse
- Regex (re module)

## Security Concepts Covered
- Dictionary attack prevention
- Password entropy evaluation
- Input validation