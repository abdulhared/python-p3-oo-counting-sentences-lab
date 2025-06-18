#!/usr/bin/env python3

  
import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # use the setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = re.split(r'[.!?]', self.value)
        cleaned = [s.strip() for s in sentences if s.strip()]
        return len(cleaned)

string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())       # False
print(string.is_question())       # True
print(string.is_exclamation())    # False
print(string.count_sentences()) 