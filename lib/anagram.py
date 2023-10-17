class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = [word for word in words if sorted(words) == sorted(self.word)]
        if len(anagrams) > 0:
            return anagrams
        else:
            return []
            

listen = Anagram(['listen'])
anagrams = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(anagrams)
pass