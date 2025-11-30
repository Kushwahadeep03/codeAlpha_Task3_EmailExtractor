import re

input_file = "input.txt"
output_file = "emails.txt"

with open(input_file, "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


emails = re.findall(pattern, text)

with open(output_file, "w", encoding="utf-8") as file:
    for email in emails:
        file.write(email + "\n")

print("Emails extracted successfully!")