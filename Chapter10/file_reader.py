from pathlib import Path

path = Path('pi_digits.txt')

# Read the file content
contents = path

# Print the content
print(contents)


path = Path('pi_digits.txt')

print("File exists:", path.exists())
