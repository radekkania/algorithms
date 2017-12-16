class SearchAlgorithmBase:
    def __init__(self):
        self.__counter = 0

    def __matches_at(self, text, index, pattern):
        for i in range(len(pattern)):
            self._counter += 1
            if text[index + i] != pattern[i]:
                return -1
        return index

    def get_counter(self):
        return self.__counter

