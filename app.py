import re

def remove_characters(text):
    int_numbers = re.findall(r'\d+', text)
    return list(map(int, int_numbers))
