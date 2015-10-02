# EmileObama

EmileObama uses the Markov algorithm to generate random text from source documents. 
Markov allows us to use similar word and style choices to the original document, imitating the source. This project uses a Markov Generator class to process file names into text, text into a dictionary of Markov chains, then a dictionary into randomly generated text. This resulting text is processed into a tweetable format, then posted to Twitter using a python twitter wrapper. 
### The Skills
* [Problem Solving] - Breaking down a large problem (randomly generate text) into samller pieces (input file names, get text from files, convert text to dictionary of Markov chains, etc).
* [APIs] - Using the Twitter API via a python library allows us to tweet from a python program.
* [Classes] - Grouping methods into usable classes allows abstraction of code.

### The Stack
* [Python] - Backend code that manipulates incoming data, controls access to the database, and serves data to the webpage through a framework.
* [Python Twitter] - A python wrapper for the Twitter API which allows user authentication and tweeting using python.

### The Data
EmileObama mashes the presidential speeches of Barack Obama with Emile, a long-winded and barely sensical commentator on [Anarchist News](https://www.anarchistnews.org/).
This data is available in two text files. 

### Installation
Clone repo:
```sh
$ git clone https://github.com/KaiDalgleish/EmileObama.git emileObama
$ cd emileObama
```

Install dependencies:
```sh
$ pip install -r requirements.txt
```

Store your Twitter keys in secrets.sh for export as environment variables, then source the file:
```sh
$ source secrets.sh
```

Run tweeter.py to print out Markov text, and tweet it to your account!
```sh
$ python tweeter.py
```
