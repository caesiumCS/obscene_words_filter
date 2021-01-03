from tqdm import tqdm

class WordsGenerator:

    def __init__(self):

        self.letter_changes = {
              'а' : ['а', 'a', '@'],
              'б' : ['б', '6', 'b'],
              'в' : ['в', 'b', 'v'],
              'г' : ['г', 'r', 'g'],
              'д' : ['д', 'd', 'g'],
              'е' : ['е', 'e'],
              'ё' : ['ё', 'e'],
              'ж' : ['ж', 'zh', '*'],
              'з' : ['з', '3', 'z'],
              'и' : ['и', 'u', 'i'],
              'й' : ['й', 'u', 'i'],
              'к' : ['к', 'k', 'i{', '|{'],
              'л' : ['л', 'l', 'ji'],
              'м' : ['м', 'm'],
              'н' : ['н', 'h', 'n'],
              'о' : ['о', 'o', '0'],
              'п' : ['п', 'n', 'p'],
              'р' : ['р', 'r', 'p'],
              'с' : ['с', 'c', 's', '$'],
              'т' : ['т', 'm', 't'],
              'у' : ['у', 'y', 'u'],
              'ф' : ['ф', 'f'],
              'х' : ['х', 'x', 'h' , '}{'],
              'ц' : ['ц', 'c', 'u,'],
              'ч' : ['ч', 'ch'],
              'ш' : ['ш', 'sh'],
              'щ' : ['щ', 'sch'],
              'ь' : ['ь', 'b'],
              'ы' : ['ы', 'bi'],
              'ъ' : ['ъ'],
              'э' : ['э', 'e'],
              'ю' : ['ю', 'io'],
              'я' : ['я', 'ya']}
    
    def get_all_combinations(self, word, letter_changes = None):
        
        if letter_changes is None:
            letter_changes = self.letter_changes

        result = list()

        def recursioin(word, pref, array):

            if len(word) == 0:
                array.append(pref)
                return
            
            letter = word[0]
            word = word[1:]

            if letter_changes.get(letter) is None:
                recursioin(word, pref+letter, array)
            else:
                for possible_change in letter_changes[letter]:
                    recursioin(word, pref+possible_change, array)
        
        recursioin(word, '', result)
        return result

    def create_list_of_obscene_words(self, filename, to_lower = False, letter_changes = None):

        f = open(filename, 'r')
        result = list()

        for line in tqdm(f.readlines()):

            if to_lower:
                line = line.lower()
            
            while line[-1] == ' ' or line[-1] == '\n' or line[-1] == '\t':
                line = line[:-1]
            while line[0] == ' ':
                line = line[1:]

            if len(line) > 0:
                result += self.get_all_combinations(line, letter_changes=letter_changes)
        
        f.close()
        return result

    def create_file_with_obscene_words(self, filename, array):
        
        array = sorted(array)

        f = open(filename, 'w')

        for word in array:
            f.write(word+'\n')
        
        f.close()