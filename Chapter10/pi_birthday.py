from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
     pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday in the format mmddyy: ")
if birthday in pi_string:
     print ("Your birthday appears in the digits of pi!")
else: 
     print ("Your birthday does not appear in the digits of pi.")

    