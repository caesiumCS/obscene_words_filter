from Levenshtein import distance
from tqdm import tqdm

class ObsceneFilter:

    def __init__(self, path):

        self.path = path

        f = open(path, 'r')
        self.words = f.readlines()
        f.close()

    def search_word_in_collection(self, word):

        first = 0
        last = len(self.words) - 1

        while first <= last:
            middle = (first + last) / 2

            if self.words[middle] == word:
                return True
            elif self.words[middle] > word:
                last = middle - 1
            elif self.words[middle] < word:
                first = middle + 1
            else:
                return False
            
    def get_closest_with_Levenstein(self, word):
        dist = 10**4
        word = None

        for element in tqdm(self.words):
            d_new = distance(element, word)
            if d_new < dist:
                dist = d_new
                word = element

        return dist, word

    