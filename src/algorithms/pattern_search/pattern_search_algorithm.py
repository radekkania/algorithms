class SundaySearch:
    """Sunday pattern search algorithm. """

    def _matches_at(self, text, index, pattern):
        for i in range(len(pattern)):
            self._counter += 1
            if text[index + i] != pattern[i]:
                return -1
        return index

    def __init__(self, alphabet, pattern):
        self.last = []
        self.last_dict = {}
        self._pattern = pattern
        self._alphabet = alphabet
        self._prepare_tab()
        self._counter = 0

    # prepares 'last' tab, table with index of last occurrence
    # for each letter from alphabet
    def _prepare_tab(self):
        for letter in self._alphabet:
            index = self._get_last_index_of(letter)
            self.last_dict[letter] = index

    # returns index of last letter occurrence in pattern
    def _get_last_index_of(self, letter):
        j = 1
        for i in range(len(self._pattern) - 1, -1, -1):
            if self._pattern[i] == letter:
                return j
            j += 1
        return len(self._pattern) + 1

    def search2(self, text):
        i = 0
        while i <= len(text) - len(self._pattern):
            match_index = self._matches_at(text, i, self._pattern)
            if match_index == -1 and i + len(self._pattern) < len(text)-1:
                next_elem = text[i + len(pattern)]
                i = i + self.last_dict[next_elem]
            else:
                return i
        return -1

    def search(self, text):
        i = 0
        while i <= len(text) - len(self._pattern):
            match_index = self._matches_at(text, i, self._pattern)
            if match_index == -1:
                if i + len(self._pattern) > len(text) -1:
                    return -1
                next_elem = text[i + len(self._pattern)]
                i = i + self.last_dict[next_elem]
            else:
                return i
        return -1

    def print_tab(self):
        print(self.last)

    def get_counter(self):
        return self._counter


class NaiveSearchAlgorithm:
    """" Naive pattern search algorithm"""

    def __init__(self):
        self._counter = 0

    def _matches_at(self, text, index, pattern):
        for i in range(len(pattern)):
            self._counter += 1
            if text[index + i] != pattern[i]:
                return -1
        return index

    def search(self, text, pattern):
        for i in range(len(text) - len(pattern) + 1):
            match_index = self._matches_at(text, i, pattern)
            if match_index != -1:
                return match_index
        return -1

    def get_counter(self):
        return self._counter


class MorrisPrattAlgorithm:

    def __init__(self):
        self.__PI = []
        self.__counter = 0

    def _matches_at(self, text, index, pattern):
        for i in range(len(pattern)):
            self.__counter += 1
            if text[index + i] != pattern[i]:
                return -1
        return index

    def prepare_tab(self, pattern):
        pattern_size = len(pattern)
        self.__PI = [None for _ in range(pattern_size)]

        self.__PI[0] = -1 # sentry
        ps_len = self.__PI[0]  # length = prefix_suffix_length
        for i in range(1, pattern_size, 1):
            while ps_len > -1 and pattern[ps_len] != pattern[i-1]:
                ps_len = self.__PI[ps_len]
            ps_len += 1
            self.__PI[i] = ps_len

    # pp - pattern position
    # lp - dlugosc prefiksu wzorca p pasujacego do okna wzorca w lanchu
    # i - index of matching sign
    # P - pattern
    def search(self, text, p):
        self.prepare_tab(p)
        pp = -1
        lp = 0
        for i in range(len(text)-1):
            while lp > -1 and p[lp] != text[i]:
                lp = self.__PI[lp]
            lp += 1
            if lp < len(p):
                while pp < i - lp + 1:
                    pp += 1
                pp += 1
                lp = self.__PI

    def print_PI(self):
        print(self.__PI)

    def get_counter(self):
        return self.__counter


if __name__ == "__main__":
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
    import random

    # test 1

    pattern = "abcab"
    alphabet = "abcdef"
    text = ''
    for _ in range(1000):
        text += random.choice(alphabet)
    text += pattern

    print("length of text" + str(len(text)))

    print("Sunday method")
    s = SundaySearch(alphabet, pattern)
    print(s.search(text))
    sundayCount = s.get_counter()

    print("Naive method")
    n = NaiveSearchAlgorithm()
    print(n.search(text, pattern))
    naiveCount = n.get_counter()

    # charts
    algorithms = ('Sunday', 'Naive')
    y_pos = np.arange(len(algorithms))

    results = [sundayCount, naiveCount]

    plt.bar(y_pos, results, align='center', alpha=0.5)
    plt.xticks(y_pos, algorithms)
    plt.ylabel('count of comparision for booth algorithms')
    plt.title('sunday and naive comparision for text of length 10000')

    plt.show()

    # tests 2

    text_alphabets = ['ab', 'abcd', 'abcdefgh', 'abcdefghijklmno', 'abcdefghijklmnopqrstuvwxyz']
    patterns = []
    texts = []
    pattern_sizes = [4, 8, 16, 20]

    text_sizes = [1000, 5000, 10000, 50000]

    # preparing patterns
    for i in range(len(pattern_sizes)):
        pattern = ''
        for _ in range(pattern_sizes[i]):
            pattern += random.choice(text_alphabets[i])
        patterns.append(pattern)

        text = ''
        for _ in range(1000):
            text += random.choice(text_alphabets[i+1])
        texts.append(text)

    sunday_results = []
    naive_results = []

    for i in range(len(patterns)):
        sunday = SundaySearch(text_alphabets[i+1], patterns[i])
        sunday.search(texts[i])
        sunday_results.append(sunday.get_counter())

        naive = NaiveSearchAlgorithm()
        naive.search(texts[i], patterns[i])
        naive_results.append(naive.get_counter())

    print(sunday_results)
    print(naive_results)

    n_test = 4
    fig, ax = plt.subplots()
    index = np.arange(n_test)

    bar_width = 0.35
    opacity = 0.8

    sunday = tuple(sunday_results)
    naive = tuple(naive_results)

    rects1 = plt.bar(index, sunday, bar_width,
                     alpha=opacity,
                     color='b',
                     label='sunday')

    rects2 = plt.bar(index + bar_width, naive, bar_width,
                     alpha=opacity,
                     color='g',
                     label='naive')

    plt.xlabel('Tests')
    plt.ylabel('count of comparision of letters')
    plt.title('comparision sunday vs naive')
    plt.xticks(index + bar_width, ('Test 1', 'Test 2', 'Test 3', 'Test 4'))
    plt.legend()

    plt.tight_layout()
    plt.show()




