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
        TWEET_TEXT_LENGTH = 140
        #runs replace for puctuation
        characters_to_replace = {
                                '...': '',
                                '-': '',
                                '[': '',
                                ']': '',
                                '(': '',
                                ')': '',
                                ' . ': ' ',
                                '"': ''
                                }
        for key, value in characters_to_replace.iteritems():
            text = text.replace(key, value)
        #Capitalizes first character (capitalize() removes other caps)
        #adds first character to clean text
        clean_text = text[:1].upper() + text[1]
        #capitalizes text after punctuation
        i = 2
        while i < len(text):
            if text[i - 2] == '.' or text[i - 2] == '!' or text[i - 2] == '?':
                clean_text += text[i].upper()
            else:
                clean_text += text[i]
            i += 1

        #adds punctuation at end.
        # or sets word_limit, and deletes everything after last puctuation 
        j = 0
        while j < len(clean_text[:TWEET_TEXT_LENGTH]):
            if text[j] == '.' or text[j] == '!' or text[j] == '?':
                last_punctuation_location = j
            j += 1
        tweetable_clean_text = clean_text[:last_punctuation_location + 1]
        return tweetable_clean_text


# if __name__ == "__main__":
    # filenames = sys.argv[1:]
    # generator = MarkovMachine()
    # generator.read_files(filenames)
    # markov_text = generator.make_text()
    # formatted_text = generator.tidy_text(markov_text)