## This is a dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

## This is a list
respondents = ['jen', 'sarah', 'eren', 'mikasa', 'levi', 'edward', 'phil', 'dua']

for respondent in respondents:
    if respondent in favorite_languages.keys():
        print(f"{respondent.title()} thanks for taking the survey.")
    if respondent not in favorite_languages.keys():
        print(f"{respondent.title()} please complete the survey.")