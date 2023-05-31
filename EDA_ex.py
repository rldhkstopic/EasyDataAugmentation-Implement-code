import random
import argparse

from random import shuffle
from nltk.corpus import wordnet

class EDA:
    def __init__(self, alpha):
        self.words = ''
        self.n = alpha

        self.argument()

    def argument(self):
        parser = argparse.ArgumentParser(description='EDA method')
        parser.add_argument('-t', '--technique', type=str, help='사용할 EDA 기법 선택', choices=["sr","ri","rs","rd"])
        parser.add_argument('-d', '--data', type=str, help='data 문장 입력',default="hanyang university erica")
        
        args = parser.parse_args()
        self.words = args.data.split(' ')

        if args.technique:
            if args.technique == 'sr':
                print(self.synonym_replacement(self.words, self.n))
            elif args.technique == 'ri':
                print(self.random_insertion(self.words, self.n))
            elif args.technique == 'rs':
                print(self.random_deletion(self.words, self.n))
            elif args.technique == 'rd':
                print(self.random_deletion(self.words, self.n))
            else:
                raise ValueError("Invalid technique choice")

    def synonym_replacement(self, words, n): # 동의어 교체
        new_words = words.copy()
        random_word_list = list(set([word for word in words if word not in self.stop_words]))
        random.shuffle(random_word_list)
        num_replaced = 0
        for random_word in random_word_list:
            synonyms = self.get_synonyms(random_word)
            if len(synonyms) >= 1:
                synonym = random.choice(synonyms)
                new_words = [synonym if word == random_word else word for word in new_words]
                num_replaced += 1
            if num_replaced >= n:
                break

        sentence = ' '.join(new_words)
        return sentence

    def random_insertion(self, words, n): # 랜덤 삽입
        new_words = words.copy()
        for _ in range(n):
            self.add_word(new_words)
        sentence = ' '.join(new_words)
        return sentence

    def add_word(self, new_words):
        synonym_words = []
        counter = True
        while counter:
            random_word = new_words[random.randint(0, len(new_words)-1)]
            synonyms = self.get_synonyms(random_word)
            if len(synonyms) >= 1:
                counter = False
                synonym_word = random.choice(synonyms)
                new_words.insert(random.randint(0,len(new_words)-1),synonym_word)
                break

    def random_deletion(self, words, p): # 랜덤 삭제
        if len(words) == 1:
            return words

        new_words = []
        for word in words:
            r = random.uniform(0, 1)
            if r > p:
                new_words.append(word)

        if len(new_words) == 0:
            rand_int = random.randint(0, len(words)-1)
            return [words[rand_int]]

        sentence = ' '.join(new_words)
        return sentence

    def get_synonyms(self, word): # 유의어 추출
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonym = lemma.name().replace("_", " ").replace("-", " ").lower()
                synonym = "".join([char if char in 'abcdefghijklmnopqrstuvwxyz' else '' for char in synonym])
                if synonym not in synonyms and synonym != word:
                    synonyms.append(synonym)
        return synonyms
    

if __name__ == "__main__":
    eda = EDA(0.5)