# ---------------- Change to Class ---------------- #

class WordFrequency:
    def __init__(self, filename):
        self.filename = filename
        self.frequency_dict = {}
        self.punctuations = r".,!?;:\"'()[]{}"

    def line_reader(self):
        with open(self.filename) as file:
            for line in file:
                line = line.strip()
                yield line

    def word_frequency(self):
        for line in self.line_reader():
            for word in line.split():
                word = word.lower()
                word = word.strip(self.punctuations)
                if word not in self.frequency_dict:
                    self.frequency_dict[word] = 1
                else:
                    self.frequency_dict[word] += 1
        return self.frequency_dict

    def get_freq_dict(self):
        self.word_frequency()
        return self.frequency_dict

    def get_sorted_freq_dict(self):
        self.word_frequency()
        sorted_freq_dict =dict(sorted(self.frequency_dict.items(), key=lambda item: item[1], reverse=True))
        return sorted_freq_dict
