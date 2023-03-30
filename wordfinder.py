"""Word Finder: finds random words from a dictionary.

>>> wf = WordFinder("/Users/student/words.txt")
3 words read

>>> wf.random()
'cat'
"""


import random


class WordFinder:
    ...
    def __init__(self, path):
        """Reads file"""
        self.path = path
        self.words = self.read_file()

    def read_file(self):
        """Reads file and returns list of words"""
        file = open(self.path)
        return [word.strip() for word in file]
    
    def random(self):
        """Returns random word from list of words"""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        """Reads file and returns list of words, excluding blank lines and comments"""
        super().__init__(path)
        self.words = [word for word in self.words if word and not word.startswith('#')]



        