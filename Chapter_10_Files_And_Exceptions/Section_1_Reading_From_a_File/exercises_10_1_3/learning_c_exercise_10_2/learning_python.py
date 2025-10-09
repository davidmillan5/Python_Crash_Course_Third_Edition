from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

print(contents)

c_language = contents.replace('Python','C')
print(c_language)