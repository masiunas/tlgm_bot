import csv
import re
import random
#
# text = """
# na podstawie - на основе
# dostać - получить
# """
#

def get_data() -> dict:
    dictionary = dict()
    with open("dictionary.csv", 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            word, translation = row
            dictionary[word] = translation
    return dictionary


def get_random_data(count=5):
    data = get_data()
    random_keys = random.sample(data.keys(), count)
    random_keys.sort()
    return {key:data[key] for key in random_keys}

def convert_str_to_data(text: str) -> dict:
    pattern = re.compile(r'(?P<word>[\S\s]+?)\s*-\s*(?P<translation>.+)')
    matches = pattern.findall(text)
    if not matches:
        pattern = re.compile(r'(?P<word>[\w\s]+)\s*–\s*(?P<translation>.+)')
        matches = pattern.findall(text)
    return {word.strip(): translation.strip() for word, translation in matches}

def write_data(data: dict):
    with open("dictionary.csv", 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        for word, translation in data.items():
            csv_writer.writerow([word, translation])

def sanitaze_data(data: dict):
    return {word.lower().capitalize().strip(): translation.lower().capitalize().strip() for word, translation in data.items()}

def add_data(text: str) -> bool:
    """Добавляет новые слова в словарь"""
    new_data = convert_str_to_data(text)
    if new_data:
        data = sanitaze_data(new_data)
        old_data = get_data()
        data.update(old_data)
        write_data(data)
        return True
    return False