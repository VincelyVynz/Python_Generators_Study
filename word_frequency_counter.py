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

