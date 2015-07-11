import sys
from random import choice


class MarkovMachine(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        body = ""

        for filename in filenames:
            text_file = open(filename)
            body = body + text_file.read()
            text_file.close()

        self.make_chains(body)

    def make_chains(self, corpus):
        """Takes input text as string; returns dictionary of markov chains."""

        self.chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in self.chains:
                self.chains[key] = []

            self.chains[key].append(value)

    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""
        MAX_TEXT_LENGTH = 300
        key = choice(self.chains.keys())
        words = " ".join([key[0], key[1]])

        while key in self.chains and len(words) < 300:          
            word = choice(self.chains[key])
            words += " " + word
            key = (key[1], word)

        return words

    def tidy_text(self, text):
        #runs replace for puctuation
        characters_to_replace = {
                                '...': '',
                                '-': '',
                                '[': '',
                                ']': '',
                                '(': '',
                                ')': ''
                                }
        for key, value in characters_to_replace.iteritems():
            text = text.replace(key, value)
        #capitalizes characters at beginning and after periods

        #adds punctuation at end.
        return text


if __name__ == "__main__":
    # filenames = sys.argv[1:]



    generator = MarkovMachine()
    # generator.read_files(filenames)
    #print generator.make_text()

    test_text = "so much.   [brackets] \n and (paren) and... ---"
    generator.tidy_text(test_text)