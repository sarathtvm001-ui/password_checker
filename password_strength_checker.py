# Password Strength Checker
# Checks length, uppercase, lowercase, numbers, and special characters.

password = input("Enter your password: ")

score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("Use at least 8 characters.")

if any(ch.isupper() for ch in password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter (A-Z).")

if any(ch.islower() for ch in password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter (a-z).")

if any(ch.isdigit() for ch in password):
    score += 1
else:
    feedback.append("Add at least one number (0-9).")

if any(not ch.isalnum() for ch in password):
    score += 1
else:
    feedback.append("Add at least one special character (such as @, #, or !).")

print("\nPassword strength:")

if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")

if feedback:
    print("\nSuggestions to improve your password:")
    for item in feedback:
        print("-", item)
else:
    print("Good! Your password meets all the basic checks.")

# Note: This is a basic educational checker, not a full security audit.
