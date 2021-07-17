from collections import Counter



class BigramModel():

    def __init__(self, train_pos_set, train_neg_set):
        self.train_positive_set = train_pos_set
        self.train_negative_set = train_neg_set
        self.train_pos_dict = {}
        self.train_neg_dict = {}


    def create_pos_words_dict(self):
        for sentence in self.train_positive_set:
            words_in_sent = sentence.split(' ')
            words_in_sent.insert(0, '<s>')
            words_in_sent.append('</s>')
            words_in_sent = Counter(words_in_sent)
            for word in words_in_sent.keys():
                if word in self.train_pos_dict.keys():
                    self.train_pos_dict[word] += 1
                else:
                    self.train_pos_dict[word] = 1

    def create_neg_words_dict(self):
        for sentence in self.train_negative_set:
            words_in_sent = sentence.split(' ')
            words_in_sent.insert(0, '<s>')
            words_in_sent.append('</s>')
            words_in_sent = Counter(words_in_sent)
            for word in words_in_sent.keys():
                if word in self.train_neg_dict.keys():
                    self.train_neg_dict[word] += 1
                else:
                    self.train_neg_dict[word] = 1