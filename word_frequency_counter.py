def get_word_frequency(filename):
    def line_reader():
        try:
            with open(filename, 'r') as file:
                line = file.readline()
                while line != "":
                    yield line
                    line = file.readline()
        except FileNotFoundError:
            print(f"Could not find {filename}")
        except Exception as e:
            print(e)


    def word_splitter():
        for line in line_reader():
            for word in line.split():
                yield word

    punctuations = r".,!?;:\"'()[]{}"
    frequency_dict = {}
    for word in word_splitter():
        word = word.lower().strip(punctuations)
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1

    def print_freq_dict():
        print(f"Word Frequency: \n{frequency_dict}")

    return frequency_dict

# ---------------- Change to Class ---------------- #

class WordFrequency:
    def __init__(self, filename):
        self.filename = filename
        self.freq_dict = {}
        self.line_reader()
        self.word_splitter()

    def line_reader(self):
        try:
            with open(self.filename, 'r') as file:
                self.line = file.readline()
                while self.line != "":
                    yield self.line
                    self.line = file.readline()
        except FileNotFoundError:
            print(f"Could not fine {self.filename}")
        except Exception as e:
            print(e)

    def word_splitter(self):
        punctuations = r".,!?;:\"'()[]{}"
        while self.line != "":
            for word in self.line:
                self.word = word.split().strip(punctuations)
                yield self.word
                self.freq_counter()

    def freq_counter(self.word):
        if self.word not in self.freq_dict:
            self.freq_dict[self.word] = 1
        else:
            self.freq_dict[self.word] += 1

    def print_freq_dict(self):
        if self.word not in self.freq_list:
            self.freq_counter()
        print(self.freq_dict)

