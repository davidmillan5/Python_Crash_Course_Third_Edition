from pathlib import Path

def file_reader(filename):
    """Function to read txt files"""
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        counter = 0
        lines = contents.splitlines()
        for line in lines:
            counter +=1
            print(f"{counter}. {line.title()}")

file_reader("cats.txt")
file_reader("dogs.txt")
file_reader("cas.txt")