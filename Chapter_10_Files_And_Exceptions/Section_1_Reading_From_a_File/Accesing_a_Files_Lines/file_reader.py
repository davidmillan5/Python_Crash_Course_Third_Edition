from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
count = 1
for line in lines:
    print(f"Line #{count} ---- > {line}")
    count+=1