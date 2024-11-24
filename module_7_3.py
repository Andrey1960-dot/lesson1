import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = file_name

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read().lower()
                for punc in [',','.','=','!','?',';',':','-']:
                    text = text.replace(punc, '')
                    words = text.split()
                    all_words[file] = words
                    return all_words

    def find(self, search_word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            for i, word in enumerate(words):
                result[file_name] = i
                return result


    def count(self, search_word:str):
        search_word = search_word.lower()
        word_number = {}
        for file_name, words in self.get_all_words().items():
            word_number[file_name] = words.count(search_word)
            return word_number



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
