
# ---------------- Change to Class ---------------- #

class WordFrequency:
    def __init__(self, filename):
        self.filename = filename
        self.frequency_dict = {}
        self.processed = False
        self.punctuations = r".,!?;:\"'()[]{}"

    def process_file(self):
        try:
            with open(self.filename, 'r') as file:
                line = file.readline()
                while line != "":
                    for word in line.split():
                        word = word.strip(self.punctuations)
                        if word not in self.frequency_dict:
                            self.frequency_dict[word] = 1
                        else:
                            self.frequency_dict[word] += 1
                    line = file.readline()
                    if line == "":
                        self.processed = True
        except FileNotFoundError:
            print(f"Could not find {self.filename}")

    def get_freq_dict(self):
        if not self.processed:
            self.process_file()
            return self.frequency_dict
