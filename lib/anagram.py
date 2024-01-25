# your code 
word_list = ['enlists', 'google', 'inlets', 'banana']

class Anagram:

    def __init__(self, word):
        self.word = word

    def word(self):
        return self._word

    def set_word(self, word):
        self._word = word

    word = property(word, set_word)

    def match(self, word_list):
        sorted_self_word = sorted(self.word)
        result =  [item for item in word_list if sorted(item) == sorted_self_word]
        if result:
            return result
        else:
            return []

listen = Anagram("listen")
listen.match(word_list = ['enlists', 'google', 'inlets', 'banana'])
