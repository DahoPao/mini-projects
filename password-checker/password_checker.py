# password strength checker
# gives a password a score from 0-5 and tells you what to improve
# also checks it against a small list of the most common passwords
# can check a whole file of passwords at once too (one per line)

import sys

COMMON = ["123456", "password", "12345678", "qwerty", "111111", "abc123",
          "password1", "iloveyou", "admin", "letmein", "monkey", "dragon"]

SPECIALS = "!@#$%^&*()-_=+[]{};:,.<>?/"


def score_password(pw):
    score = 0
    hints = []

    if pw.lower() in COMMON:
        return 0, ["this is one of the most common passwords ever, change it now"]

    if len(pw) >= 8:
        score += 1
    else:
        hints.append("make it at least 8 characters")

    if len(pw) >= 12:
        score += 1
    else:
        hints.append("longer is stronger, 12+ is a good goal")

    if any(c.isupper() for c in pw):
        score += 1
    else:
        hints.append("add an uppercase letter")

    if any(c.islower() for c in pw):
        score += 1
    else:
        hints.append("add a lowercase letter")

    if any(c.isdigit() for c in pw):
        score += 1
    else:
        hints.append("add a number")

    if any(c in SPECIALS for c in pw):
        score += 1
    else:
        hints.append("add a special character like ! or #")

    if score > 5:
        score = 5
    return score, hints


def verdict(score):
    if score <= 1:
        return "VERY WEAK"
    if score == 2:
        return "WEAK"
    if score == 3:
        return "OK"
    if score == 4:
        return "GOOD"
    return "STRONG"


def main():
    print("password strength checker")
    print("1. check one password")
    print("2. check a file of passwords (one per line)")
    choice = input("pick 1 or 2: ").strip()

    if choice == "2":
        filename = input("file name: ").strip()
        try:
            f = open(filename, "r", encoding="utf-8", errors="ignore")
            passwords = [line.rstrip("\n") for line in f if line.strip()]
            f.close()
        except FileNotFoundError:
            print("file not found:", filename)
            sys.exit(1)
        for pw in passwords:
            score, hints = score_password(pw)
            print(f"{verdict(score):<10} {pw}")
        return

    pw = input("password to check: ")
    score, hints = score_password(pw)
    print(f"\nscore: {score}/5  ->  {verdict(score)}")
    for h in hints:
        print(" -", h)


main()
